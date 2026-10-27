"""Copy published aggregate values from the camera-ready source into plot tables."""

from __future__ import annotations

import csv
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARTICLE = ROOT.parent
PAPER = ARTICLE / "paper.tex"
DATA = ROOT / "data"


def main() -> None:
    source = PAPER.read_text()
    tables = re.findall(
        r"table\[x=length,y=estimate,y error minus=errminus,y error plus=errplus\]"
        r"\s*\{([^}]+)\}",
        source,
    )
    if len(tables) != 2:
        raise ValueError("Expected the two camera-ready length-retrieval tables.")
    rows = [[line.split() for line in table.strip().splitlines()[1:]] for table in tables]
    if any(len(direction) != 4 for direction in rows):
        raise ValueError("Expected four source-length bands in each direction.")
    quality = re.search(
        r"COMETKiwi followed a different pattern, with means of "
        r"([\d.]+), ([\d.]+), ([\d.]+), and ([\d.]+) across",
        source,
    )
    coverage = re.search(
        r"Emotion-lexicon coverage was zero in ([\d.]+)\\% of Portuguese "
        r"responses and ([\d.]+)\\% of English responses",
        source,
    )
    if quality is None or coverage is None:
        raise ValueError("Expected the published COMETKiwi and coverage summaries.")
    DATA.mkdir(exist_ok=True)
    with (DATA / "length_results.tsv").open("w", newline="") as stream:
        writer = csv.writer(stream, delimiter="\t", lineterminator="\n")
        writer.writerow(
            ["x", "length", "en_pt", "en_pt_minus", "en_pt_plus",
             "pt_en", "pt_en_minus", "pt_en_plus", "cometkiwi"]
        )
        for index, (en_pt, pt_en, comet) in enumerate(
            zip(rows[0], rows[1], quality.groups(), strict=True)
        ):
            if en_pt[0] != pt_en[0]:
                raise ValueError("Retrieval directions have different length bands.")
            writer.writerow(
                [index, en_pt[0].replace("--", "-"),
                 *(f"{100 * float(value):.8f}" for value in en_pt[1:]),
                 *(f"{100 * float(value):.8f}" for value in pt_en[1:]), comet]
            )
    with (DATA / "emotion_coverage.tsv").open("w", newline="") as stream:
        writer = csv.writer(stream, delimiter="\t", lineterminator="\n")
        writer.writerow(["language", "zero_coverage"])
        writer.writerows(zip(["Portuguese", "English"], coverage.groups(), strict=True))
    inputs = [PAPER, ARTICLE / "authors_camera_ready.tex",
              ARTICLE / "appendix.tex", ARTICLE / "main_final.pdf"]
    manifest = {
        "source": "../paper.tex",
        "source_files_sha256": {
            path.name: hashlib.sha256(path.read_bytes()).hexdigest() for path in inputs
        },
        "retrieval": {
            "unit": "percent",
            "directions": ["English query to Portuguese candidates",
                           "Portuguese query to English candidates"],
            "interval": "95% percentile bootstrap, clustered by survey-specific record",
            "resamples": 2000,
            "candidate_count": 44118,
        },
        "quality": {"measure": "mean COMETKiwi", "unit": "model score"},
        "coverage": {"measure": "responses with zero emotion-lexicon coverage",
                     "unit": "percent"},
    }
    (DATA / "source_manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    print("Extracted published aggregate values from paper.tex.")


if __name__ == "__main__":
    main()

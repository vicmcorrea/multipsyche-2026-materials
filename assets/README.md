# Institutional marks

The current header uses the four affiliations listed in the camera-ready paper.
All marks retain their original geometry and proportions.

| Institution | Included artwork | Source |
| --- | --- | --- |
| Universidade de São Paulo | usp.pdf, usp-black.svg | Existing USP vector in the author-owned GPMH website repository, checked against the [USP identity guidance](https://scs.usp.br/identidadevisual/identidade-visual-referencias-de-elementos-visuais/) |
| Great People Mental Health | gpmh.pdf, gpmh.svg | [Official website header artwork](https://gpmh.com.br/brand/logos/full-black-cerise-gptw-red-horizontal.svg) |
| Faculdade de Ciências Médicas da Santa Casa de São Paulo | santa-casa.png | [Official faculty media file](https://fcmsantacasasp.edu.br/vemprasanta/wp-content/uploads/2025/04/FCMSCSP-Logotipo.png) |
| Universidade Federal do Pará | ufpa.pdf | [Official institutional mark downloads](https://ufpa.br/brasao/) |

The original USP master usp.svg has a light color intended for dark backgrounds.
usp-black.svg uses the standard black monochrome color on this white poster.
Only the fill color changes. Paths and proportions are preserved.
The GPMH file retains the complete published lockup, including its GPTW mark.

The SVG marks were converted to vector PDFs with rsvg-convert. These PDFs are
included, so ordinary poster compilation requires only the LaTeX toolchain.
The Santa Casa PNG has 1100 by 438 pixels and prints at approximately 397 ppi
at its current size. logo_sources.json records asset provenance and hashes.

The earlier nilc.pdf and icmc-usp.pdf files are retained for previous revisions
and are unused by the current poster.

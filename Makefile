PYTHON ?= python3.14
LATEXMK ?= latexmk
POSTER := output/pdf/AACL_2026_MultiPsyche_2_poster.pdf

.PHONY: all data preview clean

all:
	mkdir -p build output/pdf
	$(LATEXMK) -quiet -pdf -interaction=nonstopmode -halt-on-error -file-line-error -outdir=build main.tex
	cp build/main.pdf $(POSTER)

data:
	$(PYTHON) scripts/extract_plot_data.py

preview: all
	pdftoppm -scale-to 2400 -png -singlefile $(POSTER) output/poster-preview

clean:
	$(LATEXMK) -c -outdir=build main.tex

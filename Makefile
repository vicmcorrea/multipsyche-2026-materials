LATEXMK ?= latexmk
POSTER := output/pdf/AACL_2026_MultiPsyche_2_poster.pdf

.PHONY: all preview clean

all:
	mkdir -p build output/pdf
	$(LATEXMK) -quiet -pdf -interaction=nonstopmode -halt-on-error -file-line-error -outdir=build main.tex
	cp build/main.pdf $(POSTER)

preview: all
	pdftoppm -scale-to 2400 -png -singlefile $(POSTER) output/poster-preview

clean:
	$(LATEXMK) -c -outdir=build main.tex

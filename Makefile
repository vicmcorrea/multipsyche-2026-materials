LATEXMK ?= latexmk
POSTER := output/poster/AACL_2026_MultiPsyche_2_poster.pdf
SLIDES := output/slides/AACL_2026_MultiPsyche_2_slides.pdf

.PHONY: all poster slides preview poster-preview slides-preview clean

all: poster slides

poster:
	mkdir -p build/poster output/poster
	cd poster && $(LATEXMK) -quiet -pdf -interaction=nonstopmode -halt-on-error -file-line-error -outdir=../build/poster main.tex
	cp build/poster/main.pdf $(POSTER)

slides:
	mkdir -p build/slides output/slides
	cd slides && $(LATEXMK) -quiet -pdf -interaction=nonstopmode -halt-on-error -file-line-error -outdir=../build/slides main.tex
	cp build/slides/main.pdf $(SLIDES)

preview: poster-preview slides-preview

poster-preview: poster
	mkdir -p output/previews
	pdftoppm -scale-to 2400 -png -singlefile $(POSTER) output/previews/poster

slides-preview: slides
	mkdir -p output/previews/slides
	pdftoppm -scale-to 1600 -png $(SLIDES) output/previews/slides/slide

clean:
	cd poster && $(LATEXMK) -c -outdir=../build/poster main.tex
	cd slides && $(LATEXMK) -c -outdir=../build/slides main.tex

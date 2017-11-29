TEX = pdflatex -shell-escape -interaction=nonstopmode -file-line-error

.PHONY: all feuille_de_triche.pdf

all : feuille_de_triche.pdf

feuille_de_triche.pdf : feuille_de_triche.tex
	$(TEX) science_po.tex
	$(TEX) science_po.tex

clean :
	rm *.aux
	rm *.log
	rm *.nav
	rm *.out
	rm *.pdf
	rm *.snm
	rm *.toc
	rm *.vrb

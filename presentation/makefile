TEX = pdflatex -shell-escape -interaction=nonstopmode -file-line-error

.PHONY: all view

all : science_po.pdf

science_po.pdf : science_po.tex
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

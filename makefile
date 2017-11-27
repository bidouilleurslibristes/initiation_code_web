TEX = pdflatex -shell-escape -interaction=nonstopmode -file-line-error

.PHONY: all presentation td

all : presentation td

presentation :
	(cd presentation && make all)

td :
	(cd td && make all)

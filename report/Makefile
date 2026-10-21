# Render doc.md -> report.pdf (and report.docx) with Pandoc + LaTeX.
# Usage: make | make pdf | make docx | make tex | make clean
#
# The deliverable is accepted as Word (.docx) or PDF, provided the matrices are
# editable and integrated in the document (no screenshots / external links).
# `make pdf` produces the PDF; `make docx` produces an editable Word file.

PANDOC ?= pandoc
SRC    := doc.md
PDF    := report.pdf
DOCX   := report.docx
TEX    := report.tex

PFLAGS := --pdf-engine=xelatex \
          --toc -V toc-title="Contents" \
          -H header.tex \
          -V documentclass=article \
          -V mainfont="DejaVu Serif" \
          -V monofont="DejaVu Sans Mono" \
          -V fontsize=10pt \
          -V papersize=a4 \
          -V geometry:margin=1.5cm,top=1.2cm,bottom=1.2cm \
          -V parskip=4pt \
          -V indent=false

DFLAGS := --toc -V toc-title="Contents"

.PHONY: all pdf docx both tex wordcount check clean

all: pdf

pdf: $(PDF)

docx: $(DOCX)

both: pdf docx

# Running gauge: body word count (sections 1-10, references excluded) against
# the 6,000-8,000 target, plus a per-section breakdown.
wordcount:
	@python3 ../tools/check_report.py --wordcount

# Full verification pass against the rubric (format, integrity, sources).
check:
	@python3 ../tools/check_report.py

$(PDF): $(SRC) header.tex
	$(PANDOC) $(SRC) -o $@ $(PFLAGS)

$(DOCX): $(SRC)
	$(PANDOC) $(SRC) -o $@ $(DFLAGS)

tex: $(TEX)

$(TEX): $(SRC)
	$(PANDOC) $(SRC) -o $@ --standalone

clean:
	rm -f $(PDF) $(DOCX) $(TEX) *.aux *.log *.toc *.out *.lof *.lot *.fls *.fdb_latexmk

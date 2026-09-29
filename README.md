# Gregorio B. Lontok (1894 to 1959)

This repository holds research on my grandfather, Gregorio B. Lontok, whom the family calls Lolo. He was a Filipino agronomist trained at the UP College of Agriculture in Los Baños. He ran sugarcane experiments in Negros Occidental in the late 1920s and ended his career as Superintendent of La Granja Experiment Station in La Carlota.

The goal is to check the family's own account of his life against outside records, and to cite every claim so any relative can follow a link and see the source.

## What's here

- `08426C04-...PNG` is the family's typed "A Biographical Record" of his career.
- `2A3073DC-...PNG` is the family's list of his writings from 1924 to 1954.
- `reports/Gregorio B Lontok life and work.md` is the full cited report, including a claim-by-claim check of the biography and a corrected list of his writings.
- `research_notes/Gregorio B Lontok life and work/` has the notes behind the report. There are three research tracks (publications, career, and origins and wartime) plus a fact-check pass that re-opened the key sources.
- `site/` has the shareable web page and the script that builds it from the report.

## How claims are labeled

Every claim carries one of three labels. Confirmed means a source outside the family papers says it. Partial means a source supports part of it. Family only means we've found it only in the family documents so far, which doesn't make it wrong.

## Rebuilding the page

The page is generated from the report, so edit the report first and then rebuild.

```sh
python3 -m venv .venv
.venv/bin/pip install -r site/requirements.txt
.venv/bin/python site/build.py
```

That writes `site/lolo-gregorio-lontok.html` with the two family documents embedded as images.

## Open questions

The report ends with a list of places to look next. The biggest gaps are his wife's name, which an unsourced family tree gives as Esperanza Odjar or Odejar, and whether the agronomist Gregorio O. Lontok, Jr. was his son. Other gaps are his whereabouts from 1935 to 1948 and the wartime cassava story. If you know something the record doesn't, tell Greg and the report will be updated.

This is a first draft and is open to corrections.

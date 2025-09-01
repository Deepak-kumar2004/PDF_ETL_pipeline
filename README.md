# PDF ETL Pipeline

A simple Python pipeline to (1) extract text from PDF files, (2) structure the content into tabular form, and (3) persist the results for analysis.

## Features
- Watches a directory for new PDF files every 30 minutes (scheduler loop in `ETL.py`).
- Extracts text from PDFs using `pdfminer.six`.
- Stores raw extracted text (example: `output.txt`).
- Provides a curated CSV (`Curated_Book_data_anlysis.csv`) with paragraph- and chapter-level metadata (word counts, sentence counts, part-of-speech style summaries, etc.).
- Jupyter Notebook (optional) for exploration (`Project_3(2)_Deepak&Pankaj.ipynb`).
- Fully reproducible with a few Python dependencies.

## Repository Contents
| File | Description |
|------|-------------|
| ETL.py | Scheduler-based ETL script (runs every 30 minutes) |
| book.pdf | Example source PDF document |
| output.txt | Extracted raw/semi-processed text |
| Curated_Book_data_anlysis.csv | Curated structured dataset (paragraph-level stats) |
| Project_3(2)_Deepak&Pankaj.ipynb | Exploration / analysis notebook |
| Project_3(1)_deepak&pankaj.pdf | Project write-up / reference |
| LICENSE | MIT License |
| README.md | Project documentation |

---

## Data Flow / Architecture
```
        +-----------+
        | book.pdf  |
        +-----+-----+
              |
              |  (Extract: PDF parsing)
              v
        +-----------+
        | Raw Text  |  -> output.txt
        +-----+-----+
              |
              |  (Transform: cleaning, parsing, feature engineering)
              v
        +-----------------------------+
        | Curated Structured Dataset  | -> Curated_Book_data_anlysis.csv
        +---------------+-------------+
                        |
                        | (Load / Analyze)
                        v
        +-----------------------------+
        | Jupyter Notebook / Insights |
        +-----------------------------+
```

---

## Installation
Create and activate a virtual environment (recommended) and install dependencies:

```bash
python -m venv .venv
# Linux / macOS
source .venv/bin/activate
# Windows
.\.venv\Scripts\activate

pip install pandas pdfminer.six schedule plotly
# (Optional, for notebook)
pip install notebook
```

## Usage
Run the ETL scheduler:

```bash
python ETL.py
```

The script:
- Monitors the configured `pdf_directory`
- Processes any new `.pdf` files
- Writes extracted text and curated CSVs alongside a record of processed PDFs (`processed_pdfs.txt`)

To stop, interrupt the process (Ctrl+C).

## Notes
- Default paths in `ETL.py` point to a local system directory. Adjust `pdf_directory` and `output_directory` to match your environment.
- The curated CSV included demonstrates the target structure and metrics produced after transformation.
- Plotly is imported; you can extend the script or the notebook to build visualizations.

## Author
Deepak Kumar (2025)

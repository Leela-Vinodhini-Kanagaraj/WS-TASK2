##  Overview

This project is a Python-based tool for extracting tabular data from PDF documents. Using libraries like `pdfplumber` and `pandas`, it processes all PDF files in a designated folder and saves the extracted tables into a separate directory. This is especially useful for automating the conversion of report tables into usable spreadsheet formats.

---

##  Project Structure
WS-TASK2/

├── pdfs/ # Output folder containing PDF files

├── tables/ # Output folder for extracted tables

└── t2.py # Main Python script to perform the extraction
- `pdfs/`: Placed all the PDF documents processed over here.
- `tables/`: The folder where the script will save the extracted tables.
- `t2.py`: The main script that scans the `pdfs/` folder and extracts tables using `pdfplumber`.

---

##  Requirements

Before running the script, ensure you have Python installed along with the following libraries:

- `pdfplumber`
- `pandas`

---
##  How to Use

Clone this Repository or copy the script into a .py file.

Install dependencies
Run the Script
Check Output:
 -PDFs will be saved in the pdfs/ folder.
 -Extracted CSV tables will be in the tables/ folder, named like:
      tables/document_1_page1.csv

---

## Script to run

```bash
   git clone https://github.com/Leela-Vinodhini-Kanagaraj/WS-TASK2.git
   cd WS-TASK2
   pip install requests beautifulsoup4 pymupdf pandas
   python script.py

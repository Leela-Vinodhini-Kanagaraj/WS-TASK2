import os
import requests
from bs4 import BeautifulSoup
import fitz
import pandas as pd
url = 'https://tnathleticassociation.com/results/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
os.makedirs("pdfs", exist_ok=True)
os.makedirs("tables", exist_ok=True)
pdf_links = []
for link in soup.find_all('a', href=True):
    href = link['href']
    if href.lower().endswith('.pdf'):
        full_url = requests.compat.urljoin(url, href)
        pdf_links.append(full_url)

print(f"Found {len(pdf_links)} PDF(s).")
for i, pdf_url in enumerate(pdf_links, 1):
    pdf_name = f"pdfs/document_{i}.pdf"
    print(f"Downloading: {pdf_url}")
    pdf_response = requests.get(pdf_url)
    with open(pdf_name, 'wb') as f:
        f.write(pdf_response.content)
    doc = fitz.open(pdf_name)
    for page_number, page in enumerate(doc, start=1):
        blocks = page.get_text("dict")["blocks"]
        table_data = []
        for block in blocks:
            if "lines" in block:
                for line in block["lines"]:
                    row = [span["text"].strip() for span in line["spans"]]
                    if row:
                        table_data.append(row)
        if len(table_data) > 1:
            df = pd.DataFrame(table_data)
            csv_name = f"tables/document_{i}_page{page_number}.csv"
            df.to_csv(csv_name, index=False, header=False)
            print(f"Saved: {csv_name}")
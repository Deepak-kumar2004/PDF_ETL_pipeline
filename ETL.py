import os
import time
import schedule
import pandas as pd
from pdfminer.high_level import extract_text
import plotly.express as px
import json

# Directory where PDF files are stored
pdf_directory = "/mnt/chromeos/MyFiles/Downloads/Project_3_Deepak&Pankaj"
output_directory = "/mnt/chromeos/MyFiles/Downloads/Project_3_Deepak&Pankaj"

# Store the list of already processed PDFs
processed_pdfs_file = os.path.join(output_directory, "processed_pdfs.txt")

# Check for processed PDFs and load them into a set
if os.path.exists(processed_pdfs_file):
    with open(processed_pdfs_file, "r") as f:
        processed_pdfs = set(f.read().splitlines())
else:
    processed_pdfs = set()

# Function to process new PDFs
def process_new_pdfs():
    # Get all PDF files in the directory
    pdf_files = set([f for f in os.listdir(pdf_directory) if f.endswith(".pdf")])

    # Find new PDFs by comparing with the already processed set
    new_pdfs = pdf_files - processed_pdfs

    if new_pdfs:
        for pdf_file in new_pdfs:
            pdf_path = os.path.join(pdf_directory, pdf_file)
            txt_path = os.path.join(output_directory, pdf_file.replace(".pdf", ".txt"))
            csv_path = os.path.join(output_directory, pdf_file.replace(".pdf", ".csv"))

            # Extract text from the PDF
            extract_text_from_pdf(pdf_path, txt_path)

            # Perform the additional processing steps
            # Text cleaning, chapter extraction, text analysis, etc.
            parse_book_structure(txt_path, csv_path)

            # Mark this PDF as processed
            processed_pdfs.add(pdf_file)

        # Save the updated set of processed PDFs
        with open(processed_pdfs_file, "w") as f:
            f.write("\n".join(processed_pdfs))

        print(f"Processed new PDFs: {new_pdfs}")
    else:
        print("No new PDFs found.")

# Schedule the task to run every 30 minutes
schedule.every(30).minutes.do(process_new_pdfs)

# Start the scheduler
while True:
    schedule.run_pending()
    time.sleep(1)

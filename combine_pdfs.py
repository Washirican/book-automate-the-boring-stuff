# !/usr/bin/env python3
"""
Combines all the PDFs in the current working directory into 
into a single PDF.
"""
import os
import PyPDF2
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

folder_path = 'C:\\Users\\tg715c\\Documents\\Reference Documents'  # Replace with the actual folder path

# Get all filenames in the folder
filenames = os.listdir(folder_path)

# Filter filenames to include only PDF files
pdf_files = [filename.lower() for filename in filenames if filename.endswith('.pdf') or filename.endswith('.PDF')]
pdf_files.sort()
logging.debug('Found %s total PDF files in folder.', len(pdf_files))

pdf_writer = PyPDF2.PdfFileWriter()
total_files_processed = 0
total_pages_processed = 0

# Loop through all the PDF files.
for file in pdf_files:
    pdf_file_obj = open(folder_path + '\\' + file , 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)

    # Only process unencrypted files.
    if pdf_reader.isEncrypted:
        # Skip if encrypted.
        logging.warning('File "%s" is encrypted and will not be processed.', file)
    else:
        # Process file.
        
        total_files_processed += 1
        logging.debug('Processing file: %s\\%s, with %s pages', folder_path, file, pdf_reader.numPages) 

        # Loop through all the pages (except the first) and add them.
        for page_num in range(1, pdf_reader.numPages):
            total_pages_processed += 1
            pdf_writer.addPage(pdf_reader.getPage(page_num))

# Save the resulting PDF to a file.
logging.debug('Processed %s total PDF files.', total_files_processed)
logging.debug('Writing results to file with %s total pages.', total_pages_processed)

result_pdf = open('automate_online-materials\\combine_select_pages.pdf', 'wb')
pdf_writer.write(result_pdf)
result_pdf.close()


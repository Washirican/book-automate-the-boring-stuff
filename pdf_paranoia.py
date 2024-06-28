# !/usr/bin/env python3
"""
Encrypt and Decrypt PDF all files in a folder.
"""

import os
import PyPDF2
import logging


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

logging.disable(logging.CRITICAL)

# Replace with the actual folder path
folder_path = 'C:\\Users\\tg715c\\Documents\\Python Scripts\\automate-stuff\\automate_online-materials\\CH 15 Project Test Files\\PDF Paranoia'

# Get all filenames in the folder
pdf_files = []
for root, dirs, files in os.walk(folder_path):
    for file in files:
        logging.debug('Found filename "%s"', file)

        if os.path.splitext(file)[1] == '.pdf':
            pdf_files.append(os.path.join(root, file))
            logging.debug('\tFile "%s" is a PDF. Adding to list...', file)

logging.debug('Found %s total files in folder.', len(pdf_files))

logging.debug('Found %s total PDF files in folder/subfolder.', len(pdf_files))

for file in pdf_files:
    logging.debug('Processing file: "%s"', os.path.basename(file))

    pdf_file_obj = open(file, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)

    # Encrypt files.
    if not pdf_reader.isEncrypted:
        pdf_writer = PyPDF2.PdfFileWriter()

        for page_num in range(pdf_reader.numPages):
            pdf_writer.addPage(pdf_reader.getPage(page_num))

        logging.debug('Encrypting file: "%s"', os.path.basename(file))

        pdf_writer.encrypt('password')
        filename = os.path.dirname(file) + '\\' + \
            f'{os.path.basename(file)}_encrypted.pdf'
        result_pdf = open(filename, 'wb')
        logging.debug('Saving file: "%s"', os.path.basename(file))
        pdf_writer.write(result_pdf)
        result_pdf.close()

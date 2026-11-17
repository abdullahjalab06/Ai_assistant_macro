import os
from pypdf import PdfReader
from docx import Document
from openpyxl import load_workbook


def extract_text_pdf(file_path):

    readerpdf = PdfReader(file_path)

    text = ""

    for page in readerpdf.pages:
        text += page.extract_text()

    return text

def extract_text_docx(file_path):
    readerdocx = Document(file_path)
    text = ""

    for paragraph in readerdocx.paragraphs:
        text += paragraph.text

    return text

def extract_text_excel(file_path):

    readerexcel = load_workbook(file_path)

    sheet = readerexcel.active

    text = ""

    for row in sheet.iter_rows(values_only=True):

        for cell in row:

            text += str(cell) + " "

    return text

def extract_text(file_path):

    extension = os.path.splitext(file_path)[1].lower()

    if extension == ".pdf":
        return extract_text_pdf(file_path)

    elif extension == ".docx":
        return extract_text_docx(file_path)

    elif extension == ".xlsx":
        return extract_text_excel(file_path)

    else:
        print("File type not supported")
        return None
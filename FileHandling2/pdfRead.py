import PyPDF2
from PyPDF2 import PdfReader

with open('py-pdf.pdf','rb') as file:
    pdf = PdfReader(file)
    print(pdf)
    pages = len(pdf.pages)

print("Number of pages:",pages)
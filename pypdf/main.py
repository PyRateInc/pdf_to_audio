from gtts import gTTS
import os
from PyPDF2 import PdfFileReader

def extract_information(pdf_path):
    with open(pdf_path, 'rb') as f:
        pdf = PdfFileReader(f)
        information = pdf.getDocumentInfo()
        number_of_pages = pdf.getNumPages()

    txt = f"""
    Information about {pdf_path}: 

    Author: {information.author}
    Creator: {information.creator}
    Producer: {information.producer}
    Subject: {information.subject}
    Title: {information.title}
    Number of pages: {number_of_pages}
    """
    tts = gTTS(text=txt, lang='ru')
    tts.save("book.mp3")
    os.system("book good.mp3")

    print(txt)
    return information

if __name__ == '__main__':
    path = "01OPistoleiroStephenKing.pdf"
    extract_information(path)
    
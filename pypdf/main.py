#!/usr/bin/env python3
# -*- coding: UTF-8-*-

import os
from gtts import gTTS
from PyPDF4 import PdfFileReader

''' Feito por: Dimitri(Taikamya) e Pablo III(Nemo) '''
_authors = ["Dimitri", "Pablo III"]
"""
    Nota dos autores:
    Como a ideia é lançar o mais rápido possível, criei uma função que lê em inglês, e outra em português. Com o tempo, otimizamos.
"""

def extract_information_en(pdf_path):
    ''' Extract info, play and save to file. Language is set to "en"(English). '''
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
    tts = gTTS(text=txt, lang='en')
    tts.save("book_en.mp3")

    print(txt)
    return information

def extract_information_pt_br(pdf_path):
    ''' Extract info, play and save to file. Language is set to "pt-br"(Brazilian Portuguese). '''
    with open(pdf_path, 'rb') as f:
        pdf = PdfFileReader(f)
        information = pdf.getDocumentInfo()
        number_of_pages = pdf.getNumPages()

    txt = f"""
    Informação sobre {pdf_path}: 

    Autor: {information.author}
    Criador: {information.creator}
    Produtor: {information.producer}
    Assunto: {information.subject}
    Título: {information.title}
    Número de páginas: {number_of_pages}
    """
    tts = gTTS(text=txt, lang='pt-br')
    tts.save("book_pt_br.mp3")

    print(txt)
    return information


if __name__ == '__main__':
    path = "01OPistoleiroStephenKing.pdf"
    extract_information_en(path)
    extract_information_pt_br(path)
    
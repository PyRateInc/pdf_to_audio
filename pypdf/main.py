#!/usr/bin/env python3
# -*- coding: UTF-8-*-

''' Feito por: Dimitri(Taikamya) e Pablo III(Nemo) '''
_authors = ["Dimitri", "Pablo III"]

import pyttsx3
import PyPDF4
import tkinter as tk
from tkinter.filedialog import *


class App(tk.Frame):
    ''' Cria e mantém uma janela para melhor manuseio, debug e operações comandadas ao invés
        de simplesmente aparecer o prompt para escolha do arquivo sem mais nem menos '''
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        # Estabelece um título
        self.master.title("PDF Reader")
        # Estabelece o tamanho MIN da janela principal
        self.master.minsize(260, 120)
        # Estabelece o tamanho MAX da janela principal
        self.master.maxsize(640, 360)
        # Inicia o player com o pyttsx
        self.player = pyttsx3.init()

    def create_widgets(self):
        # Cria um botão "Choose file..." com comando da função "askopenfilename"
        self.open = tk.Button(self, text="Choose file...", command=self.reading)
        # self.open["command"] = self.reading
        self.open.pack(side="top")

        # Cria um botão "Quit" com comando da função de fechar a janela principal
        self.quit = tk.Button(self, text="Quit", fg="yellow", bg="black", command=self.close_window)
        self.quit.pack(side="bottom")

    def save_state(self):
        pass

    """ def get_propery(self):
        Pode se colocar as defs rate e a volume aqui e deixá-las como parametros """

    def rate(self):
        """ Função que determina quantas palavras por minuto, por padrão é 200 palavras por minuto """
        # Obtem detalhes da taxa atual de fala
        rate = engine.getProperty('rate')
        print (rate)
        engine.setProperty('rate', 100)

    def volume(self):
        # Reconhece o nível de volume atual (min = 0 e max = 1)
        volume = self.player.getProperty('volume')
        print (volume)
        # Configura o nível do volume entre 0 e 1
        self.player.setProperty('volume',1.0)

    def close_window(self):
        """ Função pra fechar a janela principal (parent) e qualquer dependente (children). """
        Tk.destroy(root)

    def reading(self):
        # Colocar um "Try/Except/Else/Finally" aqui, pq se você abre a janela e cancela a operação
        # O programa não fecha, mas dá erro e não deixa você selecionar depois.
        # Esse "askopenfilename" é muito bugado
        book = askopenfilename()
        pdfreader = PyPDF4.PdfFileReader(book)
        pages = pdfreader.numPages

        for num in range(0, pages):
            page = pdfreader.getPage(num)
            text = page.extractText()
            self.player.say(text)
            self.player.runAndWait()


if __name__ == "__main__":
    root = tk.Tk()
    myapp = App(master=root)
    myapp.mainloop()

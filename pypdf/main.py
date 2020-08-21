#!/usr/bin/env python3
# -*- coding: UTF-8-*-

''' Feito por: Dimitri(Taikamya) e Pablo III(Nemo) '''
_authors = ["Dimitri", "Pablo III"]

import pyttsx3
import PyPDF4
from tkinter import *
from tkinter.filedialog import *


class App(Frame):
    ''' Cria e mantém uma janela para melhor manuseio, debug e operações comandadas ao invés
        de simplesmente aparecer o prompt para escolha do arquivo sem mais nem menos '''
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        # self.pack()
        self.create_widgets()
        # Estabelece um título
        root.title("PDF Reader")
        # Mantém fixo o tamnho da janela
        root.geometry('{}x{}'.format(360, 240))
        root.resizable(width=False, height=False)
        engine.isBusy = False

    def create_widgets(self):
        # Cria uma tela inicial
        self.open_frame = Frame(root)
        self.open_frame.pack(side="top")

        # Cria um botão "Choose file..." com comando da função "extract_txt"
        self.open_btn = Button(self.open_frame, text="Choose file...", command=self.extract_txt, fg="red", padx=10, pady=10)
        self.open_btn.grid(row=0, column=0)
        # Cria um botão "Quit" com comando da função "close_window"
        self.quit_btn = Button(self.open_frame, text="Quit", command=self.close_window, fg="yellow", bg="black", padx=10, pady=10)
        self.quit_btn.grid(row=1, column=0)

        # Cria outra tela
        # self.play_frame = Frame(root)
        # self.play_frame.pack(side="top")

        # Cria um botão "Play" com comando da função "read_txt"
        self.play_btn = Button(self.open_frame, text="Play", command=self.read_txt, fg="red", padx=10, pady=10)
        self.play_btn.grid(row=0, column=1)

        # Cria um botão "Stop" com comando da função de parar a leitura
        self.stop_btn = Button(self.open_frame, text="Stop", command=self.stop_func, fg="yellow", bg="black", padx=10, pady=10)
        self.stop_btn.grid(row=1, column=1)

    # def save_state(self):
    #     pass

    # """ def get_propery(self):
    #     Pode se colocar as defs rate e a volume aqui e deixá-las como parametros """

    def rate(self):
        """ Função que determina quantas palavras por minuto, por padrão é 200 palavras por minuto """
        # Obtém detalhes da taxa atual de fala
        rate = engine.getProperty('rate')
        print (rate)
        engine.setProperty('rate', 100)

    def volume(self):
        # Reconhece o nível de volume atual (min = 0 e max = 1)
        volume = engine.getProperty('volume')
        print (volume)
        # Configura o nível do volume entre 0 e 1
        engine.setProperty('volume', 1.0)

    def close_window(self):
        """ Função pra fechar a janela principal (parent) e qualquer dependente (children). """
        print("Window destroyed.")
        root.destroy()

    def extract_txt(self):
        # RESOLVIDO
        # RESOLVIDO
        # RESOLVIDO
        book = askopenfile(parent=root, mode="rb", title="Choose a PDF file")
        if book != None:
            pdfReader = PyPDF4.PdfFileReader(book)
            global pdfTxt
            pdfTxt = ""
            for num in range(pdfReader.numPages):
                page = pdfReader.getPage(num)
                pdfTxt += page.extractText()
            book.close()
        if pdfReader != None:
            # Propósito para debug: Ver se o objeto é alocado em memória
            print(f"Objeto está em {pdfReader}.")
            print("File is ready.")
        else:
            # Propósito para debug: Ver se o objeto NÃO é alocado em memória
            print(f"Objeto {pdfReader}NÃO está em memória.")
            print("Operation canceled.")

    def read_txt(self):
        # Problema! Ainda não consegui fazer parar a leitura, apesar de que a "stop_func" funciona!
        print("Checking, please wait...")
        engine.isBusy = True
        if engine.isBusy == True:
            engine.say(pdfTxt)
             # engine.runAndWait()
            print("Reading has started.")
        else:
            print("File is not loaded")

    def stop_func(self):
        print("Trying to stop it. Please wait...")
        if engine.isBusy == True:
            engine.stop()
            print("Reading stopped.")
            engine.isBusy = False
        else:
            print("Reading was NOT running.")


if __name__ == "__main__":
    pdfTxt = ""  # Variável global
    engine = pyttsx3.init()
    root = Tk()
    myapp = App(master=root)
    myapp.mainloop()

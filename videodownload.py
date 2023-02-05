from tkinter.filedialog import askopenfilename
from tkinter import *
from pytube import YouTube
import glob
from moviepy.editor import*
import os
from tkinter import filedialog
import glob
from tkinter import messagebox
#import testeConversor

class Aplicacao:
    def __init__(self, master):
        self.frame1 = Frame(master)
        self.frame1.place(x=10, y=10, width=321, height=500)
        self.frame1.config(background="black")
        
        self.texto_link = Label(self.frame1)
        self.texto_link["text"] = "Insira o link"
        self.texto_link.place(x=0, y=10)
        self.texto_link.config(background="black", foreground="white")
               
        self.ent_link= Entry(self.frame1)
        self.ent_link["width"] = 90
        self.ent_link.place(x=0, y=40)
        
        self.texto_pasta = Label(self.frame1)
        self.texto_pasta["text"] = "Insira o link"
        self.texto_pasta.place(x=0, y=10)
        self.texto_pasta.config(background="black", foreground="white")
        
        self.botao_baixar = Button(self.frame1)
        self.botao_baixar["text"] = "Baixar"
        self.botao_baixar["command"] = self.executar_download
        self.botao_baixar["bd"] = 3
        self.botao_baixar["font"] = ("Arial", 10)
        self.botao_baixar.place(x=270, y=65)
        
        
        self.botao_pasta = Button(self.frame1)
        self.botao_pasta["text"] = "Pasta"
        self.botao_pasta["command"] = self.browse_button
        self.botao_pasta["bd"] = 3
        self.botao_pasta["font"] = ("Arial", 10)
        self.botao_pasta.place(x=0, y=65)
        
        self.frame2 = Frame(master)
        self.frame2.place(x=10, y=110, width=321, height=190)
        self.frame2.config(background="black")
        
        
        self.sby = Scrollbar(self.frame2)
        self.sby.pack(side=RIGHT, fill=Y)
        
        self.sbx = Scrollbar(self.frame2, orient=HORIZONTAL)
        self.sbx.pack(side=BOTTOM, fill=X)
        
        self.lista_arquivos = Listbox(self.frame2, width=50, height=11, selectmode=EXTENDED)
        self.lista_arquivos.place(x=0, y=0)
        
        self.lista_arquivos.config(yscrollcommand=self.sby.set)
        self.sby.config(command=self.lista_arquivos.yview)
        self.lista_arquivos.config(xscrollcommand=self.sbx.set)
        self.sbx.config(command=self.lista_arquivos.xview)
        
        self.frame3 = Frame(master)
        self.frame3.place(x=10, y=300, width=323, height=190)
        self.frame3.config(background="black")
        
        self.botao_adicionar = Button(self.frame3)
        self.botao_adicionar["text"] = "Selecionar Arquivo"
        self.botao_adicionar["command"] = self.adicionar
        self.botao_adicionar["bd"] = 3
        self.botao_adicionar["font"] = ("Arial", 10)
        self.botao_adicionar.place(x=0, y=10)
        
        self.botao_extrair = Button(self.frame3)
        self.botao_extrair["text"] = "Converter"
        self.botao_extrair["command"] = self.extrair_audio
        self.botao_extrair["bd"] = 3
        self.botao_extrair["font"] = ("Arial", 10)
        self.botao_extrair.place(x=230, y=10)
        
        
    def browse_button(self):
        filename = filedialog.askdirectory()
           
    def adicionar(self):
        nome_arquivo = askopenfilename()
        if nome_arquivo != "":
            self.lista_arquivos.insert(END, nome_arquivo)    
        
        

    def executar_download(self):
        
        local = self.botao_pasta
        video = YouTube(self.ent_link.get())
        yt = video.streams.filter(progressive=True, file_extension='mp4').order_by("resolution").desc().first().download()
    
    def extrair_audio(self):
        def os_detect() :
                if os.name == 'nt':
                    print('\nSaved Location:\n')
                    os.system('cd')
                else :
                    print('\nSaved Location:\n')
                    os.system('pwd')
    

        def video2audio(self,videofile,audiofile):
                    videoclip=VideoFileClip(self.lista_arquivos.curselection())
                    audioclip=videoclip.audio
                    audioclip.write_audiofile(audiofile)
                    audioclip.close()
                    videoclip.close()

        mp4file = askopenfilename()
        mp3file =  self.ent_link.get()

        video2audio(mp4file, mp3file)

        os_detect() 
       
            
            
            
            #itens = glob.glob('*.mp4')

            #for video in itens: 
            #item_pos = int(itens)
            #mp4 = VideoFileClip(os.path.join(itens))
            #nome_mp3 = itens[:-4]+'.mp3'
            #mp4.audio.write_audiofile(os.path.join(nome_mp3))  
            
janela = Tk()
janela.geometry("400x800")
janela.config(background="black")
janela.resizable(width=False, height=False)

Aplicacao(janela)
janela.mainloop()
            
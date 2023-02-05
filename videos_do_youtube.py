import PySimpleGUI as sg
from pytube import YouTube
import glob
from moviepy.editor import*
import os
from moviepy.video.fx.accel_decel import accel_decel
from moviepy.video.fx.blackwhite import blackwhite
from moviepy.video.fx.blink import blink
from moviepy.video.fx.crop import crop
from moviepy.video.fx.even_size import even_size
from moviepy.video.fx.fadein import fadein
from moviepy.video.fx.fadeout import fadeout
from moviepy.video.fx.mirror_x import mirror_x
from moviepy.video.fx.mirror_y import mirror_y
from moviepy.video.fx.resize import resize
from moviepy.audio.fx.audio_fadein import audio_fadein
from moviepy.audio.fx.audio_fadeout import audio_fadeout
from moviepy.audio.fx.audio_left_right import audio_left_right
from moviepy.audio.fx.audio_loop import audio_loop
from moviepy.audio.fx.audio_normalize import audio_normalize
from moviepy.audio.fx.volumex import volumex
from moviepy.video.fx.accel_decel import accel_decel
from moviepy.video.fx.blackwhite import blackwhite
from moviepy.video.fx.blink import blink
from moviepy.video.fx.colorx import colorx
from moviepy.video.fx.crop import crop
from moviepy.video.fx.even_size import even_size
from moviepy.video.fx.fadein import fadein
from moviepy.video.fx.fadeout import fadeout
from moviepy.video.fx.freeze import freeze
from moviepy.video.fx.freeze_region import freeze_region
from moviepy.video.fx.gamma_corr import gamma_corr
from moviepy.video.fx.headblur import headblur
from moviepy.video.fx.invert_colors import invert_colors
from moviepy.video.fx.loop import loop
from moviepy.video.fx.lum_contrast import lum_contrast
from moviepy.video.fx.make_loopable import make_loopable
from moviepy.video.fx.margin import margin
from moviepy.video.fx.mask_and import mask_and
from moviepy.video.fx.mask_color import mask_color
from moviepy.video.fx.mask_or import mask_or
from moviepy.video.fx.mirror_x import mirror_x
from moviepy.video.fx.mirror_y import mirror_y
from moviepy.video.fx.painting import painting
from moviepy.video.fx.resize import resize
from moviepy.video.fx.rotate import rotate
from moviepy.video.fx.scroll import scroll
from moviepy.video.fx.speedx import speedx
from moviepy.video.fx.supersample import supersample
from moviepy.video.fx.time_mirror import time_mirror
from moviepy.video.fx.time_symmetrize import time_symmetrize
from tkinter.filedialog import askopenfilename



def Extrair_audio(video):
    lista_mp4 = glob.glob('*.mp4')

    for video in lista_mp4: 
        mp4 = VideoFileClip(os.path.join(video))
        nome_mp3 = video[:-4]+'.mp3'
        mp4.audio.write_audiofile(os.path.join(nome_mp3))
        

def remover_videos(files):
    files = glob.glob('*.mp4')

    for file in files:
        print(file)
        os.unlink(file)

            

def executar_download(link, path):
        video = YouTube(link)
        video.streams.get_highest_resolution().download(output_path=path)

sg.theme("black")


aviso = [[sg.popup("Recomendo baixar todos os videos e depois converter todos de uma única vez!")]]

layout = [[sg.Text("Insira o Link: "), sg.InputText()],
          [sg.Text("Informe a Pasta "), sg.InputText(), sg.FolderBrowse()],
          [sg.Text("Caso não informe a pasta, o arquivo será baixado na pasta atual do programa.")],
          [sg.Button("Baixar"),sg.Button("Cancelar"),sg.Button("Converter Videos")],
          [sg.Text("Após converter os videos clique em excluir os videos originais.")],
          [sg.Button("Excluir videos originais")],
          [sg.Text("\nRDN Softwares")]
          
         ]

janela = sg.Window("RDN Softwares", layout)

while True:
    event, values = janela.read()
    if event == "Cancelar" or event == sg.WIN_CLOSED:
        break
    elif event =="Baixar":
        executar_download(values[0], values[1])
        sg.popup_ok("Download Concluido com sucesso!")
    elif event == "Converter Videos":
        Extrair_audio(values[0])   
        sg.popup_ok("Videos convertidos com sucesso!")
    elif event == "Excluir videos originais":        
        remover_videos(values[0])
        sg.popup_ok("Videos Excluídos com sucesso!")
        


janela.close()    


from reproductor import Reproductor
from tkinter import *


musica = Reproductor("MERCEDES CAROTA.mp3")
resp = ""
def play_musica():
    resp = musica.play()

master = Tk()
master.geometry("200x200")
master.title("Reproductor de Windows")

etiqueta = Label(master,text = "DJ")
etiqueta.pack(pady = 5)

btn_play = Button(master, text="Play", command=play_musica)
btn_play.pack(pady = 10)

mainloop()


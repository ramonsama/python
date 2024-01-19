from pygame import mixer
class Reproductor: 
    #atributos
    archivo = None

    #Constructor
    def __init__(self, archivo):
        self.archivo = archivo
        mixer.init()
        mixer.music.load(archivo)

    def play(self):
        mixer.music.play()
        return "Reproduciendo música"
    
    def pause(self):
        mixer.music.pause()
        return "La música se ha pausado"

    def stop(self):
        mixer.music.stop()
        return "La música se detuvo"
    
    def unpause(self):
        mixer.music.unpause()
        return "♪"

    def volume(self, v):
        mixer.music.set_volume(v)
        return "Volumen a",(100*v), "%"

if __name__ == "__main__":
    file = "MERCEDES CAROTA.mp3"
    musica = Reproductor(file)
    while True:
        print("1- PLAY | 2- PAUSE | 3- STOP | 4-VOL")
        accion = int(input("Opción: "))
        if(accion == 1):
            resp = musica.play()
        if(accion == 2):
            resp = musica.pause()
        if(accion == 3):
            resp = musica.unpause()
        if(accion == 4):
            vol = float(input("Volumen :"))
            resp = musica.volume(vol)
        elif(accion == 5):
            vol = float(input("Volumen 0 -- 100 "))
            if(vol >=0 and vol <= 100):
                vol /= 100
                resp = musica.volume(vol)
        
        print(resp)

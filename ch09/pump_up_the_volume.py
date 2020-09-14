from tkinter import *
import pygame.mixer

mixer = pygame.mixer
mixer.init()

track = mixer.Sound("50459_M_RED_Nephlimizer.wav")

def change_volume(resolution):
    track.set_volume(volume.get())
    
app = Tk()
app.title("Pump up the volume!")
app.geometry('350x100+100+100')

volume = DoubleVar()
volume_scale = Scale(app,variable = volume, from_ = 0.0, to = 1.0, resolution = 0.1,
                     command = change_volume, label = "Volume", orient = HORIZONTAL)
volume_scale.pack(side = RIGHT)

track.play(loops = -1)

app.mainloop()

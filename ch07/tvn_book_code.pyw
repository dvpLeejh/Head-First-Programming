from tkinter import *
import pygame.mixer

def play_correct_sound():
    num_correct.set(num_correct.get()+1)
    correct_s.play()

def play_wrong_sound():
    num_wrong.set(num_wrong.get()+1)
    wrong_s.play()

app = Tk()
app.title("TVN Game Show")
app.geometry('300x100+200+100')

sounds = pygame.mixer
sounds.init()

correct_s = sounds.Sound("correct.wav")
wrong_s = sounds.Sound("wrong.wav")

num_correct = IntVar()
num_correct.set(0)

num_wrong = IntVar()
num_wrong.set(0)

l = Label(app, text = 'When you are ready, Click on the buttons!', height = 3)
l.pack()

lab1 = Label(app, textvariable = num_correct)
lab1.pack(side='left')

lab2 = Label(app, textvariable = num_wrong)
lab2.pack(side='right')

b1 = Button(app, text = "Correct!", width = 10, command = play_correct_sound)
b1.pack(side = 'left', padx = 10, pady = 10)

b2 = Button(app, text = "Wrong!", width = 10, command = play_wrong_sound)
b2.pack(side = 'right', padx = 10, pady = 10)


app.mainloop()

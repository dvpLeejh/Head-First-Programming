from tkinter import *
import pygame.mixer


sounds = pygame.mixer
sounds.init()

number_correct = 0
number_wrong = 0

def Correct():
    global number_correct
    global num_correct
    num_correct.set(number_correct)
    number_correct += 1
    correct_s = sounds.Sound("correct.wav")
    correct_s.play()

def Wrong():
    global number_wrong
    global num_wrong
    num_wrong.set(number_wrong)
    number_wrong += 1
    wrong_s = sounds.Sound("wrong.wav")
    wrong_s.play()

app = Tk()
app.title("TVN Game Show")
app.geometry('300x100+200+100')

num_correct = IntVar()
num_correct.set(0)

num_wrong = IntVar()
num_wrong.set(0)

l = Label(app, text = 'When you are ready, Click on the buttons!', height = 3)
l.pack()

l2 = Label(app, textvariable = num_correct)
l2.pack(side='left')

l3 = Label(app, textvariable = num_wrong)
l3.pack(side='right')

b1 = Button(app, text = "Correct!", width = 10, command = Correct)
b1.pack(side = 'left', padx = 10, pady = 10)

b2 = Button(app, text = "Wrong!", width = 10, command = Wrong)
b2.pack(side = 'right', padx = 10, pady = 10)


app.mainloop()

print("%d %d" % (number_correct, number_wrong))

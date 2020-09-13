import pygame.mixer

def wait_finish(channel):
    while channel.get_busy():
        pass
    
sounds = pygame.mixer
sounds.init()

number_asked = 0
number_correct = 0
number_wrong = 0

while True:
    g=(int(input("press the number: ")))
    if g == 1:
        number_asked += 1
        number_correct += 1
        s = sounds.Sound("correct.wav")
        wait_finish(s.play())
        
    elif g == 2:
        number_asked += 1
        number_wrong += 1
        s2 = sounds.Sound("wrong.wav")
        wait_finish(s2.play())
    else:
        break

print("%d %d %d" % (number_asked, number_correct, number_wrong))

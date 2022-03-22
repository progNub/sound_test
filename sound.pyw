
from tkinter import *
from pygame import mixer
import random

mixer.init()
root = Tk()             
root.title("Dominator 3000")                    
root.geometry("400x400")                         

class Propert(object):
    temp_song = 0

    def __init__(self) -> None:
        super().__init__()

    def get_song(self):
        return Propert.temp_song

    def set_song(self,temp):
        Propert.temp_song = temp
        
mainframe = Frame(root, bg = "lightblue")
mainframe.pack(expand = True, fill = BOTH)

proper = Propert()

def random_sound(temp = 0, access = 0):
    if access == 0:
        while True:
            song = random.randrange(1,4)
            if song != temp:
                break
    else: 
        song = temp
    proper.set_song(song)
    if song == 1:
        mixer.music.load("TON_C.mp3")
        mixer.music.play()
    elif song == 2:
        mixer.music.load("DOM_C.mp3")
        mixer.music.play()
    elif song == 3:
        mixer.music.load("subDOM_C.mp3")
        mixer.music.play()

top = Frame(mainframe, bg = "lightblue")
top.pack(pady = 20)
p = 10
run = Button(top, width = 15, text= "Играть", command = lambda: (random_sound(proper.get_song())))
run.grid(row = 0, column=0, padx = p)

repeat = Button(top,width = 15, text= "Повторить аккорд", command = lambda: (random_sound(proper.get_song(), access= 1)) )
repeat .grid(row = 0,column=1,padx = p)

close = Button(top,width = 15, text= "Закрыть",command = exit)
close.grid(row = 0,column=2,padx = p)

def update_text(temp):
    if str(proper.get_song()) == temp:
        text.delete(1.0, END)
        text.insert(1.0, "Верно")
    elif temp != "":
        error = "Тональность"
        

        text.delete(1.0, END)
        text.insert(1.0, "Ошибка это " + error)

def play_sound(temp):
    if temp == "ton":
        mixer.music.load("TON_C.mp3")
        mixer.music.play()
    elif temp == "dom":
        mixer.music.load("DOM_C.mp3")
        mixer.music.play()
    elif temp == "sub":
        mixer.music.load("subDOM_C.mp3")
        mixer.music.play()

def update_songs(temp):
    update_text("")
    if temp == "0":
        ton["bg"] = "silver"
        dom["bg"] = "silver"
        sub["bg"] = "silver"
        ton["command"] = lambda: (update_text("1"))
        dom["command"] = lambda: (update_text("2"))
        sub["command"] = lambda: (update_text("3"))
    else:
        update_text("")
        ton["bg"] = "white"
        dom["bg"] =  "white"
        sub["bg"] =  "white"
        ton["command"] = lambda: (play_sound("ton"))
        dom["command"] = lambda: (play_sound("dom"))
        sub["command"] = lambda: (play_sound("sub"))

frame = Frame(mainframe, bg = "lightblue",highlightthickness=1, highlightbackground= "black")
frame.pack(side=TOP)

favorit = StringVar()               
favorit.set(0)          
Radiobutton(frame, width = 15, justify= LEFT,  bg="silver", text = "Отвечать", 
variable = favorit, value = "0",command=lambda: (update_songs(favorit.get()))).grid(sticky=W,row = 2, column = 0) 
Radiobutton(frame, width = 15, justify= LEFT, bg="white", text = "Прослушивать", 
variable = favorit, value = "1",command=lambda: (update_songs(favorit.get()))).grid(sticky=W, row = 3, column = 0) 


frame1 = Frame(mainframe, border=2, pady = 20, bg = "lightblue")
frame1.pack(side=TOP)
butx = 9
buty = 3
message = StringVar()
ton = Button(frame1, width = 12, bg="silver", text= "Тоника", padx = butx, pady = buty)
dom = Button(frame1,width = 12, bg="silver", text= "Доминанта", padx = butx, pady = buty)
sub = Button(frame1,width = 12,  bg="silver",text= "Суб-Доминанта", padx = butx, pady = buty)
px = 5
ton.grid(row = 1, column = 1, padx = px)
dom.grid(row = 1, column = 2, padx = px)
sub.grid(row = 1, column = 3, padx = px)

frame2 = Frame(mainframe, bg = "lightblue")
frame2.pack(side=TOP)


text = Text(frame2, height = 10, width = 40)
text.grid(pady = 20)

update_songs("0")

root.mainloop()




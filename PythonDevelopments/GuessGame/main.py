import random
from customtkinter import *
from CTkMessagebox import CTkMessagebox

root =CTk()
root.title("Guess Game")
root.geometry("350x250")
root.resizable(0,0)
root.config(bg="black")

global n
n = random.randrange(0,5)
global a
a=1


def entrylab(a,n):
    CTkButton(frame2,text="Play",command=lambda:game(a,n),bg_color="black").grid(row=50,column=0,columnspan=2,pady=10)

def game(a,n):
    try:
        guess= int(entry.get())
        if (guess > 5):
            CTkMessagebox(width=200,height=100,title="Input Error", message="Please, enter no from 0-5",icon="warning")
        elif (guess <0):
            CTkMessagebox(width=200,height=100,title="Input Error", message="Please, enter no from 0-5",icon="warning") 
        else:
            if (guess == n):
                CTkMessagebox(width=200,height=100,title="Win", message="Congratulations, you did it in attempt "+str(a),icon="check")
                a= 1
                entrylab(a,n)
            elif (guess > n):
                CTkMessagebox(width=200,height=100,title="Info", message="Oops, you went higher than real guess in attempt "+str(a),icon="info")
                a = a+1
                entrylab(a,n)
            elif (guess < n):
                CTkMessagebox(width=200,height=100,title="Info", message="Oops, you went lower than real guess in attempt "+str(a),icon="info")
                a = a+1
                entrylab(a,n)
    except ValueError:
        CTkMessagebox(width=200,height=100,title="Data error", message="Please enter no from 0-5",icon="warning")
    return

CTkLabel(root,text="Guess Game",text_color="white",bg_color="black",fg_color="black",font=("Goudy Old Style", 40,"bold")).pack(pady=10)
frame1 = CTkFrame(root,bg_color="black",fg_color="black")
frame1.pack(pady=20)
frame2 = CTkFrame(root,bg_color="black",fg_color="black")
frame2.pack(pady=20)
CTkLabel(frame1,text="Enter guess from 0-5: ",text_color="white",bg_color="black",fg_color="black",font=("Goudy Old Style", 20, "bold")).grid(row=0,column=0)
entry = CTkEntry(frame1,width=50,text_color="black",bg_color="black",border_color="black",fg_color="white")
entry.grid(row=0,column=1)

entrylab(a,n)
root.mainloop()
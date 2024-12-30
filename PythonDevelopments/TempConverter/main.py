from customtkinter import *
from CTkMessagebox import CTkMessagebox

root = CTk()
root.title("Temperature~Converter")
root.config(bg="black")
root.geometry("300x250")
root.resizable(0,0)
C = 0
F = 0
K = 0

def output(C,F,K):
        
        win = CTkToplevel(root)
        win.grab_set()
        win.geometry("230x225")
        win.resizable(0,0)
        win.config(bg="black")
        win.title("Output")

        def end():
             win.destroy()
             win.update()
             entry.delete(0,END)
        
        CTkLabel(win, text="Celcius: "+str(C),width=100,fg_color="white",text_color="black").pack(pady=10)
        CTkLabel(win, text="Farenheit: "+str(F),width=100,fg_color="white",text_color="black").pack(pady=10)
        CTkLabel(win, text="Kelvin: "+str(K),width=100,fg_color="white",text_color="black").pack(pady=10)
        CTkButton(win, text="Close",command=end).pack(pady=20)



def operation():
    try:
        unit = optionmenu.get()
        value = float(entry.get())
        if (unit==" °C"):
            C = value
            F = (C * 9/5)+32
            K = C+273.15
            output(C,F,K)
        elif (unit==" °F"):
            F = value
            C = (F-32)*5/9
            K = ((F-32)*5/9)+273.15
            output(C,F,K)
        elif (unit==" °K"):
            K = value
            C = K-273.15
            F = ((K-273.15)*9/5)+32
            output(C,F,K)
    except ValueError:
        CTkMessagebox(width=200,height=100,title="Data error", message="Please enter valid data")

def main():
    frame = CTkFrame(root)
    frame.pack(pady=30)
    global entry
    entry = CTkEntry(frame, 
                    placeholder_text="0",
                    placeholder_text_color="black", 
                    border_color="black",
                    height=30,
                    width=150, 
                    corner_radius=0,
                    fg_color="white", 
                    text_color="black", 
                    font=("Goudy Old Style", 20, "bold"))
    entry.grid(row=0, column=0)
    global optionmenu
    optionmenu = CTkOptionMenu(frame,
                            fg_color="white",
                            text_color="black",
                            height=25,
                            width=60,
                            corner_radius=0,
                            button_color="red",
                            dropdown_fg_color="white",
                            dropdown_text_color="black",
                            values=[" °C", " °F", " °K"],
                            font=("Goudy Old Style", 20, "bold"))
    optionmenu.grid(row=0,column=1)

    convert = CTkButton(root, 
                        text="Convert", 
                        hover=False, 
                        text_color="white", 
                        bg_color="black", 
                        font=("Goudy Old Style", 20, "bold"),
                        command=operation)
    convert.pack(pady=50)

main()

root.mainloop()
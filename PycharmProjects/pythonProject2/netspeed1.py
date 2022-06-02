import tkinter as tk
import speedtest

def st1():
    s = speedtest.Speedtest()
    s.get_servers()
    down = str(round(s.download()/(10**6),3))+"Mbps"
    print("your download speed is", down)
    down_button.config(text="⏬- " + down)

def st2():
    s = speedtest.Speedtest()
    s.get_servers()
    up = str(round(s.upload() / (10**6), 3)) + "Mbps"
    print("your upload speed is", up)
    upload_button.config(text="⏫- " + up)

var=tk.Tk()
var.title("Speed-Test")
var.geometry('500x500')
var.config(background="pink", borderwidth=100, border=1)

lab = tk.Label(var, text="Internet Speed Test", font=("Arial", 15, "bold","underline"),bg="pink")
lab.place(x=150,y=100)
#lab.pack()
upload_button = tk.Button(var, text="Upload Speed", font=("Arial", 15, "bold"), relief="raised", cursor="plus",
command=st2)
upload_button.place(x=150, y=175, height=50, width=200)

down_button = tk.Button(var, text="Download Speed", font=("Arial", 15, "bold"), relief="raised", cursor="plus",
command=st1)
down_button.place(x=150, y=250, height=50, width=200)

var.mainloop()

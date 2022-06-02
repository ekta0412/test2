import tkinter as tk
import speedtest

def st():
    s = speedtest.Speedtest()
    s.get_servers()
    down = str(round(s.download()/(10**6),3))+"Mbps"
    print("your download speed is", down)
    up = str(round(s.upload() / (10**6), 3)) + "Mbps"
    print("your upload speed is", up)
    result_lab1.config(text="* " + up )
    result_lab2.config(text="* " + down)

var=tk.Tk()
var.title("Speed-Test")
var.geometry('500x500')
var.config(background="pink", borderwidth=100, border=1)

lab = tk.Label(var, text="Internet Speed Test", font=("Arial", 15, "bold","underline"),bg="pink")
lab.place(x=150,y=50)
#lab.pack()
upload_lab = tk.Label(var, text="Upload Speed", font=("Arial", 15, "bold"), relief="raised")
upload_lab.place(x=150, y=100, height=30, width=200)

result_lab1=tk.Label(var, text="00", font=("Arial", 15, "bold"), relief="raised")
result_lab1.place(x=50, y=150, height=40, width=400)

down_lab = tk.Label(var, text="Download Speed", font=("Arial", 15, "bold"), relief="raised")
down_lab.place(x=150, y=200, height=30, width=200)

result_lab2=tk.Label(var, text="00", font=("Arial", 15, "bold"), relief="raised")
result_lab2.place(x=50, y=250, height=40, width=400)

check = tk.Button(var,text="CLICK here!", font=("Arial", 15, "bold"), relief="raised", command=st,bg="green")
check.place(x=150, y=350, height=30, width=200)

var.mainloop()

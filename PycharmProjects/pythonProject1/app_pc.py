import tkinter as tk
import os

def restart():
    os.system("shutdown /r /t /1")

def restart_t():
    os.system("shutdown /r /t /20")

def logout():
    os.system("shutdown -1")

def shutdown():
    os.system("shutdown /s /t /1")

sh= tk.Tk ()
sh.title("App Guru")
sh.geometry('500x500')
sh.config(bg="yellow")

restart_button= tk.Button(sh,text="Restart",font= ("Arial", 30,"bold"),relief="raised",cursor="plus",command=restart)
restart_button.place(x=150,y=70,height=50,width=200)

restartw_button= tk.Button(sh,text="Restart_t",font= ("Arial", 30,"bold"),relief="raised",cursor="plus",command=restart_t)
restartw_button.place(x=150,y=150,height=50,width=200)

logout_button= tk.Button(sh,text="Logout",font= ("Arial", 30,"bold"),relief="raised",cursor="plus",command=logout)
logout_button.place(x=150,y=230,height=50,width=200)

shutdown_button= tk.Button(sh,text="Shutdown",font= ("Arial", 30,"bold"),relief="raised",cursor="plus",command=shutdown)
shutdown_button.place(x=150,y=310,height=50,width=200)

sh.mainloop()



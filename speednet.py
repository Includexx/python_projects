from tkinter import *
import speedtest

def  speedcheck() :
  sp = speedtest.Speedtest()
  sp.get_servers()
  down =str(round( sp.download()/(10**6),3))+" Mbps"
  Up = str(round(sp.upload()/(10**6),3))+ " Mbps"
  lab_down.config(text= down)
  lab_up.config(text= Up)






sp = Tk()
sp.title("INTERNET SPEED ")
sp.geometry("500x700")
sp.config(bg="green")
lab = Label(sp,text ="INTERNET SPEED",font = ("time new roman",32,"bold"),bg="green",fg="black")
lab.place(x=50,y=30,height=50,width=400)
lab= Label(sp,text="DOWNLOAD SPEED",font=("time new roman",30,"bold"),bg="white",fg="black")
lab.place(x=50,y=120,height=50,width=400)
lab_down = Label(sp,text="00",font=("time new roman",30,"bold"),bg="green",fg="white")
lab_down.place(x=50,y=190,height=50,width=400)
lab = Label(sp,text="UPLOAD SPEED",font=("time new roman",30,"bold"),bg="white",fg="black")
lab.place(x=50,y=260,height=50,width=400)
lab_up = Label(sp,text = "00",font = ("time new roman",30,"bold"),bg="green",fg="white")
lab_up.place(x=50,y=330 , height=50 , width=400)
button = Button(sp,text = "CHECK SPEED",font = ("time new roman",30,"bold"),relief=RAISED,bg= "red",fg="black",command = speedcheck)
button.place(x=50, y= 420 , height= 50 , width= 400)



sp.mainloop()

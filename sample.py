from tkinter import *
window=Tk()
window.geometry("420x420")
window.title("Kiran Gajjana")
window.config(background="skyblue")
photo = PhotoImage(file='background.png')
label=Label(window,text="KiranGajjana",font=('Arial',20,'bold'),fg='green',relief=RAISED,bd=10,padx=100,pady=100,image=photo,compound='bottom',background='gold')
label.place(x=30,y=0)
window.mainloop()
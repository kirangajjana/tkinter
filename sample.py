from tkinter import *
window=Tk()
def kirangajjana():
    for i in range(5):
        print("welcome")
window.geometry("420x420")
window.title("Kiran Gajjana")
window.config(background="skyblue")
label=Label(text='kirangajjana',fg='red',relief=RAISED,background="gold",padx=10,pady=20)
label.place(x=100,y=50)
button=Button(window,
              text="Click Me",
              command=kirangajjana)
button.pack()
window.mainloop()

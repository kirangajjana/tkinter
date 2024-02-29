from tkinter import *
window=Tk()
def kirangajjana():
    for i in range(5):
        print(f"welcome")
        if i==3:
            print('hello kiran gajjana')
window.geometry("420x420")
window.title("Kiran Gajjana")
def clickme():
    for i in range(5):
        print("hello welcome")
count=0
def new():
    global count
    count+=1
    print(count)


window.geometry('420x420')
window.config(background="skyblue")
label=Label(text='kirangajjana',fg='green',background='black',font=('bold',30),relief=RAISED)
label.pack()
button=Button(window,
              text='Click Me',
              fg='green',
              background='gold',
              command=clickme,
              activeforeground='green',
              activebackground='gold',
              compound='left')
button.pack()
button1=Button(window,
         text='Count',
         fg='gold',
         background='green',
         command=new)
button1.pack()
window.mainloop()
print('updated everything')

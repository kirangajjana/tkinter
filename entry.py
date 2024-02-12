from tkinter import *
window=Tk()
def submmit():
    user=entry.get()
    print('Hi:  '+user)

def delete():
    entry.delete(0,END)







window.title('Entry')
window.config(background='orange')
window.geometry('420x420')
entry=Entry(window,
            font=('Arial',50),
            fg='green',
            bg='white')
entry.pack()
submit=Button(window,
              text='submit',
              fg='gold',
              bg='black',
              command=submmit)
# delete=Button(window,
#               text='Delete',
#               fg='gold',
#               bg='black',
#               command=delete)
# delete.pack()
submit.pack()
window.mainloop()
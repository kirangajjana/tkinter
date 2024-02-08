# tkinter Practice....
---
## 07-02-2024..
---
### By Kiran gajjana
<br>

|WINDOW|Serves as a container to hold or contain the widgets|
|---|-------------------------------------------------------|
|Widgets|Gui elements like buttons,images,labels,textboxes  |
<br>

## Creating an simple window
```python
from tkinter import *
window=Tk() #instance of an window
```
### Displaying the window
```python
from tkinter import  *
window=Tk() #instance of an window
window.mainloop() # Displaying the window on computer screen
``` 
## Screenshot of window created on computer screen..
<br>
<img width="146" alt="Screenshot 2024-02-07 120941" src="https://github.com/kirangajjana/tkinter/assets/44581291/80d5d8ae-2d2f-43fe-8ec4-7fcaf66fc253">
<br>
 <b>we can change the size of the window by using below function<b>


```python
window.geometry(420*420)
```

<img width="311" alt="Screenshot 2024-02-07 121853" src="https://github.com/kirangajjana/tkinter/assets/44581291/bf4d19ab-025c-45af-aa61-a043707653d9">






we can change the title name of the window by using the below function
```python
window.title("kiran Gajjana")
```
<img width="314" alt="Screenshot 2024-02-07 122717" src="https://github.com/kirangajjana/tkinter/assets/44581291/683a3c08-23c3-4fdf-aa0f-b6acc2792bf9">
<br>
if we want to change the logo of the window you can add the below code
<br>



```python
icon = PhotoImage(file='logo.jpg')
window.iconphoto(True,icon)
```

Adding background color to the window
<br>

```python
window.config(background="skyblue")
```


<img width="314" alt="Screenshot 2024-02-07 124739" src="https://github.com/kirangajjana/tkinter/assets/44581291/182c992c-337c-4d1d-96e5-1965cd08a2e5">

<br>


|label|An area widget that holds text or images on the window|
|---|--------------------------------------------------------|
<br>


```python
label=Label(text='kirangajjana',fg='red',relief=RAISED,background="gold",padx=10,pady=20)
label.place(x=100,y=50)
```
<br>
<img width="314" alt="Screenshot 2024-02-08 161045" src="https://github.com/kirangajjana/tkinter/assets/44581291/d2879ce1-f2d9-423e-b9ed-2ec0c1fcc225">
<br>
now we will display button on the window

```python
button=Button(window,
              text="Click Me",
              command=kirangajjana)
```

Function for the text button click me is shown below
<br>
```python
def kirangajjana():
    for i in range(5):
        print("welcome")
```
<br>
once the user press on the click me button then the welcome will be displayed 5 times based on above function..   
<br> 
We can redesign the button and change the background and fonts also
<br>




```python
button=Button(window,
              text="Click Me",
              command=kirangajjana,
              font=("arial",10),
              fg='darkgreen',
              bg='black')

              
```              





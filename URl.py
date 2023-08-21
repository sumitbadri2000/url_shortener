import pyshorteners
from tkinter import *


#win is helping for window
#Tk is function which is window name
win = Tk()
#geometry is help give increase window size
win.geometry("400x400")
# confifure is help to give background
win.configure(bg="grey")
# fg is means tex color
# pack means is complete and run
# function define
def url_short():
    url=URl_input.get()
    UrlShort = pyshorteners.Shortener().tinyurl.short(url)
    URl_result.insert(END,UrlShort)

Label(win,text="Enter your url to convert in shortener",font="20",fg="black",bg="white",width="100").pack(pady=20)
# input box where we can write url 
# bd means border, pady means padding
URl_input=Entry(win,bd="5",font="14",width="30")
URl_input.pack(pady="10")
Button(win,text="URL SHORT",width="15",bg="blue",font="12",bd="2",fg="white",command=url_short).pack(pady=10)
Label(win,text="Your URL Shortener Link",font="16",fg="black",bg="white").pack(pady=10)
URl_result=Entry(win,bd="0",font="14",width="24",bg="grey")
URl_result.pack(pady=10)
mainloop()




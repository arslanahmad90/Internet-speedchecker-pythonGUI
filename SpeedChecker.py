import speedtest
import tkinter as tk  
import time
from tkinter import ttk
def bytes_to_mb(bytes):
    KB = 1024 # One Kilobyte is 1024 bytes
    MB = KB * 1024 # One MB is 1024 KB
    return int(bytes/MB)
def loadEvent():
    count=0
    while True:
        try:
            speed_test = speedtest.Speedtest()
            print("Session "+str(count+1)+" starts ..")
            download_speed = speed_test.download()
            downloadSpeed.set("Download Speed : "+ str(bytes_to_mb(download_speed))+"MBPS")
            upload_speed = speed_test.upload()
            uploadSpeed.set( "Updload Speed : "+str(bytes_to_mb(upload_speed))+"MBPS")
            print("Session "+str(count+1)+" ends ..")
            count=count+1
        except Exception as e:
            downloadSpeed.set("0MBPS")
            uploadSpeed.set("0MBPS")
            win.update()
            print(e)
            print("Exit")
        win.update()
        time.sleep(10)


win = tk.Tk()# Application Name
win.resizable(0,0)  
win.geometry("265x50")  
win.title("Internet Speed")# Label  
downloadSpeed= tk.StringVar()
downloadSpeed.set("Download Speed")
uploadSpeed= tk.StringVar()
uploadSpeed.set("Upload Speed")
#lbl = ttk.Label(win, text = "Enter the name:").grid(column = 0, row = 0)
lbl1 = ttk.Label(win, textvariable=downloadSpeed) #.grid(column = 5, row = 0)
lbl1.place(relx = 0.5,
                   rely = 0.4,
                   anchor = 'center')
lbl2 = ttk.Label(win, textvariable=uploadSpeed) #.grid(column = 5, row = 1)
lbl2.place(relx = 0.5,
                   rely = 0.8,
                   anchor = 'center')
win.after(500, loadEvent)
win.mainloop()
print("HELLO-1")

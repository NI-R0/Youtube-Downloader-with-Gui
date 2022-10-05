from pytube import YouTube
import tkinter as tk
from tkinter import ttk
import os


def download_video():
    url = textBox.get()
    #print("Started downloading video...")
    yt = YouTube(url)
    ytr = yt.streams.get_highest_resolution()
    path = 'C:/Users/' + os.getlogin() + '/Videos/YouTube'
    if(os.path.isdir(path)):
        ytr.download(path)
    else:
        ytr.download('C:/Users/' + os.getlogin() + '/Videos')
    #print("Video successfully downloaded")
    resetWindow()


def resetWindow():
    btnText.set("Download Video")
    # downloadBtn.state(tk.NORMAL)
    textBox.delete(0, tk.END)


def createHeadingStyle():
    style0 = ttk.Style()
    style0.configure("Custom.TLabel", font="Abel-Regular 18",
                     padding=[0, 90, 0, 40])


def createEntryStyle():
    style1 = ttk.Style()
    style1.configure("Custom.TEntry")


def createButtonStyle():
    style2 = ttk.Style()
    style2.configure("Custom.TButton", font="Abel-Regular 12",
                     padding=[50, 5, 50, 5])


window = tk.Tk()
window.title("YouTube Downloader")
window.geometry("500x450")
window.minsize(width=650, height=400)

createHeadingStyle()
createEntryStyle()
createButtonStyle()

titleLabel = ttk.Label(
    window, text="Download a YouTube video from URL", style="Custom.TLabel")
titleLabel.pack()


textBox = ttk.Entry(window, width=60, style="Custom.TEntry",
                    font=("Abel-Regular", 12))
textBox.pack(pady=50)

btnText = tk.StringVar()
btnText.set("Download Video")

downloadBtn = ttk.Button(window, textvariable=btnText,
                         command=download_video, style="Custom.TButton")
downloadBtn.pack()


window.mainloop()

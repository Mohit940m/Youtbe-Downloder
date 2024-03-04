import tkinter
import customtkinter
from pytube import YouTube

def startDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()
        title.configure(text=ytObject.title, text_color="black")
        finishLable.configure(text="Downloading", text_color="black")
        video.download()
        finishLable.configure(text="Downloaded!", text_color="black")
    except:
        print("Youtube link invalid")
        finishLable.configure(text="Download Faild", text_color="red")
    
def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_compeletaion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_compeletaion ))
    pPercentage.configure(text=per + "%")
    pPercentage.update()

    #update pregress bar
    progtessBar.set(float(percentage_of_compeletaion) / 100)  

#system settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

#our frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloder")

#adding UI element
title = customtkinter.CTkLabel(app, text="Insert a YouTube link")
title.pack(padx=10, pady=10)

#link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()



#download button
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=10)

#finished downloading
finishLable = customtkinter.CTkLabel(app, text="")
finishLable.pack()

#progress persentage
pPercentage = customtkinter.CTkLabel(app, text="0%")
pPercentage.pack()

progtessBar = customtkinter.CTkProgressBar(app, width=400)
progtessBar.set(0)
progtessBar.pack(padx=10, pady=10)

#Run app
app.mainloop()
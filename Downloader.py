from tkinter import *
from pytube import YouTube

root = Tk()

root.geometry('720x480')

root.title('Youtube Downloader')


def search_url():
    string = entered_url.get()

    yt = YouTube(string)

    global video_links

    video_links = yt.streams.all()

    print(video_links)

    i = 1

    for stream in video_links:
        list_box.insert(END, str(i) + "." + str(stream))

        i += 1


def dowload_video():
    seleted_video = list_box.curselection()

    seleted_video = int(seleted_video[0])

    video_to_download = video_links[seleted_video]

    video_to_download.download('Users\keshav\Desktop')

    downloaded.configure(text='Successfully Downloaded !!!', font=('Arial', 18), fg="green")


list_box = Listbox(root, width=60, height=15)

list_box.place(x=80, y=100)

label_url = Label(root, text="Enter URL :")

label_url.place(x=150, y=50)

entered_url = Entry(root, width=30)

entered_url.place(x=230, y=50)

search = Button(root, text='search', width=8, height=2, font=('Arial', 16), command=search_url)

search.place(x=520, y=45)

download = Button(root, text='DOWNLOAD', width=20, height=2, font=('Times Roman', 20), command=dowload_video)

download.place(x=260, y=380)

downloaded = Label(root, text="")

downloaded.place(x=250, y=440)

root.resizable(False, False)

root.mainloop()


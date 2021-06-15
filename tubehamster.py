from pytube import YouTube
import tkinter as tk
from tkinter import ttk


# def progress(streams, chunk: bytes, bytes_remaining: int):

#     """Progress bar"""

#     contentsize = video.filesize
#     size = contentsize - bytes_remaining

#     print('[Download progress]:' % (
#     '█' * int(size*20/contentsize), ' '*(20-int(size*20/contentsize)), float(size/contentsize*100)), end='')

def mp4_download(download_file_type):
    
    def progress(streams, chunk: bytes, bytes_remaining: int):
        contentsize = video.filesize
        size = contentsize - bytes_remaining
        
        print('[Download progress]:[%s%s]%.2f%%;' % ('█' * int(size*20/contentsize), ' '*(20-int(size*20/contentsize)), float(size/contentsize*100)), end='\r')
        

    # File type (video or audio)
    yt = YouTube(url_for_download.get(), on_progress_callback=progress)
    if download_file_type == 1:
        video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        print('Загрузка видео: "' + video.title + '"')
        
    else:
        video = yt.streams.filter(only_audio=True).order_by('abr').desc().first()
        print('Загрузка аудио: "' + video.title +'"')

    title_text = video.title
    title_text = (title_text[:28] + '...') if len(title_text) > 28 else title_text
    file_label = ttk.Label(window, text = 'File "' + title_text + '" is downloaded!:-)')
    file_label.grid(row=3, column=0, columnspan=4, padx=10, pady=0)
    video.download('./YouTube_downloads')
    


# Tkinter window

window = tk.Tk()
url_for_download = tk.StringVar()
window.title("TubeHamster 1.0") 
window.geometry('350x150')


h1_label = ttk.Label(window, text="TubeHamster 1.0", font=('Comic Sans MS',16,'bold'))
h1_label.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

#Name:
username_label = ttk.Label(window, text='URL: ')
username_label.grid(row=1, column=0, padx=10)

#Input name
username_entry = ttk.Entry(window, width=45, textvariable=url_for_download)
username_entry.grid(row=1, column=1, columnspan=3, padx=5)

#Download button
mp4_button = ttk.Button(window, text='Download video ', width=25, command=lambda: mp4_download(1))
mp4_button.grid(row=2, column=0, columnspan=2, padx=5, pady=10)

#Cancel button
audio_button = ttk.Button(window, text='Download audio', width=25, command=lambda: mp4_download(2))
audio_button.grid(row=2, column=2, columnspan=2, padx=5, pady=10)


window.mainloop()
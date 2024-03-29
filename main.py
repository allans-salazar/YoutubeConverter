from pytube import YouTube
import tkinter
from tkinter import filedialog
from tkinter import ttk


""" YOUTUBE FUNCTIONS """
def download_video(url, save_path): #Youtube function downloads the video & saves to folder path 
    try:
        yt = YouTube(url, on_progress_callback=on_progress)
        streams = yt.streams.filter(progressive = True, file_extension="mp4")
        highest_res_stream = streams.get_highest_resolution()
        highest_res_stream.download(output_path=save_path)
        print("Video downloaded succesfully!")

    except Exception as e: 
        print(e)
        x.set('ERROR IN DOWNLOAD... TRY AGAIN')

def download_audio(url, save_path): #Youtube function downloads the video & saves to folder path 
    try:
        yt = YouTube(url, on_progress_callback=on_progress)
        stream = yt.streams.filter(only_audio=True).first()
        stream.download(output_path=save_path)
        print("Video downloaded succesfully!")

    except Exception as e: 
        print(e)
        x.set('ERROR IN DOWNLOAD... TRY AGAIN')

def on_progress(stream, total_size, bytes_remaining): #Youtube function allows to get the loading progress
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_completed = round(bytes_downloaded / total_size * 100)
    loadingBar['value'] = percentage_completed #Used to update the loadingbar 
    main_window.update()
    print(percentage_completed)

    if (loadingBar['value'] == 100):
        x.set('Completed Download!')


""" GUI Functions """
def open_file_dialog(): #function from tkinter to open Folders from PC 
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")
    return folder

def downloadMP4Button():
    loadingBar.pack()
    link = entry.get()
    save_dir = open_file_dialog()

    if save_dir:
        print("Started download...")
        download_video(link, save_dir)
    else:
        print("Invalid save location.")

def downloadMP3Button():
    loadingBar.pack()
    main_window.update()
    link = entry.get()
    save_dir = open_file_dialog()

    if save_dir:
        print("Started download...")
        download_audio(link, save_dir)
    else:
        print("Invalid save location.")


def out(): #To remove the result frame message
    x.set(' ')
    loadingBar['value'] = 0
    loadingBar.pack_forget()
def messageDissapear():
    entry.delete(0, 'end')
    main_window.after(7000,out)



""" GUI Window """
main_window = tkinter.Tk()

main_window.title("Youtube Converter App")
main_window.geometry("400x150")

#Displays Label (Instructions) on top of the screen & Entry (Type in the Link) 
top_frame = tkinter.Frame(main_window)
label = tkinter.Label(top_frame, text = 'Enter YouTube link: ')
entry = tkinter.Entry(top_frame, width = 35)
label.pack()
entry.pack()

#Displays MP4 Button 
bottom_frame = tkinter.Frame(main_window)
mp4Button = tkinter.Button(bottom_frame, text = 'CONVERT TO MP4', command = lambda:[downloadMP4Button(), messageDissapear()])
mp4Button.pack(side="left")

#Display MP3 Button
bottom_frame2 = tkinter.Frame(main_window)
mp3Button = tkinter.Button(bottom_frame2, text = 'CONVERT TO MP3', command= lambda:[downloadMP3Button(), messageDissapear()])
mp3Button.pack(side="left")

#Progress Bar
barFrame = tkinter.Frame(main_window)
loadingBar = ttk.Progressbar(barFrame, orient='horizontal', mode='determinate', length=280)


#Invisible Frame with Label to pop up when download has completed
result_frame = tkinter.Frame(main_window)
x = tkinter.StringVar()
show = tkinter.Label(result_frame, textvariable = x)
show.pack()

#Packs all the frames I used
top_frame.pack()
bottom_frame.pack()
bottom_frame2.pack()
barFrame.pack()
result_frame.pack()


tkinter.mainloop()
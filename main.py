from pytube import YouTube
import tkinter
from tkinter import filedialog

 
def download_video(url, save_path): #Youtube function downloads the video & saves to folder path 
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive = True, file_extension="mp4")
        highest_res_stream = streams.get_highest_resolution()
        highest_res_stream.download(output_path=save_path)
        print("Video downloaded succesfully!")

    except Exception as e: 
        print(e)

def open_file_dialog(): #function from tkinter to open Folders from PC 
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")
    return folder



class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.title("Youtube MP4 Converter")
        self.main_window.geometry("400x120")

        #Displays Label on top of the screen & Entry for user to put in the link 
        self.top_frame = tkinter.Frame(self.main_window)
        self.label = tkinter.Label(self.top_frame, text = 'Enter YouTube link: ')
        self.entry = tkinter.Entry(self.top_frame, width = 35)
        self.label.pack(ipadx=0.5, ipady=0.5)
        self.entry.pack(ipadx=0.5, ipady=0.5)

        #Displays MP4 Button 
        self.bottom_frame = tkinter.Frame(self.main_window)
        self.mp4Button = tkinter.Button(self.bottom_frame, text = 'CONVERT TO MP4', command = lambda:[self.downloadButton(), self.messageDissapear()])
        self.mp4Button.pack(side = 'left')

        #Invisible Frame with Label to pop up when download has completed
        self.result_frame = tkinter.Frame(self.main_window)
        self.x = tkinter.StringVar()
        self.show = tkinter.Label(self.result_frame, textvariable = self.x)
        self.show.pack(side = 'bottom')

        #Packs all the frames I used
        self.top_frame.pack()
        self.bottom_frame.pack()
        self.result_frame.pack()

        
        tkinter.mainloop()


    

    def downloadButton(self):
        link = self.entry.get()
        save_dir = open_file_dialog()

        if save_dir:
            print("Started download...")
            download_video(link, save_dir)
            self.x.set('Completed Download!')
        else:
            print("Invalid save location.")


    def out(self): #To remove the result frame message
        self.x.set(' ')
    def messageDissapear(self):
        self.entry.delete(0, 'end')
        self.main_window.after(9000,self.out)
        


#main code
mygui = MyGUI()

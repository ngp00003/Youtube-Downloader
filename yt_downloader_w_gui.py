import os
import yt_dlp
import traceback
from tkinter import *
from tkinter import ttk, messagebox, filedialog

# Global state
download_folder = os.getcwd()
progress_percent = 0

# Update progress bar callback
def progress_hook(d):
    if d['status'] == 'downloading':
        percent = d.get('_percent_str', '0.0%').strip()
        percent_value = float(percent.replace('%', '').strip())
        progress_bar['value'] = percent_value
        progress_label.config(text=f"{percent}")
        root.update_idletasks()
    elif d['status'] == 'finished':
        progress_label.config(text="Processing...")

# Start download
def download():
    url = url_entry.get()
    choice = format_var.get()

    if not url:
        messagebox.showerror("Error", "Please enter a URL.")
        return

    if not download_folder:
        messagebox.showerror("Error", "Please select a download folder.")
        return

    ffmpeg_path = r"C:\ProgramData\chocolatey\lib\ffmpeg\tools\ffmpeg\bin"
    ydl_opts = {
        'outtmpl': os.path.join(download_folder, '%(title)s-%(id)s.%(ext)s'),
        'progress_hooks': [progress_hook],
        'ffmpeg_location': ffmpeg_path,
        'verbose': True,
        'noplaylist': True,
        'nocheckcertificate': True,  # Optional, good for school/work networks
        'noutm': True,  # Don't use video title in output
        'nopart': True,  # Don't create .part temp files
        'nooverwrites': True,  # Don't overwrite
        'windowsfilenames': True,  # Remove bad chars from filenames
        'updatetime': False,  # ⬅️ Add this line to disable backdating

    }

    if choice == "Video":
        ydl_opts.update({
            'format': 'bestvideo+bestaudio/best',
            'merge_output_format': 'mp4',
        })
    elif choice == "Audio (MP3)":
        ydl_opts.update({
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        })
    elif choice == "Audio (M4A)":
        ydl_opts.update({
            'format': 'bestaudio[ext=m4a]',
        })

    try:
        progress_bar['value'] = 0
        progress_label.config(text="")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            result = ydl.download([url])

        progress_label.config(text="Download complete!")
        messagebox.showinfo("Success", "Download complete!")

    except Exception as e:
        traceback.print_exc()  # Print full error to console
        messagebox.showerror("Error", f"Download failed:\n{e}")

# Choose folder
def choose_folder():
    global download_folder
    folder = filedialog.askdirectory()
    if folder:
        download_folder = folder
        folder_label.config(text=f"Saving to: {download_folder}", fg="green")

# GUI setup
root = Tk()
root.title("YouTube Downloader - yt-dlp")
root.geometry("550x360")
root.resizable(False, False)

Label(root, text="Enter YouTube URL:", font=("Arial", 12)).pack(pady=10)
url_entry = Entry(root, width=65, font=("Arial", 10))
url_entry.pack(pady=5)

Label(root, text="Select format:", font=("Arial", 12)).pack(pady=10)
format_var = StringVar(value="Video")
format_menu = OptionMenu(root, format_var, "Video", "Audio (MP3)", "Audio (M4A)")
format_menu.pack()

Button(root, text="Choose Folder", command=choose_folder, font=("Arial", 10), bg="#6c757d", fg="white").pack(pady=10)
folder_label = Label(root, text=f"Saving to: {download_folder}", font=("Arial", 9), fg="gray")
folder_label.pack()

download_button = Button(root, text="Download", command=download, font=("Arial", 12), bg="#007bff", fg="white")
download_button.pack(pady=20)

# Progress bar and label
progress_bar = ttk.Progressbar(root, orient=HORIZONTAL, length=400, mode='determinate')
progress_bar.pack(pady=5)
progress_label = Label(root, text="", font=("Arial", 10))
progress_label.pack()

root.mainloop()
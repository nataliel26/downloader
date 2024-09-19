import yt_dlp
import tkinter as tk
from tkinter import filedialog, messagebox

def get_ydl_options(format_type, output_path):
    return {
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        'format': 'best[ext=mp4]' if format_type == 'video' else 'bestaudio/best',
    }

def download_content():
    url = url_entry.get()
    output_path = filedialog.askdirectory()

    if not url or not output_path:
        messagebox.showerror("Error", "URL or destination directory not informed")
        return

    try:
        ydl_opts = get_ydl_options(download_var.get(), output_path)
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        messagebox.showinfo("Success", f"{download_var.get().capitalize()} successfully downloaded!")
    except yt_dlp.DownloadError as e:
        messagebox.showerror("Download Error", f"Failed to download: {e}")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")

app = tk.Tk()
app.title("Video Downloader")
app.geometry("400x200")

url_label = tk.Label(app, text="Video URL:")
url_label.pack(pady=5)
url_entry = tk.Entry(app, width=50)
url_entry.pack(pady=5)

download_var = tk.StringVar(value="video")
video_radio = tk.Radiobutton(app, text="Download Video", variable=download_var, value="video")
video_radio.pack(pady=5)
audio_radio = tk.Radiobutton(app, text="Download Audio", variable=download_var, value="audio")
audio_radio.pack(pady=5)

download_button = tk.Button(app, text="Start Download", command=download_content)
download_button.pack(pady=20)

app.mainloop()

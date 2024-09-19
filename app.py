import os
import yt_dlp
import tkinter as tk
from tkinter import filedialog, messagebox
from ffmpeg import download_ffmpeg

def download_video():
    url = url_entry.get()
    output_path = filedialog.askdirectory()

    if not url or not output_path:
        messagebox.showerror("Erro", "URL ou pasta de destino não informada.")
        return

    ydl_opts = {
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        'format': 'best[ext=mp4]',
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        messagebox.showinfo("Sucesso", "Vídeo baixado com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Falha ao baixar o vídeo: {e}")

app = tk.Tk()
app.title("Video Downloader")
app.geometry("400x150")

url_label = tk.Label(app, text="URL do vídeo:")
url_label.pack(pady=5)
url_entry = tk.Entry(app, width=50)
url_entry.pack(pady=5)

download_button = tk.Button(app, text="Baixar Vídeo", command=download_video)
download_button.pack(pady=20)

app.mainloop()

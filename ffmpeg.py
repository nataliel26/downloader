import os
import platform
import urllib.request
import zipfile

def download_ffmpeg():
    system = platform.system().lower()
    
    if system == "windows":
        url = "https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip"
        ffmpeg_zip = "ffmpeg.zip"
        ffmpeg_folder = "ffmpeg"
    elif system == "linux":
        url = "https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-i686-static.tar.xz"
        ffmpeg_zip = "ffmpeg.tar.xz"
        ffmpeg_folder = "ffmpeg"
    else:
        raise Exception("Sistema operacional não suportado")

    if not os.path.exists(ffmpeg_folder):
        print("Baixando FFmpeg...")
        urllib.request.urlretrieve(url, ffmpeg_zip)

        if ffmpeg_zip.endswith(".zip"):
            with zipfile.ZipFile(ffmpeg_zip, 'r') as zip_ref:
                zip_ref.extractall(ffmpeg_folder)
        else:
            os.system(f"tar -xvf {ffmpeg_zip} -C {ffmpeg_folder}")

        os.remove(ffmpeg_zip)
        print("FFmpeg baixado e extraído com sucesso!")

download_ffmpeg()

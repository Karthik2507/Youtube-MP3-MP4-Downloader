import yt_dlp
import streamlit as st

st.set_page_config(
    page_title="YouTube to MP3 Downloader",
    page_icon="🎵"
)
def download_audio(url, output_folder='C:/Users/User/Downloads'):
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'extractaudio': True,
            'audioquality': 0,
            'outtmpl': f'{output_folder}/%(title)s.%(ext)s',
            'postprocessors': [{'key': 'FFmpegExtractAudio','preferredcodec': 'mp3','preferredquality': '192',}],
            'ffmpeg_location': r"C:\ffmpeg-7.1-essentials_build\bin\ffmpeg.exe"
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            print(f"Audio downloaded successfully.")
            print("---------------------------------------") 
    except Exception as e:
        print(f"An error occurred: {e}")

st.title("YouTube to MP3 Downloader")
st.write("Enter the YouTube video URL to download the audio as MP3.")

youtube_url = st.text_input("YouTube Video URL")
if youtube_url:
    if st.button("Download MP3"):
        with st.spinner("Downloading and converting..."):
            try:
                mp3_file = download_audio(youtube_url)
                st.success(f"Download complete! Go and check your download folder")
            except Exception as e:
                st.error(f"Error: {e}")
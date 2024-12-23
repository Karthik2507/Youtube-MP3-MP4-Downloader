import yt_dlp
import streamlit as st

st.set_page_config(page_title="YouTube Video Downloader", page_icon="🎥")

def get_available_resolutions(url):
    try:
        ydl_opts = {'quiet': True}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=False)
            formats = info_dict.get('formats', [])
            resolutions = []
            for f in formats:
                if 'height' in f and f['height'] is not None and f['height'] >= 144:
                    resolutions.append(f'{f["height"]}p')
            return sorted(set(resolutions), reverse=True)  # Sort in descending order
    except Exception as e:
        print(f"Error retrieving video formats: {e}")
        return []

def download_video(url, resolution, output_folder='C:/Users/User/Downloads'):
    try:
        ydl_opts = {'format': f'bestvideo[height={resolution}]+bestaudio/best',
                    'outtmpl': f'{output_folder}/%(title)s.%(ext)s',
                    'ffmpeg_location': r"C:\ffmpeg-7.1-essentials_build\bin\ffmpeg.exe",
                    'overwrites': True}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            print(f"Video downloaded successfully in {resolution}.\n---------------------------------------")
    except Exception as e:
        print(f"An error occurred: {e}")

st.title("YouTube Video Downloader")
st.write("Enter the YouTube video URL to download the video.")
youtube_url = st.text_input("YouTube Video URL")

if youtube_url:
    resolutions = get_available_resolutions(youtube_url)  
    if resolutions:
        selected_resolution = st.selectbox("Select Resolution", resolutions)
        if st.button("Download Video"):
            with st.spinner(f"Downloading video in {selected_resolution}..."):
                try:
                    download_video(youtube_url, selected_resolution[:-1])  # Remove the "p" to match yt-dlp format
                    st.success(f"Download complete! Check your download folder.")
                except Exception as e:
                    st.error(f"Error: {e}")
    else:
        st.warning("No available resolutions found for this video.")

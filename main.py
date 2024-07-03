import os

import streamlit as st
from pytube import YouTube
from pydub import AudioSegment
import google.generativeai as genai

from config import configure_genai
from prompt import create_summarize_prompt

# Configure the generative AI model
model = configure_genai()


# Initialize session state
def initialize_session_state():
    if "audio_downloaded" not in st.session_state:
        st.session_state["audio_downloaded"] = False
    if "mp3_file" not in st.session_state:
        st.session_state["mp3_file"] = None
    if "mp4_file" not in st.session_state:
        st.session_state["mp4_file"] = None
    if "genai_audio_file" not in st.session_state:
        st.session_state["genai_audio_file"] = None


initialize_session_state()


# Download audio from YouTube
def download_audio(url):
    try:
        yt = YouTube(url)
        audio_stream = yt.streams.filter(only_audio=True).first()
        mp4_file = audio_stream.download()
        mp3_file = mp4_file.replace(".mp4", ".mp3")
        AudioSegment.from_file(mp4_file).export(mp3_file, format="mp3")
        return mp4_file, mp3_file
    except Exception as e:
        return str(e), None


# Streamlit app
def main():
    st.title("YouTube Audio Summarizer")
    url = st.text_input("Enter YouTube URL")

    if st.button("Download Audio"):
        if url:
            with st.spinner("Downloading..."):
                mp4_file, mp3_file = download_audio(url)
                if mp4_file and mp4_file.endswith(".mp4"):
                    st.success("Download Successful!")
                    st.session_state["audio_downloaded"] = True
                    st.session_state["mp3_file"] = mp3_file
                    st.session_state["mp4_file"] = mp4_file
                    st.session_state["genai_audio_file"] = genai.upload_file(
                        path=st.session_state["mp3_file"]
                    )
                else:
                    st.error(f"Error: {mp4_file}")
        else:
            st.warning("Please enter a valid URL")

    if st.session_state["audio_downloaded"]:
        st.audio(st.session_state["mp4_file"], format="audio/mp4")
        summary_option = st.radio(
            "Choose summary length:", ("50 words", "100 words", "300 words")
        )
        if st.button("Summarize Audio"):
            prompt = create_summarize_prompt(summary_option)
            with st.spinner("Generating summary..."):
                try:
                    response = model.generate_content(
                        [prompt, st.session_state["genai_audio_file"]],
                        request_options={"timeout": 600},
                    )
                    summary = response.text
                    st.subheader("Summary of the Audio Content:")
                    st.write(summary)
                except Exception as e:
                    st.error(f"Error generating summary: {e}")


if __name__ == "__main__":
    main()

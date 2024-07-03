# YouTube Audio Summarizer

This Streamlit application allows users to summarize YouTube videos. By providing a YouTube URL, the application downloads the audio from the video, and then uses Gemini to create a summary of the audio content.

![Screenshot of the application](images/screenshot.png)

## Applications

- Audio Insights and Analytics
- Podcast & Video Summaries
- Market Research
- News Summarization

## Features

- Download audio from YouTube videos
- Summarize the audio content in different lengths (50 words, 100 words, 300 words)
- Simple and intuitive user interface

## Installation and Setup

### Prerequisites

- Python 3.11 or higher
- pip (Python package installer)
- Gemini API key

### Creating a Python Virtual Environment

1. **Open your terminal or command prompt**.

2. **Clone repo**:
    ```sh
    gh repo clone ankur-manikandan/youtube-audio-summarizer
    ```

3. **Create a virtual environment**:
    ```sh
    python -m venv venv
    ```

4. **Activate the virtual environment**:
    - **On Windows**:
        ```sh
        venv\Scripts\activate
        ```
    - **On macOS and Linux**:
        ```sh
        source venv/bin/activate
        ```

### Installing Dependencies

Once the virtual environment is activated, install the necessary packages using `pip`:
```sh
pip install -r requirements.txt
```

### Setting Up the Gemini API Key

1. Obtain your [Gemini API key](https://ai.google.dev/).
2. **Set the environment variable `GEMINI_API_KEY` with your API key**:
    - **On Windows**:
        ```sh
        set GEMINI_API_KEY=your_api_key_here
        ```
    - **On macOS and Linux**:
        ```sh
        export GEMINI_API_KEY=your_api_key_here
        ```

### Run the App

To run the Streamlit application, execute the following command:
```sh
streamlit run main.py
```

## Next Steps

Generate audio insights for analytics purposes.

## Example Summaries

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/2-Gdv0BO-oI/0.jpg)](https://www.youtube.com/watch?v=2-Gdv0BO-oI&ab_channel=Spacedust)


### Summary in 50 words or less

The audio discusses the observable universe, its age, and the cosmic web of galaxies, stars, and planets within it. It delves into dark matter and dark energy, the cosmic microwave background radiation, and the formation of elements. The audio also explores black holes, wormholes, gravitational waves, and the possibility of life beyond Earth, including the search for extraterrestrial intelligence and the Fermi paradox.

### Summary in 100 words or less

The audio discusses the observable universe, its age, and the cosmic web of galaxies, stars, and planets within it. It delves into the mysteries of dark matter and dark energy, their roles in the universe's expansion and structure formation. The audio explains the cosmic microwave background radiation as the afterglow of the Big Bang and its significance in understanding the early universe. It explores black holes, wormholes, gravitational waves, and the formation and evolution of stars and galaxies. The audio also touches upon the search for exoplanets, the concept of habitable zones, and the possibility of life beyond Earth, including the Fermi paradox and the Drake equation. It concludes with a discussion of the Kardashev scale, a method for classifying civilizations based on their energy consumption, and the ethical considerations of contacting alien civilizations.

### Summary in 300 words or less

The audio content discusses various aspects of the universe, from its vastness and age to the mysteries of dark matter and dark energy. It delves into the cosmic web of galaxies, the life cycle of stars, and the intriguing possibility of life beyond Earth.

The observable universe, a sphere with a radius of 46.5 billion light-years, is only a fraction of the entire universe, which is thought to be much larger. The audio explores the concept of the cosmic microwave background radiation, the afterglow of the Big Bang, which provides insights into the infant universe. It also discusses the four fundamental forces of nature: gravity, electromagnetism, the weak nuclear force, and the strong nuclear force, which govern the interactions of matter and energy.

The audio delves into the mysteries of dark matter and dark energy, which constitute a significant portion of the universe's total mass and energy content. It explores the concept of black holes, those enigmatic regions of spacetime where gravity dominates, and the role of supermassive black holes in the formation and evolution of galaxies.

The search for life beyond Earth is a recurring theme, with discussions on the habitable zone around stars, the possibility of life on icy moons like Europa and Enceladus, and the intriguing properties of extremophiles, organisms that thrive in extreme environments. The audio also explores the Fermi paradox, the contradiction between the high probability of extraterrestrial civilizations and the lack of evidence for their existence.

The audio concludes with a discussion on the Kardashev scale, a method of measuring a civilization's technological advancement based on its energy consumption, and the hypothetical megastructures known as Dyson spheres, which could be built by advanced civilizations to harness the energy of their stars. It ends with a thought-provoking question: "Do you think we will ever be able to find life?"
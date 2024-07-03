import os
import google.generativeai as genai


def configure_genai():
    genai.configure(api_key=os.environ["GEMINI_API_KEY"])
    generation_config = {
        "temperature": 0,
    }
    model = genai.GenerativeModel(
        model_name="gemini-1.5-pro", generation_config=generation_config
    )
    return model

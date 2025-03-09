import os
import requests
from dotenv import load_dotenv

load_dotenv()
HUGGINGFACE_API_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")

if not HUGGINGFACE_API_TOKEN:
    raise ValueError("API Token No Find, .env")

MODEL = "google/flan-t5-small"

def generate_answer_huggingface(context, question, max_length=200):
    API_URL = f"https://api-inference.huggingface.co/models/{MODEL}"
    headers = {"Authorization": f"Bearer {HUGGINGFACE_API_TOKEN}"}
    data = {
        "inputs": f"Context: {context}\n\nQuestion: {question}\n\nAnswer:",
        "parameters": {"max_length": max_length, "temperature": 0.7},
    }

    try:
        response = requests.post(API_URL, headers=headers, json=data, timeout=15)

        if response.status_code != 200:
            return f"Error API ({response.status_code}): {response.text}"

        try:
            return response.json()[0]['generated_text']
        except (IndexError, KeyError):
            return "API fail, Try again!"

    except requests.exceptions.Timeout:
        return "⏳ API respone low, Try again!"
    except requests.exceptions.RequestException as e:
        return f"error API: {str(e)}"

import os
import requests
from dotenv import load_dotenv

# Load API Token từ file .env
load_dotenv()
HUGGINGFACE_API_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")

if not HUGGINGFACE_API_TOKEN:
    raise ValueError("API Token không được tìm thấy! Hãy kiểm tra file .env")

MODEL = "google/flan-t5-small"

def generate_answer_huggingface(context, question, max_length=200):
    """Gọi API Hugging Face để sinh câu trả lời"""
    API_URL = f"https://api-inference.huggingface.co/models/{MODEL}"
    headers = {"Authorization": f"Bearer {HUGGINGFACE_API_TOKEN}"}
    data = {
        "inputs": f"Context: {context}\n\nQuestion: {question}\n\nAnswer:",
        "parameters": {"max_length": max_length, "temperature": 0.7},
    }

    try:
        response = requests.post(API_URL, headers=headers, json=data, timeout=15)

        # Kiểm tra nếu API không phản hồi dữ liệu
        if response.status_code != 200:
            return f"Lỗi API ({response.status_code}): {response.text}"

        # Kiểm tra nếu API trả về JSON rỗng hoặc không hợp lệ
        try:
            return response.json()[0]['generated_text']
        except (IndexError, KeyError):
            return "❌ API không trả về dữ liệu hợp lệ. Hãy thử lại sau!"

    except requests.exceptions.Timeout:
        return "⏳ API phản hồi quá chậm. Hãy kiểm tra kết nối mạng hoặc thử lại sau."
    except requests.exceptions.RequestException as e:
        return f"❌ Lỗi khi gọi API: {str(e)}"

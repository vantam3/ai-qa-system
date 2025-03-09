# AI-Powered Question-Answering System

## 📌 Introduction
This project is a document-based question-answering system (PDF) that uses FAISS for information retrieval and Hugging Face language models for answer generation.

## 🔹 1. Installation & Running the Application

### 📌 Step 1: Clone the project & set up a virtual environment
```sh
git clone https://github.com/vantam3/ai-qa-system.git
cd ai-qa-system
python -m venv venv
source venv/bin/activate  # On Mac/Linux
venv\Scripts\activate      # On Windows
pip install -r requirements.txt
```

### 📌 Step 2: Set up API Token
- Create a `.env` file and add your Hugging Face API Token:
  ```
  HUGGINGFACE_API_TOKEN=your_api_token
  ```
- **Setting up permissions on Hugging Face:**
  1. Go to **[Hugging Face Settings](https://huggingface.co/settings/tokens)**.
  2. Click **New Token** and name it (e.g., `AI-QA-System`).
  3. Under **Permissions**, select the following:
     - ✅ **Read** (Access models and datasets)
     - ✅ **Inference** (Make API inference requests)
  4. Click **Generate Token** and copy the key.
  5. Add this token to the `.env` file as shown above.

### 📌 Step 3: Run the application
```sh
streamlit run app.py
```
Then open your browser at **http://localhost:8501** to test the application.

## 🔹 2. How to Test the Application
1. **You can upload your own PDF file or download and use the test file `test_pdf_ai.pdf` located in the `data/` folder to test.**
2. **Ask sample questions:**  
   - *"Where is the Eiffel Tower?"*
   - *"What is Artificial Intelligence?"*
3. **Check if the AI-generated answer is correct.**

## 🔹 3. API Usage Limitations
- **Hugging Face free API** has a request limit (~50-100 requests/day). If you encounter `429 Too Many Requests`, please wait or upgrade your account.
- **The `flan-t5-small` model has a maximum input limit of ~512 tokens (~400 words) per request.**
- **Larger models (`flan-t5-xl`) can support more tokens but are still limited to around 1024 tokens (~800 words).**
- **Hugging Face free API may have a limit of ~2048 tokens (~1600 words).**
- **If the PDF file is too long, split the content before sending it to the AI model.**

## 🔹 4. Technologies Used
- **Hugging Face API (`flan-t5-small`)**
- **FAISS (Vector search retrieval)**
- **Streamlit (Web interface)**
- **pdfplumber (Extracting text from PDFs)**
- **Sentence Transformers (Embedding models)**

## 🔹 5. API Error Handling Guide
- **401 (Unauthorized):** Invalid or missing API Token.
- **503 (Service Unavailable):** The API is overloaded, please try again later.
- **429 (Too Many Requests):** The API free-tier limit has been exceeded; wait or upgrade your account.
- **Input not recognized:** If the text is too long, try splitting it before sending it to the API.

## 🔹 6. Contact Information
For any inquiries, please contact:  
📧 Email: vtam0805@gmail.com


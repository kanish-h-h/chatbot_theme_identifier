from fastapi import FastAPI
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="Doc_theme_Chatbot API",
    description="Document Analysis Chatbot",
    version="0.1.0"
)

@app.get("/")
def health_check():
    return {"status": "active", "version": app.version}

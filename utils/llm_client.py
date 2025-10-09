import os
from openai import OpenAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

try:
    api_key = st.secrets["GROQ_API_KEY"]
except Exception:
    api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY not found")

client = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1"
)

def ask_groq(prompt):
    try:
        if not prompt.strip():
            return "Please provide a valid question."
        
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": "Answer questions about resumes based on the provided context."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error in ask_groq: {e}")
        return f"Error: {str(e)}"
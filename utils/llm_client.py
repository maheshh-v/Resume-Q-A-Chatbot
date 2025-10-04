import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY not found in environment variables")

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
                {"role": "system", "content": "You are a helpful assistant that answers questions about resumes."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return "Sorry, couldn't process your request. Please try again."
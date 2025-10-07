from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
import google.generativeai as genai
genai.configure(api_key=api_key)

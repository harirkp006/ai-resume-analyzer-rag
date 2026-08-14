from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
def generate_answer(query, context):

    prompt = f"""
You are an experienced technical recruiter.

Use the resume information below to evaluate the candidate.

Resume Information:
{context}

Question:
{query}

Instructions:
- If asked for a score, provide a score out of 10.
- Explain strengths.
- Explain weaknesses.
- Suggest improvements.
- Base your evaluation only on the resume content.

Answer:
"""

    response = API_KEY.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text

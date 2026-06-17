from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def generate_insights(question, dataframe):

    sample_data = dataframe.head(10).to_string()

    prompt = f"""
    You are a senior business analyst.

    Question:
    {question}

    Query Result:
    {sample_data}

    Rules:
    1. Generate exactly 3 insights.
    2. Each insight must be one sentence.
    3. Use bullet points.
    4. Be concise.
    5. No introductions.
    6. No conclusions.

    Insights:
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ]
    )

    return response.choices[0].message.content
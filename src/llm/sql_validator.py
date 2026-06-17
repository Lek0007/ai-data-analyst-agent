from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def validate_sql(
    question,
    sql_query,
    schema
):

    prompt = f"""
You are a PostgreSQL SQL validator.

Question:
{question}

Schema:
{schema}

SQL Query:
{sql_query}

Instructions:

1. Check table names.
2. Check column names.
3. Check joins.
4. Check aggregations.
5. Check SQL correctness.

OUTPUT RULES:

- If query is valid, return exactly:

VALID

- If query is invalid, return ONLY the corrected SQL query.

- Do NOT explain.
- Do NOT provide reasoning.
- Do NOT use markdown.
- Do NOT use code blocks.
- Do NOT write any text except VALID or corrected SQL.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content.strip()
import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

import pandas as pd

from sqlalchemy import text

from database.connection import engine

from groq import Groq
from dotenv import load_dotenv

from llm.prompts import (
    schema,
    relationships,
    examples
)

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

question = input(
    "Ask a question: "
)

prompt = f"""
You are an expert PostgreSQL SQL generator.

Rules:

1. Generate ONLY SQL.
2. Return exactly ONE SQL query.
3. Do NOT explain.
4. Do NOT add comments.
5. Do NOT use markdown.
6. Use ONLY tables and columns provided.
7. Never invent columns.
8. Never invent tables.
9. Only generate SELECT statements.
10. Use the relationships provided.
11. Prefer direct JOINs.
12. Avoid subqueries unless absolutely necessary.

Schema:

{schema}

Relationships:

{relationships}

Examples:

{examples}

Question:

{question}
"""

print("\nGenerating SQL...")

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

generated_sql = (
    response
    .choices[0]
    .message
    .content
)

generated_sql = (
    generated_sql
    .replace("```sql", "")
    .replace("```", "")
    .strip()
)

sql_lower = generated_sql.lower()

blocked_words = [
    "drop",
    "delete",
    "update",
    "insert",
    "alter",
    "truncate",
    "create"
]

if any(word in sql_lower for word in blocked_words):
    raise ValueError(
        "Unsafe SQL detected"
    )

print("\nGenerated SQL:\n")
print(generated_sql)

print("\nExecuting SQL...\n")

try:

    with engine.connect() as conn:

        conn.execute(
            text(
                "SET statement_timeout = 10000"
            )
        )

        df = pd.read_sql(
            generated_sql,
            conn
        )

    print("\nResults:\n")
    print(df.head())

except Exception as e:

    print("\nExecution Error:\n")
    print(e)
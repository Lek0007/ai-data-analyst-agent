import time
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

from utils.logger import log_query
import pandas as pd

from sqlalchemy import text

from database.connection import engine
from analytics.chart_selector import choose_chart

from analytics.chart_generator import (
    create_bar_chart,
    create_line_chart
)
from groq import Groq
from dotenv import load_dotenv

from database.schema_extractor import (
    extract_schema
)
from llm.sql_validator import validate_sql
from llm.prompts import (
    get_relationships,
    examples
)
relationships = get_relationships()

schema = extract_schema()

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
13. Some date columns are stored as TEXT.
14. Always CAST date columns to TIMESTAMP before using EXTRACT, DATE_TRUNC, AGE, or date calculations.

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

print("\nValidating SQL...\n")

validation_result = validate_sql(
    question,
    generated_sql,
    schema
)
if validation_result.strip() == "VALID":

    print("\nSQL validation passed.")

else:

    if not validation_result.lower().startswith("select"):

        raise ValueError(
            "Validator returned invalid output."
        )

    print("\nValidator corrected query:\n")

    print(validation_result)

    generated_sql = validation_result
print("\nExecuting SQL...\n")

try:

    with engine.connect() as conn:

        conn.execute(
            text(
                "SET statement_timeout = 10000"
            )
        )

        start_time = time.time()

        df = pd.read_sql(
            generated_sql,
            conn
        )

        execution_time =round( 
            time.time() - start_time,
            3
            )

    print("\nResults:\n")
    print(df.head(10))

    log_query(
    question,
    generated_sql,
    execution_time,
    len(df)
    )

    chart_type = choose_chart(df)

    if chart_type == "bar":

        create_bar_chart(df)

    elif chart_type == "line":

        create_line_chart(df)

    from llm.insight_generator import generate_insights

    insights = generate_insights(
    question,
    df)

    print("\nBusiness Insights:\n")
    print(insights)


except Exception as e:

    print("\nExecution Error:\n")
    print(e)
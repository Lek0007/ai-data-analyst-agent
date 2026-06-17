import pandas as pd

from database.connection import engine


def extract_schema():

    query = """
    SELECT
        table_name,
        column_name
    FROM information_schema.columns
    WHERE table_schema='public'
    ORDER BY table_name, ordinal_position;
    """

    df = pd.read_sql(
        query,
        engine
    )

    schema_text = ""

    for table in df["table_name"].unique():


        schema_text += f"\nTable: {table}\n"
        schema_text += "Columns:\n"

        columns = df[
            df["table_name"] == table
        ]["column_name"]

        for col in columns:
            schema_text += f"{col}\n"


        schema_text += """

IMPORTANT DATABASE NOTES:

1. order_purchase_timestamp is stored as TEXT.
2. order_approved_at is stored as TEXT.
3. order_delivered_carrier_date is stored as TEXT.
4. order_delivered_customer_date is stored as TEXT.
5. order_estimated_delivery_date is stored as TEXT.

When using date functions:
- CAST date columns to TIMESTAMP first.

Example:

EXTRACT(
YEAR FROM CAST(order_purchase_timestamp AS TIMESTAMP)
)

DATE_TRUNC(
'month',
CAST(order_purchase_timestamp AS TIMESTAMP)
)
"""

    return schema_text
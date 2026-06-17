import csv
import os
from datetime import datetime


def log_query(
    question,
    sql,
    execution_time,
    rows_returned
):

    log_file = "logs/query_history.csv"

    file_exists = os.path.isfile(
        log_file
    )

    with open(
        log_file,
        mode="a",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        if not file_exists:

            writer.writerow([
                "timestamp",
                "question",
                "sql",
                "execution_time_seconds",
                "rows_returned"
            ])

        writer.writerow([
            datetime.now(),
            question,
            sql,
            execution_time,
            rows_returned
        ])
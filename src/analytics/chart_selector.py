def choose_chart(df):

    if len(df.columns) != 2:
        return "table"

    first_col = df.columns[0].lower()

    if (
        "date" in first_col
        or "month" in first_col
        or "year" in first_col
    ):
        return "line"

    return "bar"
       


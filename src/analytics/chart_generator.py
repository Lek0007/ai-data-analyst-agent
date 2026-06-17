import matplotlib.pyplot as plt


def create_bar_chart(df):

    x_col = df.columns[0]
    y_col = df.columns[1]

    plt.figure(figsize=(10, 5))

    plt.bar(
        df[x_col].astype(str),
        df[y_col]
    )

    plt.xlabel(x_col)
    plt.ylabel(y_col)

    plt.title(
        f"{y_col} by {x_col}"
    )

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.show()

def create_line_chart(df):

    x_col = df.columns[0]
    y_col = df.columns[1]

    plt.figure(figsize=(10,5))

    plt.plot(
        df[x_col],
        df[y_col]
    )

    plt.title(
        f"{y_col} over {x_col}"
    )

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.show()
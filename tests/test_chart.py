import pandas as pd

from chart_generator import create_bar_chart

data = {
    "state": ["SP", "RJ", "MG"],
    "revenue": [100, 80, 60]
}

df = pd.DataFrame(data)

create_bar_chart(df)
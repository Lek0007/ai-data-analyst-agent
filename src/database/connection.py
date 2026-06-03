from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://postgres:das21077@localhost:5432/ecommerce_analytics"
)

'''try:
    with engine.connect() as conn:
        print("Database Connected!")
except Exception as e:
    print(e)'''
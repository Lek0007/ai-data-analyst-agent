from database.schema_extractor import extract_schema

schema = extract_schema()

print(schema)

print("\n====================\n")
print("Length:", len(schema))
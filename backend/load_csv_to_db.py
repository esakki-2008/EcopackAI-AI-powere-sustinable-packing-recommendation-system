import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get full DATABASE_URL directly
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL not set!")

# Load CSV
df = pd.read_csv(
    r"D:/Project ecopackai/data/materials_module2_final.csv"
)

# Create engine using full URL
engine = create_engine(DATABASE_URL)

# Upload to PostgreSQL
df.to_sql("materials", engine, if_exists="replace", index=False)

print("✅ CSV imported into PostgreSQL successfully!")

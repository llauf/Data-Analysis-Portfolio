import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()
file_path = os.getenv("REPORT_PATH")
data_dir = os.getenv("DATA_DIR")

df = pd.read_csv(file_path)
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)
df.fillna("Not specified", inplace=True)
df['Expenses'] = df['Amount'].apply(lambda x: x if x < 0 else 0)
df['Income'] = df['Amount'].apply(lambda x: x if x >= 0 else 0)
df['Expenses'] = df['Expenses'].abs()
df = df.drop(['Amount', 'Currency', 'Original amount', 'Original Currency', 'Tags', 'User', 'Place'], axis=1)

#export
output_file_path = os.path.join(data_dir, '2_cleaned_data.csv')
df.to_csv(output_file_path, index=False)
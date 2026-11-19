
import argparse
import pandas as pd
from rich.console import Console
from rich.table import Table

# Accept the CSV file path
parser = argparse.ArgumentParser(
    description="Filter a CSV file and save the result."
)
parser.add_argument("csv_path", help="Path to the CSV file")
args = parser.parse_args()

# Read CSV data
df = pd.read_csv(args.csv_path)

# My own filter: CPU usage is 80 or higher
result = df[df["cpu"] >= 80]

# Create a Rich table
table = Table(title=f"Servers with CPU usage >= 80")

for col in result.columns:
    table.add_column(col)

for row in result.itertuples(index=False):
    table.add_row(*[str(value) for value in row])

Console().print(table)

# Save results to Excel
result.to_excel("result.xlsx", index=False)

print("Saved result.xlsx")

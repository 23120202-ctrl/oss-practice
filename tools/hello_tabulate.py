import argparse
from tabulate import tabulate

parser = argparse.ArgumentParser(description="My personal introduction tool")
parser.add_argument("--name", default="Student", help="Enter your name")
args = parser.parse_args()

print("Hello! Welcome to my Python tool.")
print("Created by Paul Sumit")

data = [
    ["Name", args.name],
    ["Student ID", "23120202"],
    ["Favorite Subject", "Python Programming"],
    ["Goal", "Learn Open Source Software"]
]

print(tabulate(data, headers=["Information", "Details"], tablefmt="grid"))
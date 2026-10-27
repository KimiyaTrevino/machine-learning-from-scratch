# Lesson 1: Open and inspect the public sleep dataset.
# Source: Bloomfield et al. (2024)
# https://doi.org/10.1371/journal.pdig.0000473

import csv
from pathlib import Path

# Find the CSV in the same folder as this Python script.
file_path = Path(__file__).parent / "Sleep Measures Data.csv"

# Open the CSV and read each row using its column names.
with open(file_path, newline="", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)
    columns = reader.fieldnames
    rows = list(reader)

# Show the size of our dataset
print("Number of rows:", len(rows))
print("Number of colmns:", len(columns))

# Show the column names.
print("\nColumn names:")
print(columns)

# Display a few vales from the first three records
print("\nFirst three records:")
for row in rows[:3]:
    print(
        "Participant:", row["id"],
        "Week:", row["week"],
        "Stress score:", row["pss"]
    )

# Collect each participant ID once.
participant_ids = {row["id"] for row in rows}

print("\nNumber of unique participants:", len(participant_ids))
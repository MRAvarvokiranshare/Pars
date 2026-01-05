import csv
import os

def collect_stats(csv_file="Evidence/reports.csv"):
    violations = {}
    try:
        with open(csv_file, encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                v = row["Violation"]
                violations[v] = violations.get(v, 0) + 1
    except FileNotFoundError:
        print("❌ فایل CSV پیدا نشد.")
        return []

    stats_table = [(v, count) for v, count in violations.items()]
    return stats_table

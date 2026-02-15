import csv

def csv_to_text(path: str) -> list:
    texts = []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            texts.append(" ".join(row))
    return texts

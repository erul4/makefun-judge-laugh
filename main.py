"""Write the bounty entry line to /output/entry.txt."""
from pathlib import Path

LINE = "I didn't break prod, I just gave it a surprise feature called downtime."

Path("/output").mkdir(parents=True, exist_ok=True)
Path("/output/entry.txt").write_text(LINE, encoding="utf-8")

print(LINE)

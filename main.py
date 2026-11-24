import os

LINE = "I didn't break prod, I just gave it a surprise feature called downtime."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)

print(LINE)

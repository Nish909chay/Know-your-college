import json

with open("/home/nish/Downloads/SE Project Data/VIT_fixed.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print("Total records:", len(data))
for i, entry in enumerate(data[:5]):
    print(f"Record {i}: keys = {list(entry.keys())}")

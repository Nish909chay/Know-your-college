import os
import json

input_dir = "/home/nish/Downloads/college_json"
output_dir = "/home/nish/Downloads/college_json/converted"

os.makedirs(output_dir, exist_ok=True)

for filename in os.listdir(input_dir):
    if filename.endswith(".json"):
        college_name = os.path.splitext(filename)[0]  # e.g. "bharatividyapeeth"
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, f"{college_name}_clean.jsonl")

        with open(input_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        with open(output_path, "w", encoding="utf-8") as out:
            for idx, entry in enumerate(data, start=1):
                converted = {
                    "college": college_name.upper(),   # or format properly
                    "source_file": entry.get("url", ""),
                    "doc_type": entry.get("type", ""),
                    "chunk_id": idx,
                    "content": entry.get("content", "")
                }
                out.write(json.dumps(converted, ensure_ascii=False) + "\n")

        print(f"Converted {filename} → {output_path}")

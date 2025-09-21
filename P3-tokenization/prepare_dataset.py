import json
import random

input_file = "college_documents_chunks_cleaned.jsonl"
train_file = "train.jsonl"
valid_file = "valid.jsonl"

# Split ratio
TRAIN_SPLIT = 0.9

# Load all chunks
with open(input_file, "r", encoding="utf-8") as f:
    data = [json.loads(line) for line in f]

# Shuffle for randomness
random.shuffle(data)

# Split
split_idx = int(len(data) * TRAIN_SPLIT)
train_data = data[:split_idx]
valid_data = data[split_idx:]

# Save train
with open(train_file, "w", encoding="utf-8") as f:
    for obj in train_data:
        # Convert into "instruction-style" format
        json.dump({
            "prompt": "You are a helpful assistant. Summarize the following college document:",
            "completion": obj["content"]
        }, f, ensure_ascii=False)
        f.write("\n")

# Save valid
with open(valid_file, "w", encoding="utf-8") as f:
    for obj in valid_data:
        json.dump({
            "prompt": "You are a helpful assistant. Summarize the following college document:",
            "completion": obj["content"]
        }, f, ensure_ascii=False)
        f.write("\n")

print(f"✅ Dataset prepared: {len(train_data)} train / {len(valid_data)} validation")


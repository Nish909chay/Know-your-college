import json
import random

input_file = "college_documents_chunks_cleaned.jsonl"
output_train = "college_train.jsonl"
output_val = "college_val.jsonl"

# Load all chunks
chunks = []
with open(input_file, "r", encoding="utf-8") as f:
    for line in f:
        obj = json.loads(line)
        if "content" in obj and obj["content"].strip():
            chunks.append(obj["content"].strip())

print(f"Loaded {len(chunks)} chunks")

# Shuffle for randomness
random.shuffle(chunks)

# Split train/val
split = int(0.9 * len(chunks))
train_chunks, val_chunks = chunks[:split], chunks[split:]

def make_record(text):
    return {
        "instruction": "Summarize the following project/internship document chunk:",
        "input": text,
        "output": "Summary not provided (to be learned during training)"  # placeholder
    }

# Write train
with open(output_train, "w", encoding="utf-8") as f:
    for t in train_chunks:
        f.write(json.dumps(make_record(t), ensure_ascii=False) + "\n")

# Write val
with open(output_val, "w", encoding="utf-8") as f:
    for v in val_chunks:
        f.write(json.dumps(make_record(v), ensure_ascii=False) + "\n")

print(f"✅ Summarization dataset prepared: {len(train_chunks)} train / {len(val_chunks)} val")


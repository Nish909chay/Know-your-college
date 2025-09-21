import json
import re

input_file = "4- all_final_data.jsonl"
output_file = "4- all_final_data_fixed.jsonl"

with open(input_file, 'r', encoding='utf-8') as f:
    data = f.read()

# Split objects by '}{' pattern (objects touching each other)
parts = re.split(r'\}\s*\{', data)

fixed_objects = []
for i, part in enumerate(parts):
    # Add braces back
    if i == 0:
        json_str = part + '}'
    elif i == len(parts) - 1:
        json_str = '{' + part
    else:
        json_str = '{' + part + '}'

    # Try parsing
    try:
        obj = json.loads(json_str)
        fixed_objects.append(obj)
    except json.JSONDecodeError as e:
        print(f"Skipping object {i+1} due to JSONDecodeError: {e}")

# Write proper JSONL
with open(output_file, 'w', encoding='utf-8') as f:
    for obj in fixed_objects:
        f.write(json.dumps(obj, ensure_ascii=False) + '\n')

print(f"Fixed JSONL saved to {output_file} with {len(fixed_objects)} objects.")


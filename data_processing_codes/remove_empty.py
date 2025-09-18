import json
import re

input_file = "/home/nish/Downloads/SE Project Data/VIT.json"
output_file = "/home/nish/Downloads/SE Project Data/VIT_fixed.json"

fixed_lines = []

with open(input_file, "r", encoding="utf-8") as f:
    for line in f:
        # Fix lines where "text": is not followed by a value
        line = re.sub(r'("text"\s*:\s*)([\n\r])', r'\1""\2', line)
        fixed_lines.append(line)

# Write fixed content to a new file
with open(output_file, "w", encoding="utf-8") as f:
    f.writelines(fixed_lines)

# Test if JSON loads now
try:
    with open(output_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    print(f"✅ JSON fixed successfully! {len(data)} records loaded.")
except json.JSONDecodeError as e:
    print(f"❌ JSON still invalid: {e}")

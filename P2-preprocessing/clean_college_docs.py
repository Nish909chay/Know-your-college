"""
import json
import re

input_file = "4- all_final_data.jsonl"
output_file = "4- all_final_data_cleaned.jsonl"

def clean_text(text):
    # Remove control characters and weird symbols
    text = re.sub(r'[\x0c\x0b\r]', '', text)

    # Normalize line breaks
    paragraphs = text.split('\n\n')  # split by paragraph
    cleaned_paragraphs = []
    for p in paragraphs:
        # Replace remaining line breaks inside paragraph with space
        p = p.replace('\n', ' ')
        # Collapse multiple spaces into one
        p = re.sub(r'\s+', ' ', p)
        # Strip leading/trailing spaces
        p = p.strip()
        if p:  # ignore empty paragraphs
            cleaned_paragraphs.append(p)
    
    # Rejoin paragraphs with double line break
    cleaned_text = '\n\n'.join(cleaned_paragraphs)

    # Optional: lowercase
    # cleaned_text = cleaned_text.lower()

    # Remove common page number patterns (e.g., "Page 1 of 10")
    cleaned_text = re.sub(r'Page\s+\d+\s+of\s+\d+', '', cleaned_text, flags=re.IGNORECASE)

    return cleaned_text.strip()

# Process JSONL
with open(input_file, 'r', encoding='utf-8') as fin, open(output_file, 'w', encoding='utf-8') as fout:
    for line in fin:
        obj = json.loads(line)
        if 'content' in obj and obj['content'].strip():
            obj['content'] = clean_text(obj['content'])
            # Optionally, skip if content becomes empty after cleaning
            if obj['content']:
                fout.write(json.dumps(obj, ensure_ascii=False) + '\n')

print(f"Cleaning complete. Output saved to {output_file}")

"""
import json
import re

input_file = "4- all_final_data_fixed.jsonl"
output_file = "college_documents_cleaned.jsonl"

def clean_text(text):
    if not text:
        return ""

    # Remove control characters and weird symbols
    text = re.sub(r'[\x0c\x0b\r]', '', text)

    # Normalize line breaks
    paragraphs = text.split('\n\n')  # split by paragraph
    cleaned_paragraphs = []
    for p in paragraphs:
        # Replace remaining line breaks inside paragraph with space
        p = p.replace('\n', ' ')
        # Collapse multiple spaces into one
        p = re.sub(r'\s+', ' ', p)
        # Strip leading/trailing spaces
        p = p.strip()
        if p:  # ignore empty paragraphs
            cleaned_paragraphs.append(p)
    
    # Rejoin paragraphs with double line break
    cleaned_text = '\n\n'.join(cleaned_paragraphs)

    # Optional: lowercase
    # cleaned_text = cleaned_text.lower()

    # Remove common page number patterns (e.g., "Page 1 of 10")
    cleaned_text = re.sub(r'Page\s+\d+\s+of\s+\d+', '', cleaned_text, flags=re.IGNORECASE)

    return cleaned_text.strip()


# Process JSONL
with open(input_file, 'r', encoding='utf-8') as fin, open(output_file, 'w', encoding='utf-8') as fout:
    for line in fin:
        try:
            obj = json.loads(line)
        except json.JSONDecodeError:
            # skip invalid JSON lines
            continue

        content = obj.get('content')
        if content:  # only process if content is not None or empty
            obj['content'] = clean_text(content)
            if obj['content']:
                fout.write(json.dumps(obj, ensure_ascii=False) + '\n')

print(f"Cleaning complete. Output saved to {output_file}")


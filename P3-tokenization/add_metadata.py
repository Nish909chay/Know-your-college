import json
import re

input_file = "college_documents_cleaned.jsonl"
output_file = "college_documents_enriched.jsonl"

def extract_year(filename):
    # Try to extract first 4-digit year from filename
    match = re.search(r'(20\d{2})', filename)
    if match:
        return int(match.group(1))
    return None

def categorize_doc_type(doc_type):
    doc_type = doc_type.lower()
    if "pdf" in doc_type or "doc" in doc_type:
        return "document"
    elif "xls" in doc_type or "sheet" in doc_type:
        return "spreadsheet"
    else:
        return "other"

with open(input_file, 'r', encoding='utf-8') as fin, open(output_file, 'w', encoding='utf-8') as fout:
    for line in fin:
        try:
            obj = json.loads(line)
        except json.JSONDecodeError:
            continue
        
        content = obj.get('content', '')
        obj['content_length'] = len(content)  # Number of characters

        source_file = obj.get('source_file', '')
        obj['year'] = extract_year(source_file)

        doc_type = obj.get('doc_type', '')
        obj['doc_type_category'] = categorize_doc_type(doc_type)

        fout.write(json.dumps(obj, ensure_ascii=False) + '\n')

print(f"Metadata enrichment complete. Output saved to {output_file}")


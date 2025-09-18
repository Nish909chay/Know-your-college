import json
import os

# 1. Input directory and output file
input_dir = "/home/nish/Downloads/SE Project Data/cleanData"
output_file = "/home/nish/Downloads/SE Project Data/cleanData/college_documents.jsonl"

# 2. Helper function to detect college and doc_type from filename
def parse_filename(filename):
    parts = filename.split('_')
    college = parts[0]
    if "pdf_docx" in filename:
        doc_type = "pdf/docx"
    elif "img_aspx_xlsx" in filename:
        doc_type = "img/aspx/xlsx"
    else:
        doc_type = "unknown"
    return college, doc_type

# 3. Merge all JSON files into one JSONL
with open(output_file, "w", encoding="utf-8") as out_f:
    for fname in os.listdir(input_dir):
        if fname.endswith(".json"):
            filepath = os.path.join(input_dir, fname)
            college, doc_type = parse_filename(fname)
            
            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
                for idx, entry in enumerate(data, start=1):
                    # Add metadata
                    enriched_entry = {
                        "college": college,
                        "source_file": entry.get("file"),
                        "doc_type": doc_type,
                        "chunk_id": idx,
                        "content": entry.get("content")
                    }
                    # Write as one line in JSONL
                    out_f.write(json.dumps(enriched_entry, ensure_ascii=False) + "\n")

print("✅ Merge complete! Output file:", output_file)

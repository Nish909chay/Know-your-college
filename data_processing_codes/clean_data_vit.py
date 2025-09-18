import os
import json
import re

def clean_text(text: str) -> str:
    if not text:
        return ""
    text = re.sub(r"\s+", " ", text)
    text = "".join(ch for ch in text if ch.isprintable())
    return text.strip()

def clean_pdf_docx(input_json, output_json):
    if not os.path.exists(input_json):
        print(f"❌ File not found: {input_json}")
        return

    with open(input_json, "r", encoding="utf-8") as f:
        raw_data = json.load(f)

    cleaned = []
    for entry in raw_data:
        cleaned.append({
            "file": entry.get("filename", entry.get("file", "")),
            "content": clean_text(entry.get("text", entry.get("content", "")))
        })

    with open(output_json, "w", encoding="utf-8") as f:
        json.dump(cleaned, f, ensure_ascii=False, indent=4)

    print(f"✅ Cleaned PDF/DOCX -> {output_json}")

def main():
    colleges = ["VIT"]
    base_path = "/home/nish/Downloads/SE Project Data"

    for college in colleges:
        input_json = os.path.join(base_path, f"{college}_fixed.json")
        output_json = os.path.join(base_path, f"{college}_pdf_docx_clean.json")
        clean_pdf_docx(input_json, output_json)

if __name__ == "__main__":
    main()

import os
import json
import re

# -----------------------
# Cleaning helper
# -----------------------

def clean_text(text: str) -> str:
    """Basic cleaning for messy PDF/DOCX extracted text."""
    if not text:
        return ""
    # Replace multiple newlines/tabs/spaces with single space
    text = re.sub(r"\s+", " ", text)
    # Remove stray non-printable characters
    text = "".join(ch for ch in text if ch.isprintable())
    # Trim
    return text.strip()

def clean_pdf_docx(input_json, output_json):
    if not os.path.exists(input_json):
        print(f"❌ File not found: {input_json}")
        return
    
    try:
        with open(input_json, "r", encoding="utf-8") as f:
            raw_data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"❌ JSON error in {input_json}: {e}")
        return

    cleaned = []
    for entry in raw_data:
        cleaned.append({
            "file": entry.get("file", ""),
            "content": clean_text(entry.get("content", ""))
        })
    
    with open(output_json, "w", encoding="utf-8") as f:
        json.dump(cleaned, f, ensure_ascii=False, indent=4)

    print(f"✅ Cleaned PDF/DOCX -> {output_json}")


# -----------------------
# Main
# -----------------------

def main():
    colleges = ["VIT_fixed"]  # update if you have other colleges
    base_path = "/home/nish/Downloads/SE Project Data"

    for college in colleges:
        input_json = os.path.join(base_path, f"{college}.json")
        output_json = os.path.join(base_path, f"{college}_pdf_docx_clean.json")
        clean_pdf_docx(input_json, output_json)

if __name__ == "__main__":
    main()

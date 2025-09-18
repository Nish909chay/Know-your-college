import os
import json
from PIL import Image
import pytesseract
import pandas as pd

# -----------------------
# Utility functions
# -----------------------

def read_image(file_path):
    try:
        img = Image.open(file_path)
        return pytesseract.image_to_string(img)
    except Exception as e:
        print(f"Error reading IMAGE: {file_path}, {e}")
        return None

def read_xlsx(file_path):
    try:
        dfs = pd.read_excel(file_path, sheet_name=None)
        text_blocks = []
        for sheet, df in dfs.items():
            text_blocks.append(f"--- {sheet} ---\n{df.to_string(index=False)}")
        return "\n".join(text_blocks)
    except Exception as e:
        print(f"Error reading XLSX: {file_path}, {e}")
        return None

def read_aspx(file_path):
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            return f.read()
    except Exception as e:
        print(f"Error reading ASPX: {file_path}, {e}")
        return None

# -----------------------
# Processing
# -----------------------

def process_files(college_path, output_json):
    records = []
    for root, _, files in os.walk(college_path):
        for file in files:
            ext = file.split(".")[-1].lower()
            if ext not in ["png", "jpg", "jpeg", "xlsx", "aspx"]:
                continue

            file_path = os.path.join(root, file)
            if ext in ["png", "jpg", "jpeg"]:
                text = read_image(file_path)
            elif ext == "xlsx":
                text = read_xlsx(file_path)
            elif ext == "aspx":
                text = read_aspx(file_path)
            else:
                continue

            if text:
                records.append({"file": file, "content": text})

    if records:
        with open(output_json, "w", encoding="utf-8") as f:
            json.dump(records, f, ensure_ascii=False, indent=4)
        print(f"✅ Saved {len(records)} docs in {output_json}")
    else:
        print(f"⚠ No image/aspx/xlsx files processed in {college_path}")

# -----------------------
# Main
# -----------------------

def main():
    colleges = ["VIT"]   # adjust to your actual folder names
    base = "./SE Project Data"   # adjust if needed

    for college in colleges:
        college_path = os.path.join(base, college)
        process_files(college_path, f"{college}_img_aspx_xlsx.json")

if __name__ == "__main__":
    main()

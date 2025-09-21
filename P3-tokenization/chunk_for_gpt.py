import json

input_file = "college_documents_enriched.jsonl"
output_file = "college_documents_chunks.jsonl"

CHARS_PER_TOKEN = 4
MAX_TOKENS = 1024
MIN_TOKENS = 256

def chunk_text(text, max_tokens=MAX_TOKENS, min_tokens=MIN_TOKENS):
    max_chars = max_tokens * CHARS_PER_TOKEN
    min_chars = min_tokens * CHARS_PER_TOKEN

    paragraphs = [p.strip() for p in text.split('\n\n') if p.strip()]
    chunks = []
    current_chunk = ""

    for p in paragraphs:
        while len(p) > max_chars:
            chunks.append(p[:max_chars])
            p = p[max_chars:]
        if len(current_chunk) + len(p) + 2 <= max_chars:
            if current_chunk:
                current_chunk += "\n\n" + p
            else:
                current_chunk = p
        else:
            if len(current_chunk) >= min_chars:
                chunks.append(current_chunk)
                current_chunk = p
            else:
                current_chunk += "\n\n" + p

    if current_chunk:
        chunks.append(current_chunk)

    return chunks

chunk_id_counter = 1

with open(input_file, 'r', encoding='utf-8') as fin, open(output_file, 'w', encoding='utf-8') as fout:
    for line in fin:
        try:
            obj = json.loads(line)
        except json.JSONDecodeError:
            continue
        content = obj.get('content', '')
        if not content.strip():
            continue
        text_chunks = chunk_text(content)
        for sub_chunk in text_chunks:
            new_obj = obj.copy()
            new_obj['content'] = sub_chunk
            new_obj['chunk_id'] = chunk_id_counter
            new_obj['content_length'] = len(sub_chunk)
            fout.write(json.dumps(new_obj, ensure_ascii=False) + "\n")
            chunk_id_counter += 1

print(f"Chunking complete. Output saved to {output_file}")


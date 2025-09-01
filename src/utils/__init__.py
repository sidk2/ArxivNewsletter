import time

def save_to_markdown(content: str, folder: str = ".") -> str:
    timestamp = int(time.time())
    file_path = f"{folder}/example_{timestamp}.md"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    return file_path
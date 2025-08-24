from langchain.tools import tool
import os

@tool("write_file", return_direct=True)
def write_file(data: str) -> str:
    """Write text to a file. Input format: 'path|text'"""
    try:
        if "|" not in data:
            return "❌ Input must be in format 'path|text'"
        path, text = data.split("|", 1)
        with open(path.strip(), "a", encoding="utf-8") as f:  # append instead of overwrite
            f.write(text.strip() + "\n")
        return f"✅ File written to {os.path.abspath(path.strip())}"
    except Exception as e:
        return f"❌ Error writing file: {str(e)}"


@tool("read_file", return_direct=True)
def read_file(path: str) -> str:
    """Read contents of a file. Input: the file path as string."""
    try:
        with open(path.strip(), "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        return f"❌ Error reading file: {str(e)}"

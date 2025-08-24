# backend/tools/python_sandbox.py
import sys, io, traceback
from langchain.tools import Tool

def run_python(code: str) -> str:
    # VERY limited sandbox; do not use exposed to untrusted users
    try:
        old_stdout = sys.stdout
        sys.stdout = io.StringIO()
        # restricted globals
        restricted_globals = {"__builtins__": {"print": print, "len": len, "range": range}}
        exec(code, restricted_globals, {})
        output = sys.stdout.getvalue()
        sys.stdout = old_stdout
        return output or "NO_OUTPUT"
    except Exception:
        sys.stdout = old_stdout
        return "ERROR:\n" + traceback.format_exc()

python_tool = Tool(
    name="run_python",
    func=run_python,
    description="Run small Python snippets (safe sandbox). Input: python code. Returns stdout or errors."
)

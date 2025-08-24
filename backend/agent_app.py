import os
from langchain_ollama import OllamaLLM
from langchain.agents import initialize_agent
from langchain.agents import AgentType

# Import your tools
from tools.search_tool import search_tool
from tools.email_tool import email_tool
from tools.file_tools import read_file, write_file

# Load env vars
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_APP_PASSWORD = os.getenv("EMAIL_APP_PASSWORD")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3")

# ✅ Initialize Ollama LLM
llm = OllamaLLM(model=OLLAMA_MODEL)

# ✅ Collect tools
tools = [search_tool, email_tool, read_file, write_file]

# ✅ Create the agent
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    handle_parsing_errors=True,  # prevents parsing errors from crashing
)

print("🚀 Agent ready! Type 'quit' to exit.")

while True:
    query = input(">> ")
    if query.lower() in ["quit", "exit"]:
        break
    try:
        result = agent.invoke({"input": query})
        print(result["output"])
    except Exception as e:
        print(f"❌ Error: {e}")

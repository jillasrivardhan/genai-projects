from langchain_ollama import ChatOllama

model = ChatOllama(
   model="qwen3:4b"
)

res = model.invoke("""
translate the sentence into mandarin,

what is your name.
""")

print(res.content)


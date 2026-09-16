
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser

model = ChatOllama(
   model="qwen3:4b",
   temperature=0.5
)

parser = StrOutputParser()

summary_prompt = PromptTemplate(
   template="create a  summary for this {topic} in 50 words",
   input_variables=['topic']
)

short_summary_prompt = PromptTemplate(
   template="create a short summary for this {text} in 50 words",
   input_variables=['text']
)

chain = summary_prompt | model | parser | short_summary_prompt | model | parser

response = chain.invoke({'topic':'blackhole'})

print(response)


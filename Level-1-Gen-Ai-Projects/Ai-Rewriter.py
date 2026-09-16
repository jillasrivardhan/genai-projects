from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser

model = ChatOllama(
   model="qwen2.5:3b",
   temperature=0.5
)

parser = StrOutputParser()

prompt  = PromptTemplate(
   template="""You are an expert AI text rewriter.

Your task is to rewrite the user's text according to the selected writing style.

Selected Style: {style}

Original Text:
{text}

Follow these rules:

1. Preserve the original meaning and intent.
2. Do not add new information or facts.
3. Correct grammar, spelling, punctuation, and awkward wording.
4. Keep the rewritten text natural and human-like.
5. Do not explain what you changed.
6. Return ONLY the rewritten text.

Style instructions:

- Professional:
  Use clear, polished, formal language suitable for workplaces, emails, reports, and professional communication.

- Casual:
  Use relaxed, natural, conversational language. Avoid unnecessary formality.

- Friendly:
  Use warm, positive, approachable language while keeping the original meaning.

- Academic:
  Use formal, objective, precise language suitable for academic writing. Avoid slang and unnecessary personal expressions.

- Simple English:
  Use short sentences and simple vocabulary that is easy for a non-native English speaker to understand.

Now rewrite the text according to the selected style."""
)

style = input("enter a style you want: ")
text = input("enter a text: ")

chain = prompt | model | parser

result = chain.invoke({'style':style,'text':text})

print(result)


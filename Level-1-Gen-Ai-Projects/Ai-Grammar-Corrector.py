from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field


# --------------------------------------------------
# Model
# --------------------------------------------------

model = ChatOllama(
    model="qwen2.5:3b",
    temperature=0
)


# --------------------------------------------------
# Pydantic Schema
# --------------------------------------------------

class Grammar(BaseModel):

    corrector: str = Field(
        description="The corrected sentence or text"
    )

    mistakes: list[str] = Field(
        description="List of mistakes found in the sentence"
    )

    explanation: str = Field(
        description="Explain the grammar mistakes and corrections"
    )

parser = PydanticOutputParser(
    pydantic_object=Grammar
)

user_input = input("Enter a sentence: ")

prompt = PromptTemplate(
    template="""
Correct the following sentence or text.

User input:
{user_input}

Return the result according to the following format instructions:

{format_instructions}
""",
    input_variables=["user_input"],
    partial_variables={
        "format_instructions": parser.get_format_instructions()
    }
)

chain = prompt | model | parser

result = chain.invoke({
    "user_input": user_input
})

print("\nCorrected Sentence:")
print(result.corrector)

print("\nMistakes:")
for mistake in result.mistakes:
    print("-", mistake)

print("\nExplanation:")
print(result.explanation)
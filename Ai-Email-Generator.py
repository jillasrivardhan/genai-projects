
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser,PydanticOutputParser
from pydantic import  BaseModel,Field

model = ChatOllama(
   model="qwen2.5:3b",
   temperature=0.5
)

class structure(BaseModel):
   name:list[str] = Field(description="extract the names from that.")
   purpose:str = Field(description="what is the purpose of that email")
   recipient:str = Field(description="who are you like professor,student,mother and more")
   tone:str = Field(description="in what tone he is conveying his message")

parser = PydanticOutputParser(pydantic_object=structure)

# output = model.with_structured_output(structure)

prompt = PromptTemplate(
    template="""
You are an assistant that extracts email information.

Extract the following information from the text:

{text}

{format_instructions}
""",
    input_variables=["text"],
    partial_variables={
        "format_instructions": parser.get_format_instructions()
    }
)

chain = prompt | model | parser

response = chain.invoke({
   'text':"""Hey Marcus,

As concerns of the crisis, we’re reaching out with a brief update to let you know how the E-Marketing is preparing and planning to provide uninterrupted support during this time. As a digital tool, E-marketing is not likely to be majorly affected by the current situation but our team is continuing to provide a best-in-class experience for E-marketing members:

Our staff is continuing to work normal business hours. Our team is carrying on normal business operating, and has the resources and tools they need to do their job from any location. We’re carefully monitoring and considering advice from government and health officials in the communities where our employees live and work, and we will continue to support our customers and normal business operations.

Our customer care team will continue to provide consistent and reliable support from 8AM-8PM EST 5 days a week. Technical support will also continue throughout this time.

We are pleased to offer a free webinar on How To Thrive During Tough Economic Times With Content Marketing on 12/12/2025. Members that sign up will receive a free 30 minute consultation marketing strategies. The weibinar will focus primarily on driving inbound traffic and leads to your site, with a specific focus on SEO strategies.

As a company and as individuals, we are committed to positive action during this time. We will continue to send updates if needed as the situation evolves. In the meantime, we encourage you to follow cdc.gov for the latest updates.

We hope you will join us and stay safe.

Best wishes,
lucy
Software Engineer"""
})

print(response)

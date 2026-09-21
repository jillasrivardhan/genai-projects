# 🤖 GenAI Projects with LangChain & Ollama

A collection of hands-on **Generative AI projects built with Python, LangChain, and Ollama**.

This repository is organized into progressive levels, starting with simple text-generation applications and moving toward more structured and practical GenAI applications such as **AI Code Explanation** and **Interview Question Generation**.

The goal of this repository is to learn how to build real-world GenAI applications using **local Large Language Models (LLMs)** and LangChain components.

---

## 🚀 Repository Overview

This repository contains projects divided into two learning levels:

| Level      | Focus                           |       Projects |
| ---------- | ------------------------------- | -------------: |
| 🟢 Level 1 | Beginner GenAI Applications     |              5 |
| 🟡 Level 2 | Intermediate GenAI Applications |              2 |
| **Total**  |                                 | **7 Projects** |

### Level 1

* 📧 AI Email Generator
* ✍️ AI Grammar Corrector
* 🔄 AI Text Rewriter
* 📝 AI Text Summarizer
* 🌐 AI Text Translator

### Level 2

* 💻 AI Code Explainer
* 🎯 Interview Q&A Generator

---

# 🎯 Learning Objectives

By completing these projects, you will learn how to:

* Work with local LLMs using Ollama
* Integrate Ollama with LangChain
* Create prompts using `PromptTemplate`
* Build LangChain chains
* Use `StrOutputParser`
* Use `PydanticOutputParser`
* Create structured AI outputs
* Validate LLM responses using Pydantic
* Control LLM behavior using temperature
* Build multi-step chains
* Generate structured interview questions
* Create reusable prompt templates
* Understand practical GenAI application architecture

---

# 🧠 Technologies Used

| Technology              | Purpose                      |
| ----------------------- | ---------------------------- |
| 🐍 Python               | Programming language         |
| 🦜 LangChain            | LLM application framework    |
| 🦙 Ollama               | Local LLM runtime            |
| 🤖 Qwen 2.5             | Local LLM used in projects   |
| 🤖 Qwen 3               | Local LLM used in projects   |
| 📦 Pydantic             | Structured output validation |
| 🔧 PromptTemplate       | Prompt creation              |
| 📤 StrOutputParser      | String response parsing      |
| 📋 PydanticOutputParser | Structured response parsing  |

---

# 🏗️ Project Architecture

The projects follow a simple LangChain pipeline:

```text
                User Input
                    │
                    ▼
             PromptTemplate
                    │
                    ▼
                ChatOllama
                    │
                    ▼
              Output Parser
                    │
                    ▼
              Final Response
```

For structured-output applications:

```text
                User Input
                    │
                    ▼
             PromptTemplate
                    │
                    ▼
                ChatOllama
                    │
                    ▼
          PydanticOutputParser
                    │
                    ▼
          Validated Pydantic Object
                    │
                    ▼
              Final Output
```

---

# 📂 Project Structure

```text
genai-projects/
│
├── Level-1-Gen-Ai-Projects/
│   │
│   ├── Ai-Email-Generator.py
│   ├── Ai-Grammar-Corrector.py
│   ├── Ai-Rewriter.py
│   ├── Ai-Text-Summarizer.py
│   └── Ai-Text-Translator.py
│
├── Level-2-Gen-Ai-Projects/
│   │
│   ├── Ai-Code-Explainer.py
│   ├── Interview-QA-Generator.py
│   └── prompt.py
│
├── requirements.txt
└── .env
```

---

# 🟢 Level 1 — Beginner GenAI Projects

Level 1 focuses on fundamental GenAI concepts.

These projects are intentionally simple so that beginners can understand how:

```text
Prompt → LLM → Output
```

works before moving into structured and multi-step applications.

---

# 📧 1. AI Email Generator

### File

```text
Level-1-Gen-Ai-Projects/Ai-Email-Generator.py
```

### Description

This project demonstrates how an LLM can analyze an email and extract structured information from it.

The application uses **Pydantic** to define the expected output.

### Extracted Information

The project extracts:

* Names
* Email purpose
* Recipient
* Tone

### Architecture

```text
Email Text
    │
    ▼
PromptTemplate
    │
    ▼
Qwen 2.5
    │
    ▼
PydanticOutputParser
    │
    ▼
Structured Email Information
```

### Example Output

```text
Name:
Lucy

Purpose:
Provide an update about company operations.

Recipient:
Customer / Member

Tone:
Professional
```

### Concepts Learned

* `PromptTemplate`
* `ChatOllama`
* `Pydantic`
* `PydanticOutputParser`
* Structured LLM output
* Prompt variables

---

# ✍️ 2. AI Grammar Corrector

### File

```text
Level-1-Gen-Ai-Projects/Ai-Grammar-Corrector.py
```

### Description

An AI-powered grammar correction application that analyzes user-provided text and returns a structured response.

### Features

* Corrects grammar
* Identifies mistakes
* Explains corrections
* Returns structured output

### Output Structure

```text
Corrected Sentence
        │
        ├── Mistakes
        │
        └── Explanation
```

### Example

Input:

```text
He go to school every day.
```

Possible output:

```text
Corrected:
He goes to school every day.

Mistakes:
- Subject-verb agreement

Explanation:
"Go" should be changed to "goes" because the subject
"He" is third-person singular.
```

### Concepts Learned

* Pydantic models
* Fields
* Output validation
* Structured responses
* User input handling

---

# 🔄 3. AI Text Rewriter

### File

```text
Level-1-Gen-Ai-Projects/Ai-Rewriter.py
```

### Description

This application rewrites text according to a selected writing style while preserving the original meaning.

### Supported Styles

The project prompt supports:

* Professional
* Casual
* Friendly
* Academic
* Simple English

### Workflow

```text
Original Text
      │
      ▼
Select Writing Style
      │
      ▼
PromptTemplate
      │
      ▼
Qwen 2.5
      │
      ▼
Rewritten Text
```

### Example

Input:

```text
Hey, I wanted to tell you that the meeting is moved.
```

Style:

```text
Professional
```

Output:

```text
I would like to inform you that the meeting has been rescheduled.
```

### Concepts Learned

* Prompt engineering
* Style-controlled generation
* `StrOutputParser`
* Prompt variables
* Preserving user intent

---

# 📝 4. AI Text Summarizer

### File

```text
Level-1-Gen-Ai-Projects/Ai-Text-Summarizer.py
```

### Description

This project demonstrates a **multi-step LangChain chain** for generating summaries.

It uses:

```text
Prompt → Model → Parser → Prompt → Model → Parser
```

### Architecture

```text
Topic
 │
 ▼
Summary Prompt
 │
 ▼
Qwen 3
 │
 ▼
First Summary
 │
 ▼
Short Summary Prompt
 │
 ▼
Qwen 3
 │
 ▼
Final Summary
```

### Concepts Learned

* Multiple `PromptTemplate` objects
* Sequential processing
* Chain composition
* `StrOutputParser`
* Multi-step LLM workflows

---

# 🌐 5. AI Text Translator

### File

```text
Level-1-Gen-Ai-Projects/Ai-Text-Translator.py
```

### Description

A simple translation application using a local Ollama model.

The example demonstrates sending a translation instruction directly to the LLM.

### Workflow

```text
English Text
     │
     ▼
Translation Prompt
     │
     ▼
Qwen 3
     │
     ▼
Translated Text
```

### Example

Input:

```text
What is your name?
```

Target language:

```text
Mandarin
```

Output:

```text
你叫什么名字？
```

### Concepts Learned

* Direct LLM invocation
* Translation prompting
* `ChatOllama`
* Model responses

---

# 🟡 Level 2 — Intermediate GenAI Projects

Level 2 introduces more practical applications and structured generation.

These projects move beyond simple text generation into applications involving:

* Reusable prompts
* Complex instructions
* Structured output
* Pydantic validation
* Multi-field generation
* Domain-specific generation

---

# 💻 6. AI Code Explainer

### File

```text
Level-2-Gen-Ai-Projects/Ai-Code-Explainer.py
```

Supporting prompt:

```text
Level-2-Gen-Ai-Projects/prompt.py
```

### Description

An AI programming assistant that explains source code according to the user's selected programming language and explanation level.

### Inputs

The application accepts:

```text
Programming Language
Explanation Level
Code
```

### Explanation Levels

#### Beginner

Designed for users with limited programming experience.

Focuses on:

* Basic terminology
* Simple explanations
* Programming fundamentals
* Easy-to-understand examples

#### Intermediate

Focuses on:

* Program logic
* Execution flow
* Functions
* Data structures
* Implementation details

#### Advanced

Focuses on:

* Algorithms
* Architecture
* Performance
* Complexity
* Edge cases
* Design decisions

### Response Structure

The prompt instructs the model to generate:

```text
1. What This Code Does
2. How It Works
3. Code Breakdown
4. Important Concepts
5. Example
6. Complexity
7. Potential Issues
8. Possible Improvements
```

### Architecture

```text
Programming Language
        │
        ▼
Explanation Level
        │
        ▼
      Code
        │
        ▼
 PromptTemplate
        │
        ▼
   Qwen 2.5
        │
        ▼
 StrOutputParser
        │
        ▼
 Detailed Explanation
```

### Concepts Learned

* Complex prompt engineering
* Reusable prompt files
* Dynamic prompt variables
* Code analysis
* LLM-based educational assistants
* Chain composition

---

# 🎯 7. Interview Q&A Generator

### File

```text
Level-2-Gen-Ai-Projects/Interview-QA-Generator.py
```

### Description

An AI-powered interview question generator that creates multiple-choice questions based on:

* Job role
* Experience
* Topic
* Difficulty

### User Inputs

```text
Role
Experience
Topic
Difficulty
```

Example:

```text
Role:
Python Developer

Experience:
2

Topic:
Python

Difficulty:
Medium
```

### Output

The application generates:

* Exactly 5 questions
* Exactly 4 choices per question
* One correct answer per question

### Pydantic Schema

The project defines:

```python
class Question(BaseModel):
    question: str
    choices: list[str]
    answer: str
```

and:

```python
class QA(BaseModel):
    questions: list[Question]
```

This provides a structured representation of the generated interview questions.

### Architecture

```text
Role
Experience
Topic
Difficulty
     │
     ▼
PromptTemplate
     │
     ▼
   Qwen 2.5
     │
     ▼
PydanticOutputParser
     │
     ▼
Validated QA Object
     │
     ▼
5 MCQs
```

### Example Output

```text
Question 1
--------------------------------------------------

Which keyword is used to define a function in Python?

Choices:
- function
- def
- define
- func

Correct Answer:
def
--------------------------------------------------
```

### Concepts Learned

* Pydantic models
* Nested Pydantic models
* Structured LLM output
* Output validation
* Dynamic prompts
* MCQ generation
* Prompt constraints

---

# 🧩 LangChain Concepts Used

## 1. ChatOllama

`ChatOllama` connects LangChain applications with models running through Ollama.

Example:

```python
from langchain_ollama import ChatOllama

model = ChatOllama(
    model="qwen2.5:3b",
    temperature=0
)
```

---

# 2. PromptTemplate

`PromptTemplate` allows you to create reusable prompts with variables.

Example:

```python
from langchain_core.prompts import PromptTemplate

prompt = PromptTemplate(
    template="Explain {topic}",
    input_variables=["topic"]
)
```

When invoked:

```python
prompt.invoke({
    "topic": "machine learning"
})
```

the variable is inserted into the prompt.

---

# 3. StrOutputParser

`StrOutputParser` converts the model response into a simple string.

Example:

```python
from langchain_core.output_parsers import StrOutputParser

parser = StrOutputParser()

chain = prompt | model | parser
```

This is useful when the application expects normal text.

---

# 4. PydanticOutputParser

`PydanticOutputParser` is used when the application expects structured data.

Example:

```python
from langchain_core.output_parsers import PydanticOutputParser

parser = PydanticOutputParser(
    pydantic_object=MySchema
)
```

The model is instructed to follow the schema and the parser validates the returned structure.

---

# 5. Pydantic

Pydantic allows you to define the structure of expected data.

Example:

```python
from pydantic import BaseModel, Field

class Grammar(BaseModel):

    corrector: str

    mistakes: list[str]

    explanation: str
```

This is especially useful for GenAI applications because LLMs naturally generate text, while applications often need predictable structured data.

---

# 🔗 6. LangChain Chains

One of the most useful concepts in these projects is chain composition.

For example:

```python
chain = prompt | model | parser
```

The output of one component becomes the input of the next.

```text
Prompt
  │
  ▼
Model
  │
  ▼
Parser
  │
  ▼
Output
```

The summarizer demonstrates a longer pipeline:

```text
Prompt
  ↓
Model
  ↓
Parser
  ↓
Prompt
  ↓
Model
  ↓
Parser
```

---

# 🦙 Why Ollama?

This repository uses Ollama because it allows LLMs to run locally.

Benefits include:

* Local inference
* No mandatory cloud API for these examples
* Better control over model usage
* Useful for experimentation
* Suitable for learning local LLM application development

The repository currently uses models such as:

```text
qwen2.5:3b
qwen3:4b
```

Model requirements depend on the specific model and quantization being used.

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/jillasrivardhan/genai-projects.git
```

Move into the project:

```bash
cd genai-projects
```

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv .venv
```

Activate it:

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

---

# 📦 3. Install Dependencies

```bash
pip install -r requirements.txt
```

The repository uses packages including:

```text
langchain
langchain-core
langchain-community
langchain-ollama
python-dotenv
```

---

# 🦙 4. Install Ollama

Install Ollama on your computer and verify that it is available:

```bash
ollama --version
```

Then pull the models used by the projects.

For Level 1 projects:

```bash
ollama pull qwen2.5:3b
```

and:

```bash
ollama pull qwen3:4b
```

Verify installed models:

```bash
ollama list
```

> You can replace these models with other compatible Ollama models by changing the `model=` value in the Python files.

---

# ▶️ Running the Projects

## Level 1

### AI Email Generator

```bash
python Level-1-Gen-Ai-Projects/Ai-Email-Generator.py
```

### AI Grammar Corrector

```bash
python Level-1-Gen-Ai-Projects/Ai-Grammar-Corrector.py
```

### AI Rewriter

```bash
python Level-1-Gen-Ai-Projects/Ai-Rewriter.py
```

### AI Text Summarizer

```bash
python Level-1-Gen-Ai-Projects/Ai-Text-Summarizer.py
```

### AI Text Translator

```bash
python Level-1-Gen-Ai-Projects/Ai-Text-Translator.py
```

---

# Level 2

### AI Code Explainer

```bash
python Level-2-Gen-Ai-Projects/Ai-Code-Explainer.py
```

### Interview Q&A Generator

```bash
python Level-2-Gen-Ai-Projects/Interview-QA-Generator.py
```

---

# 🔐 Environment Variables

A `.env` file is included in the project structure.

Keep secrets such as API keys and credentials out of Git repositories.

A recommended `.gitignore` entry is:

```gitignore
.env
.venv/
__pycache__/
*.pyc
```

Never commit private API keys, passwords, tokens, or other credentials.

---

# 🧪 Recommended Learning Path

If you are learning Generative AI from scratch, follow the projects in this order:

```text
                 GENAI LEARNING PATH
                         │
                         ▼
              ┌─────────────────────┐
              │ AI Text Translator  │
              └──────────┬──────────┘
                         ▼
              ┌─────────────────────┐
              │ AI Text Rewriter    │
              └──────────┬──────────┘
                         ▼
              ┌─────────────────────┐
              │ Grammar Corrector   │
              └──────────┬──────────┘
                         ▼
              ┌─────────────────────┐
              │ Text Summarizer     │
              └──────────┬──────────┘
                         ▼
              ┌─────────────────────┐
              │ Email Generator     │
              └──────────┬──────────┘
                         ▼
              ┌─────────────────────┐
              │ Code Explainer      │
              └──────────┬──────────┘
                         ▼
              ┌─────────────────────┐
              │ Interview Q&A       │
              └─────────────────────┘
```

---

# 📈 Skills Progression

## 🟢 Level 1

Learn:

```text
LLM Basics
   ↓
Prompting
   ↓
PromptTemplate
   ↓
ChatOllama
   ↓
String Output
   ↓
Structured Output
```

## 🟡 Level 2

Learn:

```text
Advanced Prompting
       ↓
Reusable Prompts
       ↓
Complex Instructions
       ↓
Pydantic Schemas
       ↓
Structured Generation
       ↓
Practical GenAI Applications
```

---

# 🔥 Future Improvements

These projects can be extended into more complete applications.

## UI Improvements

* Add Streamlit interfaces
* Add Gradio interfaces
* Add chat history
* Add downloadable results
* Add model selection

## LLM Improvements

* Allow users to select Ollama models
* Add configurable temperature
* Add streaming responses
* Add model availability checks

## Application Improvements

### AI Email Generator

* Generate complete emails
* Support different tones
* Add subject generation
* Add email templates

### Grammar Corrector

* Add grammar scoring
* Highlight corrections
* Support paragraphs
* Add language detection

### Text Rewriter

* Add custom writing styles
* Add length control
* Add tone control

### Summarizer

* Support PDFs
* Support long documents
* Add bullet-point summaries
* Add multiple summary lengths

### Translator

* Support multiple languages
* Add language selection
* Add automatic language detection

### Code Explainer

* Add file upload
* Support multiple programming languages
* Add code improvement suggestions
* Add bug detection
* Add complexity analysis

### Interview Q&A Generator

* Add difficulty filtering
* Add topic selection
* Add scoring
* Add explanations
* Build an interactive interview simulator

---

# 🚀 Ideas for Level 3

After completing these projects, you can move toward more advanced GenAI applications:

* 📚 RAG-based document chatbot
* 📄 PDF Question Answering
* 🤖 AI Agents
* 🧠 AI Memory Systems
* 🔎 Semantic Search
* 🗃️ Vector Databases
* 🧑‍💻 AI Coding Assistant
* 📊 AI Data Analyst
* 📝 Research Paper Assistant
* 🎓 AI Interview Platform
* 🔗 Multi-agent applications

A natural progression is:

```text
Basic LLM Apps
      ↓
LangChain Applications
      ↓
Structured Outputs
      ↓
RAG
      ↓
Agents
      ↓
Production GenAI Applications
```

---

# ⚠️ Common Issues

## Model Not Found

If you receive:

```text
model not found
```

check your installed models:

```bash
ollama list
```

Then pull the required model:

```bash
ollama pull qwen2.5:3b
```

---

## Ollama Connection Error

Make sure Ollama is installed and running.

Test:

```bash
ollama list
```

If the command works, the Ollama installation is generally available from the terminal.

---

## Pydantic Parsing Error

Structured-output projects may fail if the LLM returns data that does not match the expected schema.

For example, the Interview Q&A Generator expects:

```json
{
  "questions": [
    {
      "question": "Example question?",
      "choices": [
        "Choice A",
        "Choice B",
        "Choice C",
        "Choice D"
      ],
      "answer": "Choice A"
    }
  ]
}
```

If the model returns a schema definition instead of actual data, `PydanticOutputParser` will not be able to validate it.

This is a useful practical lesson when working with smaller local models: **structured-output prompting and validation are separate concerns from simply generating text.**

---

# 🧠 Key Takeaways

After completing this repository, you should understand how to:

```text
                    GenAI Application
                           │
             ┌─────────────┼─────────────┐
             ▼             ▼             ▼
           Prompt         Model        Parser
             │             │             │
             └─────────────┼─────────────┘
                           ▼
                        Output
```

More importantly, you will have practical experience with:

* Local LLMs
* Ollama
* LangChain
* Prompt engineering
* Prompt templates
* Chains
* String parsing
* Pydantic
* Structured outputs
* Multi-step generation
* Practical GenAI applications

---

# 🤝 Contributing

Contributions are welcome!

To contribute:

```bash
git clone <repository-url>
```

Create a branch:

```bash
git checkout -b feature/new-project
```

Make your changes, test them, and submit a Pull Request.

Ideas for contributions include:

* New GenAI projects
* Better prompts
* Streamlit interfaces
* Additional Ollama models
* Improved documentation
* Error handling
* Unit tests
* Advanced Level 3 projects

---

# 📄 License

This repository is intended for **educational and learning purposes**.

Third-party libraries, models, and other external resources may have their own licenses and terms of use. Review the applicable license before redistributing or deploying them.

---

# 👨‍💻 Author

**Jilla Srivardhan**

### Areas of Focus

* Generative AI
* LangChain
* Ollama
* Large Language Models
* RAG
* AI Agents
* Python
* Machine Learning

---

# ⭐ Support

If this repository helps you learn Generative AI and LangChain:

⭐ Star the repository
🍴 Fork it
🧑‍💻 Build your own projects
📚 Keep learning
🚀 Keep building

---

## 📌 Final Learning Roadmap

```text
Python
  │
  ▼
LLM Fundamentals
  │
  ▼
Prompt Engineering
  │
  ▼
Ollama
  │
  ▼
LangChain
  │
  ├── Models
  ├── Prompts
  ├── Chains
  └── Output Parsers
  │
  ▼
Structured Outputs
  │
  ▼
GenAI Projects
  │
  ▼
RAG
  │
  ▼
AI Agents
  │
  ▼
Production GenAI Applications
```

> **Learn the concept → Build a small project → Improve the project → Combine concepts → Build real-world AI applications.** 🚀

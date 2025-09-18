
# pip install langchain langchain-groq

# pip install biopython

#User → Retrieve Docs (PubMed API) → LLM → Reasoning / Summarization → Answer


from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from Bio import Entrez
import os
import ssl


# SSL workaround (bypass certificate errors)
ssl._create_default_https_context = ssl._create_unverified_context

# Set API keys
os.environ["GROQ_API_KEY"] = "API_KEY_HERE!!"
Entrez.email = "birkirorri@gmail.com"

# Initilize Groq llm 
llm = ChatGroq(model = "llama-3.3-70b-versatile")


# Get Pubmed extracts function

def call_pupmed(query, max_res = 3):
    handle = Entrez.esearch(db="pubmed", term=query, retmax=max_res)
    record = Entrez.read(handle)
    ids = record["IdList"]
    abstracts = []
    for id in ids:
        summary = Entrez.efetch(db="pubmed", id=id, rettype="abstract", retmode="text").read()
        abstracts.append(summary)
    return abstracts 

# Ask question
question_user = "Generative models and their use in single cell RNA data"
docs = call_pupmed("Gen models and scRNA data")


# Build prompt
context = "\n".join(docs)
prompt = f"""You are a bioinformatics assistant.
Here are some PubMed abstracts:
{context}

Now answer the user question: {question_user}
"""

answer = llm.predict(prompt)
print(answer)
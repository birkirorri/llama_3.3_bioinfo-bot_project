import os
from groq import Groq


#### Simple llm call#####

# The workflow here: User → Groq LLM → Answer



# Initialize the Groq client
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# Define the model and prompt
#model = "llama-3.3-70b-versatile"
#prompt = "Explain the importance of fast language models."

# Make the API call
#response = client.chat.completions.create(
#    messages=[{"role": "user", "content": prompt}],
#    model=model
#)

# Print the response
#print(response.choices[0].message.content)


def ask_llama(question):
    response = client.chat.completions.create(
        model = "llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": question}],
        max_tokens = 300
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    while True:
        q = input("Ask a bioinformatics question: ")
        if q.lower() in ["exit", "quit"]:
            break
        print("\nAnswer:", ask_llama(q), "\n")






import os
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

# 1. Load the environment variables
load_dotenv()

# 2. Get the API Key
api_key = os.getenv("gemini_api_key")

# 3. Initialize the Gemini Model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite", 
    google_api_key=api_key,
    temperature=0.7,
    max_output_tokens=100
)

# 4. The comparison text provided by user
question = """
In the early days of LangChain, we primarily used LLMs. Now, we almost exclusively use ChatModels. 
Think of it like this: an LLM is a solitary scholar who finishes your sentences, while a ChatModel is a strategist you can actually converse with.

Component    Input Type        Output Type        Analogy
LLMs =>            Pure String        Pure String        A typewriter that predicts the next word.
ChatModels=>    List of Messages    Message Object    A group chat where everyone has a specific role.

Based on the above, summarize the key difference in one sentence.
"""

# 5. Invoke the model
result = llm.invoke(question)
    
print("-" * 30)
print("RESPONSE:")
print(result.content) 
print("-" * 30)
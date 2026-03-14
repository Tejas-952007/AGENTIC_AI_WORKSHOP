import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_tavily import TavilySearch
from langchain_classic.agents import AgentExecutor, create_react_agent
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    temperature=0  # zero tempreture for logical consistency in agent
)

# 3.setup the senses (tavily tool)
# max _result= 3 keep the context clen and token-efficient
search_tool = TavilySearch( max_results=3,top_k_results=3)
tools = [search_tool]

# 4. the manual react prompt (the "alternative to hub")
template ="""Answer the following questions as best you can .you have acess to the following tools
{tools}
use the following formats:
question:the input question must answer 
thought:you should always think about what to do 
action: the action to take ,should be one of 
[{tool_names}]
Action Input: the input to the action 
observation: the result of the action 
...(the thought action and observation can repeat N times)
thought:i know the answer now
final answer: the final answer to the question

Begin!
Question:{input}
Thought:{agent_scratchpad}"""

custom_prompt = ChatPromptTemplate.from_template(template)

# construct the agent
# this combine this llm ,tools and our custom manual prompt
agent = create_react_agent(llm,tools,custom_prompt)

# 6.create the excutor (the runtime enviorment)
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,   # set to the true to see the agent's thought process
    handle_parsing_errors=True,   #handling minor llm formating slips 
    max_iterations=5   #safetly limit prevent infinate loops
)
# 7 excute a query 
query = "ehat is the curruent weather in pune and is it a good day for an outdoor trek?"
response = agent_executor.invoke({"input":query})
print(response["output"])
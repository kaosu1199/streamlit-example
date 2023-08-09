from langchain.llms import OpenAI
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.memory import ConversationBufferMemory

llm = OpenAI(openai_api_key = "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" , model_name="text-davinci-003", temperature=0.2)
tool_names = ["google-search"]
tools = load_tools(tool_names, llm=llm , google_api_key="AIzaSyAXpGFUZOkgf8-ZWhyoO539zBKFSRgFsSk" , google_cse_id = "f2ba75d17d5a04cf9")



memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True,
)

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

agent.run("""
現在の日本の総理大臣は誰ですか？
""")

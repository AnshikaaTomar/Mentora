import os
import logging
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate

os.environ["GRPC_VERBOSITY"] = "ERROR"
os.environ["GLOG_minloglevel"] = "2"
logging.getLogger("absl").setLevel(logging.ERROR)


GEMENI_API_KEY = os.environ['GOOGLE_API_KEY']

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",   
    temperature=0.7,
    google_api_key=GEMENI_API_KEY
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an AI assistant for Gautam Buddha University. "
               "Keep answers under 50 tokens. Sound natural and human."),
    ("human", "{user_query}")
])


async def call_llm(query: str) -> str:
    try:
        messages = prompt.format_messages(user_query=query)  
        response = await llm.ainvoke(messages)
        return response.content
    except Exception as err:
        return {"error": str(err)}      
       







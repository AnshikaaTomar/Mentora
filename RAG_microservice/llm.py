import os
import logging
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
<<<<<<< HEAD
from langchain.chains.llm import LLMChain
=======
from langchain.chains import LLMChain
>>>>>>> a2db6d4b40d4bdc98d0a52fc0223a5ee359a6668
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv
from debug_logger import log_error

load_dotenv()

os.environ["GRPC_VERBOSITY"] = "ERROR"
os.environ["GLOG_minloglevel"] = "2"
logging.getLogger("absl").setLevel(logging.ERROR)


GEMENI_API_KEY = os.getenv('GOOGLE_API_KEY')

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",   
    temperature=0.9,
    google_api_key=GEMENI_API_KEY
)

conversationMemory = ConversationBufferMemory(
    memory_key = 'chat_history',
    input_key="user_query",
    return_messages = False
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an AI assistant for Gautam Buddha University. "
               "Keep answers under 100 tokens. Sound natural and human."
               "If you do not know something you can politely be unaware of the answer."),
    ("system", "Conversation so far:\n{chat_history}"),
    ("system", "Here is some additional context you must use:\n{context}"),  
    ("human", "{user_query}")                             
])

chain = LLMChain(
    llm=llm,
    prompt=prompt,
    memory=conversationMemory,
    verbose=True
)


async def call_llm(query: str, context : str) -> str:
    try:
        response = await chain.apredict(user_query=query, context = context)
        return response
    except Exception as err:
        log_error(err)
        return {"error": str(err)}    
       







from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from ngrok_config import start_ngrok
from llm import call_llm
from hf_gemma import generate_embeddings

class userQuery(BaseModel):
    query: str

class facts(BaseModel):
    facts: list[str]


app = FastAPI()

@app.get("/callLLM/")
async def process_data(query: userQuery):
    llmResponse =await call_llm(query.query)
    return {
        "response":llmResponse
    }

@app.post("/getEmbeddings/")
def getEmbeddings(facts : facts):
    response = generate_embeddings(facts.facts)
    return {
        'embeddings' : response
    }


if __name__ == "__main__":
    public_url = start_ngrok()
    print(f"🚀 ngrok tunnel running on: {public_url}")
    uvicorn.run(app, host="0.0.0.0", port=8000)

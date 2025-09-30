import torch
from langchain_huggingface.embeddings import HuggingFaceEmbeddings


if torch.cuda.is_available():
    device = "cuda"
    gpu_name = torch.cuda.get_device_name(0)
    print(f"🔹 Running on: {device} ({gpu_name})")
else:
    device = "cpu"
    print(f"🔹 Running on: {device}")


model_name = "google/embeddinggemma-300m"


embedding_model = HuggingFaceEmbeddings(
    model_name=model_name,
    model_kwargs={"device": device},
    encode_kwargs={"batch_size": 16} 
)


texts = [
    "Gautam Buddha University was established in 2008.",
    "The campus is located in Greater Noida, Uttar Pradesh.",
    "Campus area is 511 acres."
]


def generate_embeddings(facts: list[str]):
    embeddings = embedding_model.embed_documents(facts)
    return embeddings

# Run it
#embeddings = generate_embeddings(texts)
#print(f"Generated embeddings shape: {len(embeddings)} x {len(embeddings[0])}")

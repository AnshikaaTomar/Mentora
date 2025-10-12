from getEmbeddings import generate_embeddings
from pinecone_config import index
import time
from debug_logger import log_error

start_time = time.time()

dummy_data = [
    "The School of Management at GBU is known for its MBA programs.",
    "The library at GBU is equipped with thousands of books, journals, and digital resources.",
    "GBU has separate hostels for boys and girls with modern facilities.",
    "The university conducts entrance examinations for various courses.",
    "GBU promotes research in areas like AI, data science, and renewable energy.",
    "The university has collaborations with several international institutions.",
    "GBU organizes annual cultural and technical festivals for students.",
    "The campus has sports facilities including cricket, football, and indoor stadiums.",
    "The official website of GBU provides information about admissions and courses.",
    "GBU emphasizes value-based education inspired by Buddhist principles.",
    "Scholarships are available for meritorious and financially weaker students.",
    "Gautam Buddha University has a website which is www.gbu.ac.in"
]

try:
    embeddings = generate_embeddings(dummy_data)

    to_upsert = []
    for i, text in enumerate(dummy_data):
        to_upsert.append({
            "id": f"gbu-{i}",              # unique ID
            "values": embeddings[i],
            "metadata": {"text": text},
        })

    index.upsert(vectors=to_upsert)
    print(f"Input: {len(dummy_data)}, Output: {len(embeddings)}")

    end_time = time.time()
    print(f"Execution time: {end_time - start_time:.2f} seconds")
except Exception as err:
    log_error(err)
    print(f"Error! :\n{err}")



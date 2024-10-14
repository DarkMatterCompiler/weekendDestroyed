import json
import torch
from transformers import AutoTokenizer, AutoModel
import faiss
import numpy as np

# Load the tokenizer and model for embeddings
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")
model = AutoModel.from_pretrained("distilbert-base-uncased")

# Sample JSON data
data = [
    {
        "query": "Who is the individual associated with the cryptocurrency industry facing a criminal trial on fraud and conspiracy charges, as reported by both The Verge and TechCrunch, and is accused by prosecutors of committing fraud for personal gain?",
        "answer": "Sam Bankman-Fried",
        "question_type": "inference_query",
        "evidence_list": [
            {
                "title": "The FTX trial is bigger than Sam Bankman-Fried",
                "author": "Elizabeth Lopatto",
                "url": "https://www.theverge.com/2023/9/28/23893269/ftx-sam-bankman-fried-trial-evidence-crypto",
                "source": "The Verge",
                "category": "technology",
                "published_at": "2023-09-28T12:00:00+00:00",
                "fact": "Before his fall, Bankman-Fried made himself out to be the Good Boy of crypto — the trustworthy face of a sometimes-shady industry."
            },
            {
                "title": "SBF’s trial starts soon, but how did he — and FTX — get here?",
                "author": "Jacquelyn Melinek",
                "url": "https://techcrunch.com/2023/10/01/ftx-lawsuit-timeline/",
                "source": "TechCrunch",
                "category": "technology",
                "published_at": "2023-10-01T14:00:29+00:00",
                "fact": "The highly anticipated criminal trial for Sam Bankman-Fried, former CEO of bankrupt crypto exchange FTX, started Tuesday to determine whether he’s guilty of seven counts of fraud and conspiracy."
            }
        ]
    },
    {
        "query": "Which individual is implicated in both inflating the value of a Manhattan apartment to a figure not yet achieved in New York City's real estate history, according to 'Fortune', and is also accused of adjusting this apartment's valuation to compensate for a loss in another asset's worth, as reported by 'The Age'?",
        "answer": "Donald Trump",
        "question_type": "inference_query",
        "evidence_list": [
            {
                "title": "Donald Trump defrauded banks with 'fantasy' to build his real estate empire, judge rules in a major repudiation against the former president",
                "author": "Michael R. Sisak, The Associated Press",
                "url": "https://fortune.com/2023/09/26/donald-trump-fraud-banks-insurers-real-estate-judge-new-york/",
                "source": "Fortune",
                "category": "business",
                "published_at": "2023-09-26T21:11:15+00:00",
                "fact": "No apartment in New York City has ever sold for close to that amount, James said."
            }
        ]
    },
    {
        "query": "Who is the figure associated with generative AI technology whose departure from OpenAI was considered shocking according to Fortune, and is also the subject of a prevailing theory suggesting a lack of full truthfulness with the board as reported by TechCrunch?",
        "answer": "Sam Altman",
        "question_type": "inference_query",
        "evidence_list": [
            {
                "title": "OpenAI's ex-chairman accuses board of going rogue in firing Altman: 'Sam and I are shocked and saddened by what the board did'",
                "author": "Matt O'Brien, The Associated Press",
                "url": "https://fortune.com/2023/11/18/how-did-openai-fire-sam-altman-greg-brockman-rogue-board/",
                "source": "Fortune",
                "category": "business",
                "published_at": "2023-11-18T15:33:09+00:00",
                "fact": "Altman’s exit “is indeed shocking as he has been the face of” generative AI technology."
            }
        ]
    },
]

# Function to embed text using DistilBERT
def embed_text(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        embeddings = model(**inputs).last_hidden_state.mean(dim=1).squeeze()
    return embeddings.numpy()

# Prepare embeddings and associated query types
embeddings = []
query_types = []

for item in data:
    query_embedding = embed_text(item['query'])
    embeddings.append(query_embedding)
    query_types.append(item['question_type'])

# Convert embeddings to a numpy array
embeddings = np.array(embeddings).astype('float32')

# Step 3: Store embeddings in FAISS
index = faiss.IndexFlatL2(embeddings.shape[1])  # Using L2 distance
index.add(embeddings)  # Add embeddings to the index

# Function to classify a new query
def classify_query(query):
    query_embedding = embed_text(query).reshape(1, -1)  # Reshape for FAISS
    D, I = index.search(query_embedding.astype('float32'), k=1)  # k=1 for nearest
    closest_index = I[0][0]  # Get the index of the closest match
    return query_types[closest_index]

# Example usage
if __name__ == "__main__":
    new_query = "Do the TechCrunch article on software companies and the Hacker News article on The Epoch Times both report an increase in revenue related to payment and subscription models, respectively?"
    query_type = classify_query(new_query)
    print(f"The query type for '{new_query}' is: {query_type}")

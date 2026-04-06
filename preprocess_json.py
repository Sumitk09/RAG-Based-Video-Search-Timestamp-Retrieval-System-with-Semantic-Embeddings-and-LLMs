'''
Requires: 
ollama serve 
ollama pull bge-m3
'''

import requests
import os
import json
import pandas as pd
import numpy as np
import joblib
from sklearn.metrics.pairwise import cosine_similarity

def create_embedding(text_list):
    r = requests.post("http://localhost:11434/api/embed", json={
            "model": "bge-m3",
            "input": text_list
        })

    embeddings = r.json()['embeddings']
    return embeddings

jsons = os.listdir("jsons")   # List all the jsons
my_dicts = []
chunk_id = 0

for json_text in jsons:
    # Step 1: Read JSON file
    with open(f"jsons/{json_text}", "r", encoding="utf-8") as f:
        content = json.load(f)

    print(f"Creating embeddings for {json_text}")
    embeddings = [c['text'] for c in content["chunks"]]
    embeddings = create_embedding(embeddings)
    # Step 2: Access chunks
    for i, chunk in enumerate(content["chunks"]):
        chunk['chunk_id'] = chunk_id
        chunk['embedding'] = embeddings[i]
        chunk_id += 1
        my_dicts.append(chunk)
        # if(i==5): break     # reading 5 chunks for texting 
    # break          # to run single file for fast processing
# print("My_DICT: ", my_dicts)

df = pd.DataFrame.from_records(my_dicts)
# SAVE THIS DATA_FRAME
joblib.dump(df, 'embeddings.joblib')
print("Generated embeddings.joblib file")

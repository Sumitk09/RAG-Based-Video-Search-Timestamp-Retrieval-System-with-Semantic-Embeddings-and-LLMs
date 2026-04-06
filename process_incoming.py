'''
Requires: 
ollama serve 
ollama pull llama3.2
'''

import pandas as pd
import numpy as np
import joblib
import requests
from sklearn.metrics.pairwise import cosine_similarity
from preprocess_json import create_embedding


# def create_embedding(text_list):
#     r = requests.post("http://localhost:11434/api/embed", json={
#             "model": "bge-m3",
#             "input": text_list
#         })

#     embeddings = r.json()['embeddings']
#     return embeddings

# model = "deepseek-r1:1.5b"            # ollama model 
def inference(prompt):
    r = requests.post("http://localhost:11434/api/generate", json={
            # "model": "deepseek-r1:1.5b",
            "model": "llama3.2",
            "prompt": prompt,
            "stream": False
        })
    
    response = r.json()
    print(response)
    return response

df = joblib.load('embeddings.joblib')


# print(df)
incoming_query = input("Ask a Question: ")
question_embedding = create_embedding([incoming_query])[0]
# print(question_embedding)

# Find similarities of question_embedding with other embeddings

# print(np.vstack(df['embedding'].values))
# print(np.vstack(df['embedding'].shape))
similarities = cosine_similarity(np.vstack(df['embedding']), [question_embedding]).flatten()
# print(similarities)
top_results = 3
max_index = similarities.argsort()[::-1][0: top_results]
# print(max_index)
new_df = df.loc[max_index]
# print(new_df[["title","number","text"]]) 


prompt = f'''I am working on e-commerce and reliance foundation presentation. Here are video's subtitle chunks containing video title, video number, start time in seconds, end time in seconds and the text at that time:

{new_df[["title","number", "start", "end", "text"]].to_json(orient="records")}
----------------------------------
"{incoming_query}"

User asked this question related to the video chunks, you have to answer where and how much content is taught in which video (in which video at what timestamp) and guide the user to go to that particular video. If user asks unrelated question, then reply that you can only answer questions related to the course. Don't ask asy question at the end, only answer the question.
'''

# Verifying first before sending to LLM
with open("prompt.txt", "w") as f:
    f.write(prompt)

response = inference(prompt)['response']
print(response)

with open("response.txt", "w") as f:
    f.write(response)

# for index, item in new_df.iterrows():
#     print(index, item['title'], item['number'], item['text'], item['start'], item['end'])
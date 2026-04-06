# 🎥 RAG-Based AI Video Understanding System

## 📌 Overview

This project solves a real-world problem:

> When we have hundreds of long videos (lectures, conferences, product demos), it becomes extremely difficult to find **where a specific topic is explained**.

### 💡 Solution

This system:

* Converts videos → audio
* Converts audio → text (Whisper)
* Splits text into chunks
* Creates embeddings using Ollama
* Uses cosine similarity to retrieve relevant content
* Answers user queries with **video timestamp guidance**

---

## 🧠 Example Output

```
Video #3 → Timestamp: 0.0s - 3.1s  
"Now let's talk about Reliance..."
```

---

## 🚀 Tech Stack

* Python
* OpenAI Whisper (Speech-to-Text)
* Ollama (LLM + Embeddings)
* Pandas / NumPy
* Scikit-learn (Cosine Similarity)
* FFmpeg

---

## 📂 Project Structure

```
project/
│
├── videos/              # Input videos
├── audios/              # Generated MP3 files
├── jsons/               # Transcript chunks
├── embeddings.joblib    # Stored embeddings
│
├── video_to_mp3.py
├── speech_to_text.py
├── preprocess_json.py
├── process_incoming.py
```

---

# ⚙️ REQUIRED SETUP (IMPORTANT)

---

## 🔹 1. Install Python (Recommended)

👉 Use Python **3.10 or 3.11** (avoid 3.13)

---

## 🔹 2. Install FFmpeg

### Windows:

* Download: https://ffmpeg.org/download.html
* Add to PATH

Check:

```
ffmpeg -version
```

---

## 🔹 3. Install Ollama

Download:
https://ollama.com

Start server:

```
ollama serve
```

---

## 🔹 4. Pull Required Models

```
ollama pull bge-m3
ollama pull llama3.2
```

---

# 🪟 WINDOWS SETUP (STEP-BY-STEP)

---

## 1. Clone Repository

```
git clone <your-repo-url>
cd project
```

---

## 2. Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate
```

---

## 3. Install Dependencies

```
pip install openai-whisper
pip install torch torchvision torchaudio
pip install pandas numpy scikit-learn joblib requests
```

---

## 4. Start Ollama

```
ollama serve
```

---

## 5. Pull Models

```
ollama pull bge-m3
ollama pull llama3.2
```

---

# 🍎 MAC SETUP

```
brew install ffmpeg
brew install python
```

```
python3 -m venv venv
source venv/bin/activate
pip install openai-whisper torch torchvision torchaudio pandas numpy scikit-learn joblib requests
```

```
brew install ollama
ollama serve
ollama pull bge-m3
ollama pull llama3.2
```

---

# 🐧 UBUNTU SETUP

```
sudo apt update
sudo apt install ffmpeg python3 python3-venv -y
```

```
python3 -m venv venv
source venv/bin/activate
pip install openai-whisper torch torchvision torchaudio pandas numpy scikit-learn joblib requests
```

```
curl -fsSL https://ollama.com/install.sh | sh
ollama serve
ollama pull bge-m3
ollama pull llama3.2
```

---

# ▶️ HOW TO RUN THE PROJECT

---

## Step 1: Convert Videos → Audio

```
python video_to_mp3.py
```

👉 Uses FFmpeg to extract audio

---

## Step 2: Audio → Text (Whisper)

```
python speech_to_text.py
```

👉 Generates JSON files in `/jsons`

---

## Step 3: Create Embeddings

```
python preprocess_json.py
```

👉 Creates:

```
embeddings.joblib
```

---

## Step 4: Ask Questions (RAG)

```
python process_incoming.py
```

👉 Input:

```
Ask a Question:
```

👉 Output:

* Video number
* Timestamp
* Relevant explanation

---

# 🧩 HOW IT WORKS (PIPELINE)

1. Whisper converts speech → English text
2. Text is split into chunks
3. Ollama generates embeddings (`bge-m3`)
4. User query → embedding
5. Cosine similarity finds top matches
6. LLM (`llama3.2`) generates answer

---

# 🧩 RESPONSE WILL BE SIMILAR TO THIS ( for question: Reliance vs other retailers?)

Based on the provided subtitle chunks, I found that the relevant information is located in Video #3.

The content related to "Reliance vs other retailers?" starts at timestamp 0.0 seconds and ends at 3.1 seconds. The text mentions: "Now let's talk about Reliance, whose plan has always been the same."

To find this section, you can navigate to Video #3 and start playing from the beginning (timestamp 0.0). The relevant information should be visible on screen.

If you need further assistance, feel free to ask!

---

# ⚠️ IMPORTANT NOTES

### ❗ Ollama must be running

If error:

```
Connection refused localhost:11434
```

Run:

```
ollama serve
```

---

### ❗ Model not found

```
ollama pull bge-m3
ollama pull llama3.2
```

---

### ❗ Whisper error

Install correct package:

```
pip install openai-whisper
```

---

# ⚠️ LIMITATIONS

* Not 100% accurate
* Depends on audio quality
* Works best with clear speech
* For faster execution better models can be considered other then **llama3.2** and **deepseek-r1**

---

# 🎯 USE CASES

* Lecture search
* Conference insights
* Product demo navigation
* Research content discovery

---

# ⭐ FINAL NOTE

This is a **production-level RAG pipeline foundation**
Highly useful for:

* Data Scientist roles
* GenAI projects
* Real-world ML systems

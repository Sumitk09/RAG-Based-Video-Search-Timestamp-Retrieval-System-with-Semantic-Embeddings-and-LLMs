# SPEECH TO TEXT AND STORING CHUNKS AFTER CREATION IN JOSN FILE
# speech_to_text

'''
Requires: 
pip install openai-whisper 
pip install torch
'''

import whisper
import json
import os

model = whisper.load_model("small")
# model = whisper.load_model("base")

audios = os.listdir("audios")  # fixed path

for audio in audios:
    print(audio)
    if "_" in audio:
        result = model.transcribe(
            f"audios/{audio}",   # fixed path
            task="translate",
            language="hi",
            word_timestamps=False,
            fp16=False
        )
        audio = audio[:-4]
        # number = audio.split(" #")[1].split(" ")[0]
        # title = audio.split(" #")[0]
        audio_name = audio[:-4]  # remove .mp3

        if "_" in audio_name:
            number = audio_name.split("_")[0]
            title = "_".join(audio_name.split("_")[1:])
        else:
            number = "unknown"
            title = audio_name

        chunks = []
        for segment in result["segments"]:
            chunks.append({
                "number": number,
                "title": title,
                "start": segment["start"],
                "end": segment["end"],
                "text": segment["text"]
            })

        chunk_with_metadata = {
            "chunks": chunks,
            "text": result["text"]
        }

        with open(f"jsons/{audio}.json", "w", encoding="utf-8") as f:
            json.dump(chunk_with_metadata, f, ensure_ascii=False, indent=4)

print("Speech to Text Completed...!!!")
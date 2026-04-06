import whisper
import json

model = whisper.load_model("small")
# converting only 1 video for testing
result = model.transcribe(audio="audios/1_Quick Commerce का Dark Store Exposed.mp3",
                          language= "hi",
                          task= "translate",        
                          word_timestamps=False)

# print(result["segments"])
chunks = []
for segment in result["segments"]:
    chunks.append({"start": segment["start"], "end": segment["end"], "text": segment["text"]})

print(chunks)
# write in JSON file
with open("jsons/output.json", "w") as f:
    json.dump(chunks, f)
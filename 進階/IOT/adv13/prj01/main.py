import whisper

model = whisper.load_model("base")
result = model.transcribe("C:/Users/markc/Desktop/python/進階/IOT/adv13/prj01/1.m4a")
print(result["text"])

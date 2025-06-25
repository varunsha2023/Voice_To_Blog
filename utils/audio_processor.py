import whisper

model = whisper.load_model("base")

def process_audio(filepath):
    result = model.transcribe(filepath)
    return result['text']

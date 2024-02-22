import os
import speech_recognition as sr
from pydub import AudioSegment

def transcribe_audio(file_path):
    # Convert
    audio = AudioSegment.from_wav(file_path)

    # Initialise
    recognizer = sr.Recognizer()

    # Export
    with audio.export("temp.wav", format="wav") as temp_wav:
        with sr.AudioFile("temp.wav") as source:
            # Load Audio
            audio_data = recognizer.record(source)

            try:
                text = recognizer.recognize_google(audio_data, language="de-DE")
                return text
            except sr.UnknownValueError:
                return "Sprache nicht verstanden."
            except sr.RequestError:
                return "Kann die Anfrage nicht bearbeiten."

# Path
folder_path = 'xxx/wav/'

# Folder
for filename in os.listdir(folder_path):
    if filename.endswith(".wav"):
        file_path = os.path.join(folder_path, filename)
        print(f"Transkribiere {filename}...")
        transcription = transcribe_audio(file_path)
        print(transcription)

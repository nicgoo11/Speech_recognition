import pandas as pd

# Path
file_path = 'xxx/output.txt'

speaker_info = {
    "03": "m31",
    "08": "f34",
    "09": "f21",
    "10": "m32",
    "11": "m26",
    "12": "m30",
    "13": "f32",
    "14": "f35",
    "15": "m25",
    "16": "f31"
}


emotion_info = {
    "A": "anger",
    "W": "anger",
    "B": "boredom",
    "L": "boredom",
    "D": "disgust",
    "E": "disgust",
    "F": "anxiety/fear",
    "H": "happiness",
  #  "F": "happiness / Freude",
    "S": "sadness",
    "T": "sadness",
    "N": "neutral"
}



text_info = {
    "a01": "Der Lappen liegt auf dem Eisschrank.",
    "a02": "Das will sie am Mittwoch abgeben.",
    "a04": "Heute abend könnte ich es ihm sagen.",
    "a05": "Das schwarze Stück Papier befindet sich da oben neben dem Holzstück.",
    "a07": "In 7 Stunden wird es soweit sein.",
    "b01": "Was sind denn das für Tüten, die da unter dem Tisch stehen?",
    "b02": "Sie haben es gerade hochgetragen und jetzt gehen sie wieder runter.",
    "b03": "An den Wochenenden bin ich jetzt immer nach Hause gefahren und habe Agnes besucht.",
    "b09": "Ich will das eben wegbringen und dann mit Karl was trinken gehen.",
    "b10": "Die wird auf dem Platz sein, wo wir sie immer hinlegen."
}

text_info



import re

# Funktion, um Übereinstimmung zu überprüfen und Satzzeichen zu ignorieren
def check_match(transcription, text_description):
    # Entfernen von Satzzeichen am Ende der Sätze
    transcription_clean = re.sub(r'[\.\,\?\!]+$', '', transcription).strip()
    text_description_clean = re.sub(r'[\.\,\?\!]+$', '', text_description).strip()

    return "Korrekt" if transcription_clean.lower() == text_description_clean.lower() else "Falsch"



# List
data = []

# Read data
with open(file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

for i in range(len(lines)):
    line = lines[i]
    # Is there a transcribition?
    if line.startswith("Transkribiere"):
        filename = line.split(" ")[1].strip().rstrip(':').replace('.wav', '')
        speaker = filename[:2]
        text_code = filename[2:5].lower()
        emotion = filename[5]
        # Here is the transciption
        transcription = lines[i + 1].strip() if i + 1 < len(lines) else ""
        text_description = text_info.get(text_code, "Unknown")
        match = check_match(transcription, text_description)
        data.append({
            "Dateiname": filename,
            "Transkription": transcription,
            "Textcode": text_code.upper(),  # Upper letter
            "Textbeschreibung": text_description,
            "Übereinstimmung": match,
            "Sprecher": speaker_info.get(speaker, "Unknown"),
            "Emotion": emotion_info.get(emotion, "Unknown")
        })

# Creat a dataframe
df = pd.DataFrame(data)

# Show a dataframe
print(df)

# Save it
df.to_csv('transcriptions_extended.csv', index=False)
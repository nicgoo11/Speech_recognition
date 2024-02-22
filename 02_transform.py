import pandas as pd

# Path
file_path = 'xxx/output.txt'

data = []

# Read
with open(file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

for i in range(len(lines)):
    line = lines[i]
    # Is there a transcribition?
    if line.startswith("Transkribiere"):
        filename = line.split(" ")[1].strip().rstrip(':').replace('.wav...', '') 

        # Nächste Zeile ist die Transkription
        transcription = lines[i + 1].strip() if i + 1 < len(lines) else ""
        data.append({"Dateiname": filename, "Transkription": transcription})

# Cread a dataframe
df = pd.DataFrame(data)

# Show the dataframe
print(df)

# Save it
df.to_csv('transcriptions.csv', index=False)


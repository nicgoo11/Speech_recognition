import pandas as pd
import numpy as np


# load csv
df = pd.read_csv('transcriptions_extended.csv', delimiter=',')

# Column for wrong and false transcription
df['Richtigkeit'] = np.where(df['Übereinstimmung'] == 'Korrekt', 1, 0)

# Table
sprecher_table = pd.crosstab(df['Sprecher'], df['Richtigkeit'])
emotion_table = pd.crosstab(df['Emotion'], df['Richtigkeit'])
textcode_table = pd.crosstab(df['Textcode'], df['Richtigkeit'])

# Function for the frequency
def print_frequencies(table, column_name):
    correct = table[table['Richtigkeit'] == 1][column_name].value_counts()
    incorrect = table[table['Richtigkeit'] == 0][column_name].value_counts()
    frequencies = pd.DataFrame({'Richtig': correct, 'Falsch': incorrect})
    print(f"Häufigkeiten für {column_name}:\n{frequencies}\n")

# How often the transcription is wrong?
print_frequencies(df, 'Sprecher')
print_frequencies(df, 'Emotion')
print_frequencies(df, 'Textcode')
import pandas as pd


# Loading data from a csv file

filepath = "morse_code.csv"
df = pd.read_csv(filepath)

# Creating dictionaries

text_to_morse = dict(zip(df["Character"], df["Code"]))
morse_to_text = {value: key for key, value in text_to_morse.items()}


# A function that converts text into Morse code

def text_to_morse_code(text):
    morse_code_result = ' '.join(text_to_morse.get(char, "") for char in text if char in text_to_morse)

    return morse_code_result

# A function that converts Morse code to text

def morse_code_to_text(morse_code):
    words = morse_code.split(" / ")
    decoded_words = []

    for word in words:
        decoded_word = ''.join(morse_to_text.get(code, "") for code in word.split())
        decoded_words.append(decoded_word)

    return ' '.join(decoded_words)

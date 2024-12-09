import pandas as pd


# Loading data from a csv file
filepath = "morse_code.csv"
df = pd.read_csv(filepath)

# Creating dictionaries
text_to_morse = dict(zip(df["Character"], df["Code"]))
morse_to_text = {value: key for key, value in text_to_morse.items()}


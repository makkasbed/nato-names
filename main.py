import pandas
df = pandas.read_csv("nato_phonetic_alphabet.csv")

# TODO 1. Create a dictionary in this format:
data = {row.letter: row.code for(index, row) in df.iterrows()}
#print(data)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
name = input("Please enter a word:").upper()

nato_names = []

for letter in name:
    nato_names.append(data[letter])

print(nato_names)





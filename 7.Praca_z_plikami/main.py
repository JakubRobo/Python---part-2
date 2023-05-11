from os import path
dir_path = path.dirname(__file__)
filename = "tekst.txt"
data_path = path.join(dir_path, filename)

with open(data_path, "r", encoding="utf-8") as f:
    file_lines = f.readlines()
    

def count_words(file_lines):
    text = text.replace(",", "").replace(".", "").replace("!", "").replace("?", "").replace(";", "")
    words = file_lines.split()
    word_count = len(words)
    return word_count


def word_ending_stats(text):

    text = text.replace(",", "").replace(".", "").replace("!", "").replace("?", "").replace(";", "")
    words = text.split()
    ending_stats = {}

    for word in words:
        if word:
            last_letter = word[-1].lower()
            if last_letter in ending_stats:
                ending_stats[last_letter] += 1
            else:
                ending_stats[last_letter] = 1
    return ending_stats

word_count = count_words(filename)
print("Liczba słów:", word_count)

ending_stats = word_ending_stats(filename)
print("Statystyki końcówek słów:")
for letter, count in ending_stats.items():
    print(f"Litera '{letter}': {count} słów")

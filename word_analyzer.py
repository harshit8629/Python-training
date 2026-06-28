text = input("Enter a paragraph:\n")

words = text.split()

word_count = len(words)

longest_word = max(words, key=len)

vowels = "aeiouAEIOU"

vowel_count = 0

for char in text:
    if char in vowels:
        vowel_count += 1

print("\nWord Count:", word_count)
print("Longest Word:", longest_word)
print("Vowel Count:", vowel_count)

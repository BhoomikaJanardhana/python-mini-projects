sentence = input("Enter a sentence: ")

print("Characters (with spaces):", len(sentence))
print("Characters (without spaces):", len(sentence.replace(" ", "")))

words = sentence.split()
print("Total words:", len(words))

print("UPPERCASE:", sentence.upper())
print("Reversed:", sentence[::-1])
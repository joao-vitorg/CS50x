"""Compute the Coleman-Liau formula"""

# Ask the text
text = input("Text: ")

# Calculate the grade
wordsLength = len(text.split(" "))
L = len([x for x in text if x.isalpha()]) / wordsLength * 100
S = len([x for x in text if x in ['.', '!', '?']]) / wordsLength * 100
grade = round(0.0588 * L - 0.296 * S - 15.8)

# Print the grade
if grade < 1:
    print("Before Grade 1")
elif grade > 16:
    print("Grade 16+")
else:
    print(f"Grade {grade}")

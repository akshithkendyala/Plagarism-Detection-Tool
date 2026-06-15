from plagiarism import calculate_similarity

text1 = "Python is a programming language"
text2 = "Python is a powerful programming language"

score = calculate_similarity(text1, text2)

print("Similarity:", score, "%")
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarity(text1, text2):

    docs = [text1, text2]

    vectorizer = TfidfVectorizer()

    matrix = vectorizer.fit_transform(docs)

    similarity = cosine_similarity(matrix)

    return round(similarity[0][1] * 100, 2)
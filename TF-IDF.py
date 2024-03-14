# Алгоритм вытягивания слов "TF-IDF"

from sklearn.feature_extraction.text import TfidfVectorizer

def read_text_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

def get_top_tfidf_words(text, top_n=100):
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform([text])
    words = tfidf_vectorizer.get_feature_names_out()
    tfidf_scores = zip(words, tfidf_matrix.toarray()[0])
    sorted_tfidf_scores = sorted(tfidf_scores, key=lambda x: x[1], reverse=True)[:top_n]
    return sorted_tfidf_scores

def main():
    file_path = input("Введите путь к текстовому файлу: ")
    text = read_text_from_file(file_path)
    top_words = get_top_tfidf_words(text)

    print(f"\nТоп {len(top_words)} важных слов в документе:")
    for term, score in top_words:
        print(f"{term}: {score}")

if __name__ == "__main__":
    main()
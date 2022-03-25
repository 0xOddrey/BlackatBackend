from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
count_vect = CountVectorizer()
from .models import *
#import the nltk package
import nltk

from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer


porter = PorterStemmer()

def generate_word_rec(word):
    all_words = WtfWord.objects.all()
    new_list = []

    for line in all_words:

        Document1 = porter.stem(line.name)
        Document2 = porter.stem(word)

        corpus = [Document1,Document2]
        X_train_counts = count_vect.fit_transform(corpus)
        vectorizer = TfidfVectorizer()
        trsfm=vectorizer.fit_transform(corpus)
        result = cosine_similarity(trsfm[0:1], trsfm)
        result = line.name,result[0][1]
        if result[1] > .10:
            new_list.append(result[0])

    new_list.sort(key=lambda x: x[1], reverse=True)
    if len(new_list) > 0:
        return(new_list[0])
    else:
        new_word = WtfWord.objects.all().order_by('?').first()
        return(new_word.name)
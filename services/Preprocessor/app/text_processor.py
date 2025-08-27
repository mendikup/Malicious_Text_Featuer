import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

import nltk

resources = [
    'stopwords',
    'punkt',
    'punkt_tab',
    'wordnet',
    'omw-1.4',
    'averaged_perceptron_tagger_eng'
]

for res in resources:
    try:
        nltk.data.find(res)
    except LookupError:
        nltk.download(res)



class TextProcessor:
    def __init__(self, txt):
        self.txt = txt

    def remove_stop_words(self):
        # Get English stopwords and tokenize
        stop_words = set(stopwords.words('english'))
        tokens = word_tokenize(self.txt.lower())

        # Remove stopwords
        filtered_tokens = [word for word in tokens if word not in stop_words]
        self.txt = " ".join(filtered_tokens)

    def lower_words(self):
        self.txt = self.txt.lower()

    def lemmatize_words(self):
        lemmatizer = WordNetLemmatizer()
        tokens = word_tokenize(self.txt)
        lemmatized_words = [lemmatizer.lemmatize(word) for word in tokens]
        self.txt = " ".join(lemmatized_words)


    def get_data(self):
        return self.txt

from nltk.corpus import stopwords, wordnet
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

import nltk

resources = {
    'stopwords': 'corpora/stopwords',
    'punkt': 'tokenizers/punkt',
    'punkt_tab': 'tokenizers/punkt_tab',
    'wordnet': 'corpora/wordnet',
    'omw-1.4': 'corpora/omw-1.4',
    'averaged_perceptron_tagger_eng': 'taggers/averaged_perceptron_tagger_eng',
    'vader_lexicon': 'sentiment/vader_lexicon',
}

# Download if missing
for name, path in resources.items():
    try:
        nltk.data.find(path)
    except LookupError:
        nltk.download(name)

# Force-load corpora to avoid LazyLoader bugs
_ = stopwords.words("english")
_ = wordnet.synsets("dog")  #ensure wordnet and OMW resources are loaded
lemmatizer = WordNetLemmatizer()
_ = lemmatizer.lemmatize("dogs")




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

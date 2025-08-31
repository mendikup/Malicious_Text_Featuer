import os
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import re
import pandas as pd


def load_black_list():
    """Load a list of weapons from a text file."""
    base_path = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(base_path, "weapons.txt")
    with open(path, mode="r", encoding="utf-8") as f:
        data = f.read()
    return data.splitlines()

# load black list once at module import
black_list = load_black_list()



class Analyzer:
    """Provide basic NLP utilities for enrichment."""

    @staticmethod
    def find_sentiment(txt) -> str:
        """Return sentiment label for *txt* using VADER."""

        score = SentimentIntensityAnalyzer().polarity_scores(txt)
        compound = score["compound"]
        if compound <= -0.5:
            return "negative"

        elif compound >= 0.5:
            return "positive"
        else:
            return "neutral"


    @staticmethod
    def detect_weapons(txt: str) -> list:
        """Return a list of weapon names found in *txt*."""
        weapons_detected = []
        for word in txt.lower().split():
            if word in black_list:
                weapons_detected.append(word)
        return weapons_detected


    @staticmethod
    def find_relevant_timestamp(txt):
        pattern = r"\d{1,2}[-/.]\d{1,2}[-/.]\d{2,4}|\d{4}-\d{2}-\d{2}"
        matches = re.findall(pattern ,txt)
        if matches:
            matches = pd.Series(matches)
            matches = pd.to_datetime(matches)
            return  str(matches.max())
        return ""



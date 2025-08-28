import os


def load_black_list():
    base_path = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(base_path, "weapons.txt")
    with open(path, mode="r", encoding="utf-8") as f:
        data = f.read()
    return data.splitlines()



class Analyzer:

    @staticmethod
    def find_sentiment(txt):
        return None

    @staticmethod
    def detect_weapons(txt: str) -> list:
        black_list = load_black_list()
        weapons_detected = []
        for word in txt.lower().split():
            if word in black_list:
                weapons_detected.append(word)
        return weapons_detected


    @staticmethod
    def find_relevant_timestamp(txt):
        return None

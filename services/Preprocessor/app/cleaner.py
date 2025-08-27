import re


class Cleaner:
    def __init__(self, row_data):
        self.row_data = row_data

    def remove_punctuation_and_special_characters(self):
        self.row_data = re.sub(r"[^a-zA-Z0-9\s]", "", self.row_data)
        self.row_data = self.row_data.strip()

    def remove_white_spaces(self):
        self.row_data = re.sub(r"\s+", " ", self.row_data)

    def get_data(self) -> str:
        return self.row_data
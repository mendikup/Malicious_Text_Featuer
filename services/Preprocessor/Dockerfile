FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN python -m nltk.downloader stopwords punkt wordnet omw-1.4 averaged_perceptron_tagger_eng

COPY . .

CMD ["python", "app/main.py"]

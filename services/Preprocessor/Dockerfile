

# Use a lightweight Python image
FROM python:3.11-slim

# Set the working directory for the service
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Download required NLTK resources
RUN python -m nltk.downloader stopwords punkt wordnet omw-1.4 averaged_perceptron_tagger_eng

# Copy application code into the image
COPY . .

# Run the service
CMD ["python", "app/main.py"]
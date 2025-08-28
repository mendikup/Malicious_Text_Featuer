
docker build -t avigoldshtein/retriever Retriever/
docker run --name retriever -d -e KAFKA_BOOTSTRAP=kafka:9092 -p 8000:8000 --network malicious-net avigoldshtein/retriever:latest


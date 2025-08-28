
docker build -t avigoldshtein/retriever Retriever/
docker run --name retriever -d -e KAFKA_BOOTSTRAP=kafka:9092 -p 8000:8000 --network malicious-net avigoldshtein/retriever:latest


docker build -t avigoldshtein/preprocessor Preprocessor/
docker run --name preprocessor -d -e KAFKA_BOOTSTRAP=kafka:9092 -p 8001:8001 --network malicious-net avigoldshtein/preprocessor:latest


docker build -t avigoldshtein/enricher Enricher/
docker run --name enricher -d -e KAFKA_BOOTSTRAP=kafka:9092 -p 8002:8002 --network malicious-net avigoldshtein/enricher:latest


docker build -t avigoldshtein/persister Persister/
docker run --name persister -d -e MONGO_URI=mongodb://mongo:27017 -e MONGO_DB=mydb -p 8003:8003 --network malicious-net avigoldshtein/persister:latest


docker build -t avigoldshtein/data-retrieval DataRetrieval/
docker run --name data-retrieval -d -p 8004:8004 --network malicious-net avigoldshtein/persister:latest



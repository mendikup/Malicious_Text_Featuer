@REM project flow run ################

@REM network creation
docker network create malicious-net

@REM volume for mongo
docker volume create malicious_mongo_data

@REM run kafka
docker run -d --name malicious-kafka --hostname kafka --network malicious-net -e KAFKA_CFG_NODE_ID=1 -e KAFKA_CFG_PROCESS_ROLES=broker,controller -e KAFKA_CFG_CONTROLLER_QUORUM_VOTERS=1@kafka:9093 -e KAFKA_CFG_LISTENERS=PLAINTEXT://:9092,CONTROLLER://:9093 -e KAFKA_CFG_ADVERTISED_LISTENERS=PLAINTEXT://kafka:9092 -e KAFKA_CFG_CONTROLLER_LISTENER_NAMES=CONTROLLER -e KAFKA_CFG_AUTO_CREATE_TOPICS_ENABLE=true -p 9092:9092 bitnami/kafka:3.7

@REM run mongo
docker run -d --name malicious-mongo --hostname mongo --network malicious-net -p 27017:27017 -v malicious_mongo_data:/data/db mongo:latest

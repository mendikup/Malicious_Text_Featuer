oc apply -f mongo-pvc.yaml

oc apply -f mongo-deployment.yaml

oc apply -f mongo-svc.yaml

oc apply -f kafka-deployment.yaml

oc apply -f kafka-svc.yaml
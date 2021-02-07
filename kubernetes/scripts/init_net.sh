#!/bin/bash

NET_ENVIRONMENT_PATH="./environment"
MINER_NODES_PATH="./nodes-config/web-test"

#Create minikube cluster
echo "Starting new minikube cluster, cpu="$1 "memory="$2
minikube start --cpus $1 --memory $2
eval $(minikube docker-env)

#Init blockchain
echo "Initializing blockchain network"
./blockchainit

#Create pods
echo "Initializing pods"
kubectl apply -f yaml/
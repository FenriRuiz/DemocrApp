#!/bin/bash

#Delete statefulset
kubectl delete statefulset geth-miner$1

#Delete service
kubectl delete svc miner$1-svc

#Delete volumeclaim
kubectl delete pvc volume-miner$1
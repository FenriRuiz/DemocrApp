#!/bin/bash

echo "Updating ethereum blockchain net..."
./blockchainit
kubectl apply -f yaml/
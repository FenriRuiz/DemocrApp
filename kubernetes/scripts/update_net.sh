#!/bin/bash

echo "Updating ethereum blockchain net..."
if [ $1 -ge "1" ]
then
  ./blockchainit
else
  ./update_net
fi

kubectl apply -f yaml/

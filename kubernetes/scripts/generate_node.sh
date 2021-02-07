#!/bin/bash

ETHERBASE="0x023e291a99d21c944a871adcc44561a58f99bdbc"
NEW_MINER_PATH="generated_files/new_miner.yaml"

echo "node:" > $NEW_MINER_PATH

name="prueba1"
echo "- $name:
    k8s:
      replicas: 1
    geth:
      Eth_Etherbase: "$ETHERBASE"
      Node_UserIdent: $name
      Node_DataDir: /etc/testnet/$name
      Node_HTTPPort: 8545
      Node_WSPort: 8546
      NodeP2P_ListenAddr: 30301
      NodeP2P_DiscoveryAddr: 30303" >> $NEW_MINER_PATH
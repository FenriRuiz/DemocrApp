#!/usr/bin/env python3
import argparse
import os
import yaml

SCRIPT_DESCRIPTION = "Script que permite crear/eliminar el cluster de minikube.\n"
SCRIPT_DESCRIPTION += "Además permite el escalado con la adición/eliminación de nodos en la red."

CREATE_ETHEREUM_NET_COMM    = "./scripts/init_net.sh"
DELETE_ETHEREUM_NET_COMM    = "./scripts/del_net.sh"
GENERATE_NOTE_COMM          = "./scripts/generate_node.sh"
UPDATE_ETHEREUM_NET_COMM    = "./scripts/update_net.sh"
DELETE_NODE_COMM            = "./scripts/del_node.sh"

ENVIRONMENT_YAML            = "./environment.yaml"

CPU_NUM     = "4"
RAM_SIZE    = "8192"

ETHEREUM_ACCOUNTS_ADDR = [
    "0xc11ba4c7c24f70e7a581c7daa92eac108099acec",
    "0x4c92786b90d848eaa3f4ef46918af724a309ae79",
    "0x4e7afbdc9413eeb582b3f1be49d652fa714484da",
    "0x021e6d4f8ea76ba6adef4f786b6d93d23a5a695b",
    "0xc61dc668ae0ae98d526e55448ae0d6e0728ad851",
    "0x1114758b568e96eff0819b9207572395b5a5a714",
    "0x9483e96a14e2ea3d25504b60bd3b54c74d392f39"
]

def set_parser():
    parser = argparse.ArgumentParser(description=SCRIPT_DESCRIPTION)
    parser.add_argument("-c", "--create", help="Inicializar la red de ethereum", action="store_true")
    parser.add_argument("-d", "--delete", help="Eliminar la red de ethereum", action="store_true")
    parser.add_argument("-a", "--add", help="Añadir un nodo a la red", action="store_true")
    parser.add_argument("-r", "--remove", help="Eliminar un nodo de la red", action="store_true")
    return parser

def get_miner_nodes():
    a_yaml_file = open(ENVIRONMENT_YAML, "r")
    parsed_yaml_file = yaml.load(a_yaml_file, Loader=yaml.FullLoader)
    a_yaml_file.close()

    return len(parsed_yaml_file['nodes'])

def add_miner_node_yaml(miner_num):
    a_yaml_file = open(ENVIRONMENT_YAML, "r")
    parsed_yaml_file = yaml.load(a_yaml_file, Loader=yaml.FullLoader)
    a_yaml_file.close()

    node_config = {
        f'miner{miner_num + 1}':
            {
                'k8s': {'replicas': 1},
                'geth':
                    {
                        'storage_size': 20,
                        'Eth_Etherbase': ETHEREUM_ACCOUNTS_ADDR[miner_num],
                        'Eth_Password': '123',
                        'Node_UserIdent': f'miner{miner_num + 1}',
                        'Node_DataDir': f'/etc/testnet/miner{miner_num + 1}', 
                        'Node_HTTPPort': 8545, 
                        'Node_WSPort': 8546, 
                        'NodeP2P_DiscoveryAddr': 30303, 
                        'Dashboard_Port': 8080, 
                        'Dashboard_Refresh': 3000000000
                    }
            }
    }

    parsed_yaml_file['nodes'].append(node_config)

    a_yaml_file = open(ENVIRONMENT_YAML, "w")
    yaml.dump(parsed_yaml_file, a_yaml_file)
    a_yaml_file.close()

def delete_miner_nn(miner_num):
    os.system(DELETE_NODE_COMM + " " + str(miner_num))
    print(f"Miner {miner_num} succesfully deleted!")

def delete_miner_node_yaml(miner_num):
    a_yaml_file = open(ENVIRONMENT_YAML, "r")
    parsed_yaml_file = yaml.load(a_yaml_file, Loader=yaml.FullLoader)
    a_yaml_file.close()

    del parsed_yaml_file['nodes'][miner_num - 1]

    a_yaml_file = open(ENVIRONMENT_YAML, "w")
    yaml.dump(parsed_yaml_file, a_yaml_file)
    a_yaml_file.close()

def get_pod_name(miner_num):
    return f"geth-miner{MINER_NODES}-0"

def create_ethereum_net():
    os.system(CREATE_ETHEREUM_NET_COMM + " " + CPU_NUM + " " + RAM_SIZE)

def delete_ethereum_net():
    os.system(DELETE_ETHEREUM_NET_COMM)

def add_node():
    miner_nodes = get_miner_nodes()
    add_miner_node_yaml(miner_nodes)
    os.system(UPDATE_ETHEREUM_NET_COMM)
    print(f"Node miner{miner_nodes + 1} added!")

def remove_node():
    miner_nodes = get_miner_nodes()
    if miner_nodes > 1:
        delete_miner_node_yaml(miner_nodes)
        os.system(UPDATE_ETHEREUM_NET_COMM)
        delete_miner_nn(miner_nodes)
    else:
        print("Cannot remove more miner nodes!")

if __name__ == '__main__':
    parser = set_parser()
    args = parser.parse_args()

    if args.create:
        create_ethereum_net()
    elif args.delete:
        delete_ethereum_net()
    elif args.add:
        add_node()
    elif args.remove:
        remove_node()
import argparse
import os

SCRIPT_DESCRIPTION = "Script que permite crear/eliminar el cluster de minikube.\n"
SCRIPT_DESCRIPTION += "Además permite el escalado con la adición/eliminación de nodos en la red."

CREATE_ETHEREUM_NET_COMM = "./init_blockchain_net.sh"
DELETE_ETHEREUM_NET_COMM = "./delete_blockchain_net.sh"

def set_parser():
    parser = argparse.ArgumentParser(description=SCRIPT_DESCRIPTION)
    parser.add_argument("-c", "--create", help="Inicializar la red de ethereum", action="store_true")
    parser.add_argument("-d", "--delete", help="Eliminar la red de ethereum", action="store_true")
    parser.add_argument("-a", "--add", help="Añadir un nodo a la red", action="store_true")
    parser.add_argument("-r", "--remove", help="Eliminar un nodo de la red", action="store_true")
    return parser

def create_ethereum_net():
    os.system(CREATE_ETHEREUM_NET_COMM)

def delete_ethereum_net():
    os.system(DELETE_ETHEREUM_NET_COMM)

def add_node():
    raise NotImplementedError

def remove_node():
    raise NotImplementedError

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
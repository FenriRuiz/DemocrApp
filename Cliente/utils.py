import json
from web3 import Web3

#getthenonce
#nonce=web3.eth.getTransactionCount(account_1)

#tx={
#'nonce':'',
#'to':account_2,
#'value':web3.toWei(1,'ether'),
#'gas':2000000,
#'gasPrice':web3.toWei('50','gwei')
#}

#signed_tx=web3.eth.account.signTransaction(tx,private_key)
#tx_hash=web3.eth.sendRawTransaction(signed_tx.rawTransaction)

#print(tx_hash)

url_eth = "http://127.0.0.1:7545/"
web3 = Web3(Web3.HTTPProvider(url_eth))

''' Clave publica del usuario, distinta para cada usuario'''
web3.eth.defaultAccount = "0x82Eca131B20Ee051086Cf817f0b0361DE1901a27"

''' Dirección del smart contract desplegado igual para todos los clientes'''
contract_address="0x2E892Eb3aE9B1837ca00A9F032517d899541C876"

with open("build\contracts\ListaVotaciones.json", "r") as read_file:    
    data = json.load(read_file)
contract = web3.eth.contract(address=contract_address, abi=data['abi'])

#contract = json.loads(ListaVotaciones.json)
# print(data)
# print(data['abi'])

# print(contract.functions.nuevaVotacion("Primera Encuesta").transact())
# print(contract.functions.getVotacion(1).call())
# print(contract.functions.sayHello().call())

# print(contract.functions.nuevaVotacion("Segunda Encuesta").transact())
# print(contract.functions.getVotacion(2).call())
# print(contract.functions.sayHello().call())

# print(contract.functions.getVotacion(2).call())

# print(contract.functions.agregarCandidato(1, "a").call())
# print(contract.functions.agregarCandidato(1, "b").call())
# print(contract.functions.agregarCandidato(1, "c").call())
# print(contract.functions.getCandidato(1, 0).call())

# print(contract.functions.agregarCandidato(1, "a").call())

def addEncuesta(titulo):
    return contract.functions.nuevaVotacion(titulo).transact()

def openEncuesta(numVotacion):
    return contract.functions.estadoVotacionAbierto(numVotacion).transact()

def closeEncuesta(numVotacion):
    return contract.functions.estadoVotacionCerrado(numVotacion).transact()

def addCandidatoEncuesta(numVotacion, candidato):
    return contract.functions.agregarCandidato(numVotacion, candidato).transact()

def getCandidatoEncuesta(numVotacion, numCandidato):
    return contract.functions.getCandidato(numVotacion, numCandidato).call()

def getListaEncuestas():
    numVotaciones = contract.functions.getNumVotaciones().call()
    i = 1
    listaEncuestas = []
    while i < numVotaciones:
        listaEncuestas.append(contract.functions.getVotacion(i).call())
        i += 1
    return listaEncuestas

def getEncuesta(numVotacion):
    return contract.functions.getVotacion(numVotacion).call()

def getListaCandidatosEncuesta(numVotacion):
    numCandidatos = contract.functions.getNumCandidatos(numVotacion).call()
    i = 0
    listaCandidatos = []
    while i < numCandidatos:
        listaCandidatos.append(contract.functions.getCandidato(numVotacion, i).call())
        i += 1
    return listaCandidatos

def setVotacion(numVotacion, numCandidato):
    return contract.functions.votar(numVotacion).transact()

def getResultadosEncuesta(numVotacion):
    return 
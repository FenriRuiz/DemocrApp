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
web3.eth.defaultAccount = "0x00740f0EBF7246d24d38A8D80BB60A13ABf8e2db"

print(web3.isConnected())
with open("build\contracts\ListaVotaciones.json", "r") as read_file:    
    data = json.load(read_file)

#contract = json.loads(ListaVotaciones.json)
print(data)
print(data['abi'])

address="0xB41B43a69281DD3193E3C103c3087910A04411B9"
contract = web3.eth.contract(address=address, abi=data['abi'])

print(contract.functions.nuevaVotacion("Primera Encuesta").transact())
print(contract.functions.getVotacion(1).call())
print(contract.functions.sayHello().call())

print(contract.functions.nuevaVotacion("Segunda Encuesta").transact())
print(contract.functions.getVotacion(2).call())
print(contract.functions.sayHello().call())

print(contract.functions.getVotacion(2).call())

print(contract.functions.agregarCandidato(1, "a").call())
print(contract.functions.agregarCandidato(1, "b").call())
print(contract.functions.agregarCandidato(1, "c").call())
print(contract.functions.getCandidato(1, 0).call())

print(contract.functions.agregarCandidato(1, "a").call())

def addEncuesta():
    return

def closeEncuesta():
    return

def openEncuesta():
    return

def addCandidatoEncuesta():
    return

def getListaEncuestas():
    return

def getEncuesta():
    return

def getResultadosEncuesta():
    return

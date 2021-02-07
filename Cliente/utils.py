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

url_eth = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(url_eth))
print(web3.isConnected())
with open("build\contracts\ListaVotaciones.json", "r") as read_file:
    data = json.load(read_file)
#contract = json.loads(ListaVotaciones.json)
print(data)
print(data['abi'])

address="0x890DA926A29BaBB690cEdec4fa406Abcd12E795e"
contract = web3.eth.contract(address=address, abi=data['abi'])

contract.functions.nuevaVotacion('Primera Encuesta')
print(contract.functions.getNumVotaciones())
contract.functions.nuevaVotacion('Segunda Encuesta')
print(contract.functions.getNumVotaciones())
print(contract.functions.getVotacion(1))
print(contract.functions.getVotacion(2))

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

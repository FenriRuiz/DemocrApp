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
abi = json.loads('[{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"constant":true,"inputs":[],"name":"numVotaciones","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"votaciones","outputs":[{"internalType":"uint256","name":"id_votacion","type":"uint256"},{"internalType":"string","name":"titulo","type":"string"},{"internalType":"address","name":"id_creador","type":"address"},{"internalType":"enumListaVotaciones.Estado","name":"estado","type":"uint8"},{"internalType":"uint256","name":"numCandidatos","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"string","name":"_titulo","type":"string"}],"name":"nuevaVotacion","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"numVotacion","type":"uint256"},{"internalType":"string","name":"candidato","type":"string"}],"name":"agregarCandidato","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"numVotacion","type":"uint256"}],"name":"estadoVotacionAbierto","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"numVotacion","type":"uint256"}],"name":"estadoVotacionCerrado","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"numVotacion","type":"uint256"},{"internalType":"uint256","name":"candidato","type":"uint256"}],"name":"votar","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"}]')
address="0x7aF2B11a315a7De42BE3A09f175f1916a817762a"
contract = web3.eth.contract(address=address, abi=abi)
numeroDeVotaciones = contract.functions.nuevaVotacion('nombreEncuesta').call()
print(numeroDeVotaciones)

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

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
web3.eth.defaultAccount = "0xC1fdfEb32072297b3fEB093D648A09cD2bF0e611"

''' Dirección del smart contract desplegado igual para todos los clientes'''
contract_address="0x35AA0f83DE1a260F67ECeecCfdDb2766570b4Aa1"

with open("build/contracts/ListaVotaciones.json", "r") as read_file:    
    data = json.load(read_file)
contract = web3.eth.contract(address=contract_address, abi=data['abi'])

#web3.eth.getTransactionReceipt(tx_hash)
def addEncuesta(titulo):
    try:
        contract.functions.nuevaVotacion(titulo).transact()
        print("Encuesta añadida: " + titulo)
    except:
        print("Error, al añadir la encuesta")
    return 
def openEncuesta(numVotacion):
    try:
        contract.functions.estadoVotacionAbierto(numVotacion).transact()
        print("Votación en estado: Abierta. Es votable")
    except:
        print("Error, votación continua en estado: Edicion")
    return 

def closeEncuesta(numVotacion):
    try:
        contract.functions.estadoVotacionCerrado(numVotacion).transact()
        print("Votación en estado: Cerrada.")
    except:
        print("Error, votación continua en estado: Abierta")
    return 

def addCandidatoEncuesta(numVotacion, candidato):
    try:
        contract.functions.agregarCandidato(numVotacion, candidato).transact()
        print("El candidado: " + candidato + ", ha sido añadido a la votación: " + str(numVotacion))
    except:
        print("Error, al añadir al candidado: " + candidato)
    return 

def getCandidatoEncuesta(numVotacion, numCandidato):
    print("El candidato seleccionado es: "+ contract.functions.getCandidato(numVotacion, numCandidato).call())
    return

def getListaEncuestas():
    numVotaciones = contract.functions.getNumVotaciones().call()
    i = 1
    listaEncuestas = []
    while i <= numVotaciones:
        listaEncuestas.append(contract.functions.getVotacion(i).call())
        i += 1

    print("Las encuestas creadas son: ")
    i = 1
    listaEncuestas.reverse()
    while i <= numVotaciones:
        print(str(i) + ".- " + listaEncuestas.pop())
        i += 1
    return

def getEncuesta(numVotacion):
    print("Encuesta "+ str(numVotacion) + ") " +contract.functions.getVotacion(numVotacion).call())
    print(getListaCandidatosEncuesta(numVotacion))
    print("El estado de la votación es: " + contract.functions.getEstadoEncuesta(numVotacion).call())
    return

def getListaCandidatosEncuesta(numVotacion):
    numCandidatos = contract.functions.getNumCandidatos(numVotacion).call()
    i = 0
    listaCandidatos = []
    while i < numCandidatos:
        listaCandidatos.append(contract.functions.getCandidato(numVotacion, i).call())
        i += 1
    i = 1
    print("Los candidatos son: ")
    listaCandidatos.reverse()
    while i <= numCandidatos:
        print(str(i)+".- " + str(listaCandidatos.pop()))
        i += 1
    return

def setVotacion(numVotacion, numCandidato):
    try:
        contract.functions.votar(numVotacion, numCandidato).transact()
        print("Votación realizada correctamente")
    except:
        print("Votación fallida")
    return 

def getResultadosEncuesta(numVotacion):

    numVotantes = contract.functions.getNumVotantesVotacion(numVotacion).call()
    votos = {}
    i = 0
    while i < numVotantes:
        votoEmitido = contract.functions.getVotoEmitido(numVotacion, i).call()
        if votos.get(votoEmitido) != 0:
            votos[votoEmitido] = 1
        else:
            incremento = int(votos.get(votoEmitido)) + 1
            votos[votoEmitido] = incremento
        i =+ 1

    for clave in votos:
        porcentaje = (int(votos.get(clave))/numVotacion)*100
        print("Votos para el candidato: " + str(clave) + "  -  " + str(porcentaje) +"%")
    return 
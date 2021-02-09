#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from web3 import Web3
import json

from cliente import *

URL_ETH = "http://127.0.0.1:7545/"

FIRST_CLI = "0xC1fdfEb32072297b3fEB093D648A09cD2bF0e611"
SECON_CLI = "0x083d31549e9B6CFB83F414C5f2a8361b148952F2"
THIRD_CLI = "0xe8C38A38dA3A082373638191F7106646D51F5727"

ENCUESTA = "Encuesta"

FIRST_CAND = "A"
SECON_CAND = "B"
THIRD_CAND = "C"
OTHER_CAND = "ERROR"

ESTADO_EDICION = "Editando"
ESTADO_ABIERTO = "Abierto"
ESTADO_CERRADO = "Cerrado"

CONTRACT_ADDRESS= "0x35AA0f83DE1a260F67ECeecCfdDb2766570b4Aa1"



class TestIntegration(unittest.TestCase):
    '''
    Tests de integracion
    '''

    def test_crear_encuesta(self):
        '''La votación se crea y se devuelve del servidor'''
        
        with open("build/contracts/ListaVotaciones.json", "r") as read_file:    
            data = json.load(read_file)

        cli_1 = Web3(Web3.HTTPProvider(URL_ETH))
        cli_1.eth.defaultAccount = FIRST_CLI
        contract_1 = cli_1.eth.contract(address=CONTRACT_ADDRESS, abi=data['abi'])
        
        contract_1.functions.nuevaVotacion(ENCUESTA).transact()
        self.assertEqual(ENCUESTA, contract_1.functions.getVotacion(1).call())

    def test_agregar_candidato(self):
        '''Sólo el propietario de la votación podrá añadir candidatos'''

        with open("build/contracts/ListaVotaciones.json", "r") as read_file:    
            data = json.load(read_file)

        cli_1 = Web3(Web3.HTTPProvider(URL_ETH))
        cli_1.eth.defaultAccount = FIRST_CLI
        contract_1 = cli_1.eth.contract(address=CONTRACT_ADDRESS, abi=data['abi'])
        contract_1.functions.agregarCandidato(1, FIRST_CAND).transact()
        contract_1.functions.agregarCandidato(1, SECON_CAND).transact()
        contract_1.functions.agregarCandidato(1, THIRD_CAND).transact()

        self.assertEqual(FIRST_CAND, contract_1.functions.getCandidato(1, 1).call())
        self.assertEqual(SECON_CAND, contract_1.functions.getCandidato(1, 2).call())
        self.assertEqual(THIRD_CAND, contract_1.functions.getCandidato(1, 3).call())

        cli_2 = Web3(Web3.HTTPProvider(URL_ETH))
        cli_2.eth.defaultAccount = SECON_CLI
        contract_2 = cli_2.eth.contract(address=CONTRACT_ADDRESS, abi=data['abi'])
        contract_2.functions.agregarCandidato(1, OTHER_CAND).transact()

        self.assertNotEqual(OTHER_CAND, contract_2.functions.getCandidato(1, 4).call())

    def test_abir_y_cerrar_encuesta(self):
        '''Solo el propietario de la votacion podrá abrir y cerrar la encuesta '''

        with open("build/contracts/ListaVotaciones.json", "r") as read_file:    
            data = json.load(read_file)

        cli_1 = Web3(Web3.HTTPProvider(URL_ETH))
        cli_1.eth.defaultAccount = FIRST_CLI
        contract_1 = cli_1.eth.contract(address=CONTRACT_ADDRESS, abi=data['abi'])
        
        self.assertEqual(ESTADO_EDICION, contract_1.functions.getEstadoEncuesta(1).call())
        contract_1.functions.estadoVotacionAbierto(1).transact()
        self.assertEqual(ESTADO_ABIERTO, contract_1.functions.getEstadoEncuesta(1).call())
        
        cli_2 = Web3(Web3.HTTPProvider(URL_ETH))
        cli_2.eth.defaultAccount = SECON_CLI
        contract_2 = cli_2.eth.contract(address=CONTRACT_ADDRESS, abi=data['abi'])
        
        contract_2.functions.estadoVotacionCerrado(1).transact()
        self.assertNotEqual(ESTADO_CERRADO, contract_2.functions.getEstadoEncuesta(1).call())
    
    def test_agregar_candidato_existente(self):
        '''Sólo el propietario de la votación podrá añadir candidatos'''

        with open("build/contracts/ListaVotaciones.json", "r") as read_file:    
            data = json.load(read_file)

        cli_1 = Web3(Web3.HTTPProvider(URL_ETH))
        cli_1.eth.defaultAccount = FIRST_CLI
        contract_1 = cli_1.eth.contract(address=CONTRACT_ADDRESS, abi=data['abi'])
        contract_1.functions.agregarCandidato(1, FIRST_CAND).transact()
        contract_1.functions.agregarCandidato(1, SECON_CAND).transact()
        contract_1.functions.agregarCandidato(1, THIRD_CAND).transact()

        self.assertNotEqual(FIRST_CAND, contract_1.functions.getCandidato(1, 4).call())
        self.assertNotEqual(SECON_CAND, contract_1.functions.getCandidato(1, 5).call())
        self.assertNotEqual(THIRD_CAND, contract_1.functions.getCandidato(1, 6).call())

    def test_votacion_unica(self):
        '''Un votante solo podrá votar una vez por votación '''

        with open("build/contracts/ListaVotaciones.json", "r") as read_file:    
            data = json.load(read_file)

        cli_1 = Web3(Web3.HTTPProvider(URL_ETH))
        cli_1.eth.defaultAccount = FIRST_CLI
        contract_1 = cli_1.eth.contract(address=CONTRACT_ADDRESS, abi=data['abi'])

        contract_1.functions.votar(1, 1).transact()
        self.assertEqual(1, contract_1.functions.getNumVotantesVotacion(1).call())
        contract_1.functions.votar(1, 2).transact()
        self.assertEqual(1, contract_1.functions.getNumVotantesVotacion(1).call())

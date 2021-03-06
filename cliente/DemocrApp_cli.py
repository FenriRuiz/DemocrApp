import cmd
from web3 import Web3
from utils import *

class DemocrappShell(cmd.Cmd):
    intro = 'Bienvenido a la terminal de DemocrApp.   Escribe help o ? para ver la lista de opciones.\n'
    prompt = 'DemocrApp > '
    file = None

    def do_crearEncuesta(self, arg):
        '''Crea una nueva encuesta vacía: \ncrearEncuesta "Nombre de la encuesta"'''
        addEncuesta(arg)

    def do_verEncuesta(self, arg):
        '''Muestra la información de una encuesta (título, candidatos y estado): \nverEncuesta NúmeroDeLaEncuesta'''
        getEncuesta(int(arg))
    
    def do_verListaEncuestas(self, arg):
        '''Muestra una lista con las encuestas que existen: \nverListaEncuesta'''
        getListaEncuestas()
    
    def do_verCandidatosDeEncuesta(self, arg):
        '''Muestra una lista con los candidatos de la encuesta elegida: \nverCandidatosDeEncuesta NúmeroDeLaEncuesta'''
        getListaCandidatosEncuesta(int(arg))
    
    def do_agregarCandidatoAEncuesta(self, arg):
        '''Agrega un candidato a la encuesta elegida: \nagregarCandidatoAEncuesta NúmeroDeLaEncuesta "Nombre del candidato"'''
        numVotacion, candidato = arg.split()
        addCandidatoEncuesta(int(numVotacion), candidato)

    def do_permitirVotacion(self, arg):
        '''Modifica la encuesta para que pueda ser votada: \nabrirEncuesta NúmeroDeLaEncuesta'''
        openEncuesta(int(arg))
    
    def do_cerrarVotacion(self, arg):
        '''Cierra la encuesta, se dejan de poder emitir votaciones: \ncerrarEncuesta NúmeroDeLaEncuesta'''
        closeEncuesta(int(arg))
    
    def do_verResultadosEncuesta(self, arg):
        '''Muestra los resultados de una encuesta (Número de votos por candidatos, Porcentaje de votos): \nverResultadosEncuesta NúmeroDeLaEncuesta'''
        getResultadosEncuesta(int(arg))
    
    def do_votar(self, arg):
        '''Vota en una encuesta a un candidato: \nvotar NúmeroDeLaEncuesta NúmeroDelCandidato'''
        numEncuesta, numCandidato = arg.split()
        setVotacion(int(numEncuesta), int(numCandidato))
    
    def do_exit(self, arg):
        return True


if __name__ == '__main__':
    DemocrappShell().cmdloop()
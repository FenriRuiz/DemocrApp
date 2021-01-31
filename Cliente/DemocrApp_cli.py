import cmd
from utils import *
from web3 import Web3



account_1 = "0x7aF2B11a315a7De42BE3A09f175f1916a817762a"
account_2 = "0x2cc666f3ad1514f133305f53AE9909b8043b0073"
account_3 = "0x9955eC1541343826ab17397A4B4DC31922fdaC08"

class DemocrappShell(cmd.Cmd):
    intro = 'Bienvenido a la terminal de DemocrApp.   Escribe help o ? para ver la lista de opciones.\n'
    prompt = '(DemocrApp) :'
    file = None

    # ----- basic turtle commands -----
    def do_crearEncuesta(self, arg):
        'Crea una nueva encuesta vacía: crearEncuesta "Nombre de la encuesta"'
        addEncuesta(account_1)

    def do_verEncuesta(self, arg):
        'Muestra la información de una encuesta (título, candidatos y estado): verEncuesta NúmeroDeLaEncuesta'
        getEncuesta()
    
    def do_verListaEncuesta(self):
        'Muestra una lista con las encuestas que existen: verListaEncuesta'
        getListaEncuestas()
    
    def do_agregarCandidatoAEncuesta(self, arg):
        'Agrega un candidato a la encuesta elegida: agregarCandidatoAEncuesta NúmeroDeLaEncuesta "Nombre del candidato"'
        addCandidatoEncuesta()

    def do_abrirEncuesta(self, arg):
        'Modifica la encuesta para que pueda ser votada: abrirEncuesta NúmeroDeLaEncuesta'
        openEncuesta()
    
    def do_cerrarEncuesta(self, arg):
        'Cierra la encuesta, se dejan de poder emitir votaciones: cerrarEncuesta NúmeroDeLaEncuesta'
        closeEncuesta()
    
    def do_verResultadosEncuesta(self, arg):
        'Muestra los resultados de una encuesta (Número de votos por candidatos, Porcentaje de votos): verResultadosEncuesta NúmeroDeLaEncuesta'
        getResultadosEncuesta()

if __name__ == '__main__':
    DemocrappShell().cmdloop()
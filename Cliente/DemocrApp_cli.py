import cmd
from utils import *
from web3 import Web3



account_1 = "0xfdE8E18C35dae63B37BeC4682cA3D699207454E1"
account_2 = "0xFF4F6B0AC5dd70cB7450c065761EB80a2914Fcd4"
account_3 = "0x5783B9b85Bb69C04744FdA90F5BE898302DEFfF1"

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
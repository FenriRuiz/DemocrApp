pragma solidity ^0.5.0;

contract ListaVotaciones{
    enum Estado {Editando, Abierto, Cerrado} Estado estado;
    Estado constant estadoBase = Estado.Editando;
    uint public numVotaciones = 0;

    struct Votante {
        string nombre;
        string candidato_elegido;
        bool ha_votado;
    }

    struct Votacion {
        uint id_votacion;
        string titulo;
        address id_creador;
        Estado estado;
        string[] candidatos;
        mapping(string => Votante) votantes;
    }

    mapping (uint => Votacion) public votaciones;

    constructor() public {
        nuevaVotacion("Votación a delegado de centro");

    }



    function nuevaVotacion(string memory _titulo) public{
        //Crear una nueva votación y añadirla a la lista de votaciones
        //Emitir la nueva votación
        string[] memory _candidatos;
        numVotaciones ++;
        votaciones[numVotaciones] = Votacion(numVotaciones, _titulo, msg.sender, estadoBase, _candidatos);
    }

    function agregarCandidato(uint numVotacion, string memory candidato) public {
        //Si es el creador de la votación
        require(
            msg.sender == votaciones[numVotacion].id_creador,
            "Solo el creador de la votación puede llamar a esta función"
        );
        // Si no hay ningún candidato en la votación se añade
        if(votaciones[numVotacion].candidatos.length==0){
            votaciones[numVotacion].candidatos.push(candidato);
        }
        // Si hay alguno se comprueba que el nuevo no exista ya.
        else{
            for (uint i = 0; i < votaciones[numVotacion].candidatos.length; i++){
                // Comparación de string en soldity @-@
                if(keccak256(abi.encodePacked(votaciones[numVotacion].candidatos[i]))==keccak256(abi.encodePacked(candidato))){
                    revert("El candidato se encuentra en la votación");
                }
            }        
            //Si no existe el nuevo candidato en la votacion
            //Añade el candidato a la votacion.
            votaciones[numVotacion].candidatos.push(candidato);
        }

    }

    function accederVotacion() public{
        //Crear un nuevo votante
        //Si el estado de la votación es Abierto
        //Añadir votante a la lista de votantes de la votación.
    }

    function estadoVotacionAbierto() public{
        //Si es el creador de la votación
        //Tomar la votación seleccionada
        //Si el estado de la votación es Editando
        //Votacion.estado = Estado.Abierta;
    }
    function estadoVotacionCerrado() public{
        //Si es el creador de la votación
        //Tomar la votación seleccionada
        //Si el estado de la votacion es Abierto
        //Votacion.estado = Estado.Cerrado;
    }

    function votar() public {
        //Tomar la votación seleccionada
        //Si el estado de la votación es Votando
        //Si el votante está en la votación
        //Cambia el estado de ha_votado a true
        //Cambia la variable eleccion.
    }

}

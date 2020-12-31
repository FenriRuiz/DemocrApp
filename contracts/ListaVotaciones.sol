pragma solidity ^0.5.0;

contract ListaVotaciones{
    enum Estado {Editando, Abierto, Cerrado} Estado estado;
    Estado constant estadoBase = Estado.Editando;
    uint public numVotaciones = 0;

    // struct Votante {
    //     uint id_votante;
    //     string candidato_elegido;
    //     bool ha_votado;
    // }

    struct Votacion {
        uint id_votacion;
        string titulo;
        address id_creador;
        Estado estado;
        mapping (uint => string) candidatos;
        // mapping (uint => Votante) votantes;
    }

    mapping (uint => Votacion) public votaciones;

    constructor() public {
        nuevaVotacion("Votación a delegado de centro");
    }

    function nuevaVotacion(string memory _titulo) public{
        //Crear una nueva votación y añadirla a la lista de votaciones
        //Emitir la nueva votación

        numVotaciones ++;
        votaciones[numVotaciones] = Votacion(numVotaciones, _titulo, msg.sender, estadoBase);
    }
    
    function agregarCandidato() public{
        //Si es el creador de la votación
        //Si no existe el nuevo candidato en la votacion
        //Añade el candidato a la votacion.
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

pragma solidity ^0.5.0;

contract ListaVotaciones{
    enum Estado {Editando, Abierto, Cerrado} Estado estado;
    Estado constant estadoBase = Estado.Editando;
    uint public numVotaciones = 0;

    struct Votacion {
        uint id_votacion;
        string titulo;
        address id_creador;
        Estado estado;
        string[] candidatos;
        mapping(address => uint) votosEmitidos;
    }

    mapping (uint => Votacion) public votaciones;

    constructor() public {
        //nuevaVotacion("Votación a delegado de centro");

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
        //Si la votación se encuentra en el estado de ediccion.
        require(
            votaciones[numVotaciones].estado == Estado.Editando,
            "La votación debe estar edicción para poder agregar candidatos"
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

    function estadoVotacionAbierto(uint numVotacion) public{
        //Si es el creador de la votación
        require(
            msg.sender == votaciones[numVotacion].id_creador,
            "Solo el creador de la votación puede llamar a esta función"
        );
        //Si el estado de la votación es Editando
        require(
            votaciones[numVotacion].estado == Estado.Editando,
            "La votación debe estar edicción para poder ser abierta a votaciones"
        );
        //Tomar la votación seleccionada y cambiar el estado a Abierto
        votaciones[numVotacion].estado = Estado.Abierto;
    }

    function estadoVotacionCerrado(uint numVotacion) public{
        //Si es el creador de la votación
        require(
            msg.sender == votaciones[numVotacion].id_creador,
            "Solo el creador de la votación puede llamar a esta función"
        );
        //Si el estado de la votacion es Editando o Abierto
        require(
            votaciones[numVotacion].estado != Estado.Cerrado,
            "La votación debe estar edicción o abierta para poder ser cerrada"
        ); 
        //Tomar la votación seleccionada y cambiar el estado a Cerrado
        votaciones[numVotacion].estado = Estado.Cerrado;
    }

    function votar(uint numVotacion, uint candidato) public {
        //Tomar la votación seleccionada
        //Si el estado de la votación es Votando
        require(
            votaciones[numVotacion].estado == Estado.Abierto,
            "La votación debe estar abierta a votaciones para poder votar"
        ); 
        require(
            votaciones[numVotacion].votosEmitidos[msg.sender] == 0,
            "El votante no tiene que existir dentro de las votaciones"
        );
        //Cambia la variable eleccion.
        votaciones[numVotacion].votosEmitidos[msg.sender] = candidato;
    }

}

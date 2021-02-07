pragma solidity >0.5.0;

contract ListaVotaciones{
    enum Estado {Editando, Abierto, Cerrado} Estado estado;
    Estado constant estadoBase = Estado.Editando;
    uint public numVotaciones = 0;

    struct Votacion{
        uint id_votacion;
        string titulo;
        address id_creador;
        Estado estado;
        uint numCandidatos;
        uint numVotantes;
        mapping (uint => string) candidatos;
        mapping (uint => VotoEmitido) votosEmitidos;
    }
    struct VotoEmitido{
        address id_votante;
        uint elegido;
    }

    mapping (uint => Votacion) public votaciones;

    constructor() public {
        //nuevaVotacion("Votación a delegado de centro");

    }
    function getNumVotaciones() public view returns(uint){
        return numVotaciones;
    }
    function getVotacion(uint numVotacion) public view returns(string memory){
        return votaciones[numVotacion].titulo;
    }

    function getCandidato(uint numVotacion, uint numCandidato) public view returns(string memory){
        return votaciones[numVotacion].candidatos[numCandidato];
    }
    function setCandidato(uint numVotacion, uint numCandidato, string memory nuevoNombre) public{
        votaciones[numVotacion].candidatos[numCandidato] = nuevoNombre;
    }
    function getVotosEmitido(uint numVotacion, uint numVoto) public view returns(address, uint){
        return (votaciones[numVotacion].votosEmitidos[numVoto].id_votante, votaciones[numVotacion].votosEmitidos[numVoto].elegido);
    }
    function nuevaVotacion(string memory _titulo) public{
        //Crear una nueva votación y añadirla a la lista de votaciones
        //Emitir la nueva votación
        numVotaciones ++;
        votaciones[numVotaciones] = Votacion(numVotaciones, _titulo, msg.sender, estadoBase, 0, 0);
    }
    function agregarCandidato(uint numVotacion, string memory candidato) public {
        //Si es el creador de la votación
        require(
            msg.sender == votaciones[numVotacion].id_creador, "Error, no es el creador"
        );
        //Si la votación se encuentra en el estado de ediccion.
        require(
            votaciones[numVotacion].estado == Estado.Editando, "Error, votacion abierta"
        );

        // Si no hay ningún candidato en la votación se añade
        if(votaciones[numVotacion].numCandidatos==0){
            votaciones[numVotacion].candidatos[votaciones[numVotacion].numCandidatos] = candidato;
            votaciones[numVotacion].numCandidatos ++;
        }
        // Si hay alguno se comprueba que el nuevo no exista ya.
        else{
            for (uint i = 0; i < votaciones[numVotacion].numCandidatos; i++){
                // Comparación de string en soldity @-@
                if(keccak256(abi.encodePacked(votaciones[numVotacion].candidatos[i]))==keccak256(abi.encodePacked(candidato))){
                    revert("Error, candidato en votacion");
                }
            }        
            //Si no existe el nuevo candidato en la votacion
            //Añade el candidato a la votacion.
            votaciones[numVotacion].candidatos[votaciones[numVotacion].numCandidatos] = candidato;
            votaciones[numVotacion].numCandidatos ++;
        }

    }
    function estadoVotacionAbierto(uint numVotacion) public{
        //Si es el creador de la votación
        require(
            msg.sender == votaciones[numVotacion].id_creador,
            "Error, funcion del creador"
        );
        //Si el estado de la votación es Editando
        require(
            votaciones[numVotacion].estado == Estado.Editando,
            "Error, votacion ya abierta o cerrada"
        );
        //Tomar la votación seleccionada y cambiar el estado a Abierto
        votaciones[numVotacion].estado = Estado.Abierto;
    }
    function estadoVotacionCerrado(uint numVotacion) public{
        //Si es el creador de la votación
        require(
            msg.sender == votaciones[numVotacion].id_creador,
            "Error, funcion del creador"
        );
        //Si el estado de la votacion es Editando o Abierto
        require(
            votaciones[numVotacion].estado != Estado.Cerrado,
            "Error, funcion en edicion"
        ); 
        //Tomar la votación seleccionada y cambiar el estado a Cerrado
        votaciones[numVotacion].estado = Estado.Cerrado;
    }
    function votar(uint numVotacion, uint candidato) public {
        //Tomar la votación seleccionada
        //Si el estado de la votación es Votando
        for (uint i = 0; i < votaciones[numVotacion].numVotantes; i++){
            if(votaciones[numVotacion].votosEmitidos[i].id_votante == msg.sender){
                    revert("El votante ya ha votado");
            }
        }    
        require(
            votaciones[numVotacion].estado == Estado.Abierto,
            "Error, votacion en edicion o cerrada"
        ); 
        //Cambia la variable eleccion.
        votaciones[numVotacion].votosEmitidos[votaciones[numVotacion].numVotantes].id_votante = msg.sender;
        votaciones[numVotacion].votosEmitidos[votaciones[numVotacion].numVotantes].elegido = candidato;
        votaciones[numVotacion].numVotantes ++;
    }

}

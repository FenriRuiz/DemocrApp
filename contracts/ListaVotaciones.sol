pragma solidity >=0.5.0;

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
    function sayHello() public pure returns (string memory) {
        return 'Hello World!';
    }
    function getNumVotaciones() public view returns(uint){
        return numVotaciones;
    }
    function getVotacion(uint numVotacion) public view returns(string memory){
        return votaciones[numVotacion].titulo;
    }
    function getNumVotantesVotacion(uint numVotacion) public view returns(uint){
        return votaciones[numVotacion].numVotantes;
    }
    function getEstadoEncuesta(uint numVotacion) public view returns(string memory) {
        if(votaciones[numVotacion].estado==Estado.Editando){
            return "Editando";
        }
        if(votaciones[numVotacion].estado==Estado.Abierto){
            return "Abierto";
        }
        if(votaciones[numVotacion].estado==Estado.Cerrado)
            return "Cerrado";
    }
    function getNumCandidatos(uint numVotacion) public view returns(uint){
        return votaciones[numVotacion].numCandidatos;
    }
    function getCandidato(uint numVotacion, uint numCandidato) public view returns(string memory){
        return votaciones[numVotacion].candidatos[numCandidato];
    }
    function setCandidato(uint numVotacion, uint numCandidato, string memory nuevoNombre) public{
        votaciones[numVotacion].candidatos[numCandidato] = nuevoNombre;
    }
    function getVotoEmitido(uint numVotacion, uint numVoto) public view returns(uint){
        //Devuelve el id del votante y su voto elegido. Sirve para hacer el recuento de votos.
        return votaciones[numVotacion].votosEmitidos[numVoto].elegido;
    }
    function nuevaVotacion(string memory _titulo) public returns(uint){
        //Crear una nueva votación y añadirla a la lista de votaciones
        //Emitir la nueva votación
        numVotaciones ++;

        votaciones[numVotaciones] = Votacion(numVotaciones, _titulo, msg.sender, estadoBase, 0, 0);
        return numVotaciones;
    }
    function agregarCandidato(uint numVotacion, string memory candidato) public returns(string memory) {
        //Si es el creador de la votación
        if(msg.sender != votaciones[numVotacion].id_creador){ 
            return "Error, no es el creador de la votacion";
        }
        //Si la votación se encuentra en el estado de ediccion.
        if(votaciones[numVotacion].estado != Estado.Editando){
            return "Error, votacion abierta";
        }

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
                    return "Error, el candidato se encuentra en la votacion";
                }
            }        
            //Si no existe el nuevo candidato en la votacion
            //Añade el candidato a la votacion.
            votaciones[numVotacion].candidatos[votaciones[numVotacion].numCandidatos] = candidato;
            votaciones[numVotacion].numCandidatos ++;
        }
        return candidato;

    }
    function estadoVotacionAbierto(uint numVotacion) public returns(string memory){
        //Si es el creador de la votación
        if(msg.sender != votaciones[numVotacion].id_creador){
            return "Error, no es el creador de la votacion";
        }
        //Si el estado de la votación es Editando
        if(votaciones[numVotacion].estado != Estado.Editando){
            return "Error, votacion abierta o cerrada";
        }
        //Tomar la votación seleccionada y cambiar el estado a Abierto
        votaciones[numVotacion].estado = Estado.Abierto;
        return "Votacion abierta";
    }
    function estadoVotacionCerrado(uint numVotacion) public returns(string memory){
        //Si es el creador de la votación
        if(msg.sender != votaciones[numVotacion].id_creador){
            return "Error, no es el creador de la votacion";
        }
        //Si el estado de la votacion es Editando o Abierto
        if(votaciones[numVotacion].estado == Estado.Cerrado){
            return "Error, la votacion esta cerrada";
        }
        if(votaciones[numVotacion].estado == Estado.Editando){
            return "Error, la votacion esta en edicion";
        }
        //Tomar la votación seleccionada y cambiar el estado a Cerrado
        votaciones[numVotacion].estado = Estado.Cerrado;
        return "Votacion cerrada";
    }
    function votar(uint numVotacion, uint candidato) public returns(string memory){
        //Tomar la votación seleccionada
        //Si el estado de la votación es Votando
        for (uint i = 0; i < votaciones[numVotacion].numVotantes; i++){
            if(votaciones[numVotacion].votosEmitidos[i].id_votante == msg.sender){
                    return "Error, el votante ya ha votado";
            }
        }    
        if(votaciones[numVotacion].estado != Estado.Abierto){
            return "Error, votacion en edicion o cerrada";
        }
        //Cambia la variable eleccion.
        votaciones[numVotacion].votosEmitidos[votaciones[numVotacion].numVotantes].id_votante = msg.sender;
        votaciones[numVotacion].votosEmitidos[votaciones[numVotacion].numVotantes].elegido = candidato;
        votaciones[numVotacion].numVotantes ++;
        return "Voto realizado correctamente";
    }

}

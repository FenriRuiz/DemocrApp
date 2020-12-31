var ListaVotaciones = artifacts.require("./ListaVotaciones.sol");

module.exports = function(deployer) {
    deployer.deploy(ListaVotaciones);
};
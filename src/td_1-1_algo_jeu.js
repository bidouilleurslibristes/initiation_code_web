nombre_a_trouver = 10;
nombre_demande = -1;

while(nombre_demande != nombre_a_trouver){
	chaine_demande = prompt("Nombre");
	nombre_demande = parseInt(chaine_demande);

	if (nombre_demande < nombre_a_trouver){
		console.log("C'est plus");
	}
	else if (nombre_demande > nombre_a_trouver) {
		console.log("C'est moins");
	}
	else {
		console.log("C'est bon");
	}
}

console.log("Bravo");

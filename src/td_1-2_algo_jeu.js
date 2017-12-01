nombre_a_trouver = 10;
nombre_demande = -1;

function tour(nombre_demande){
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

while(nombre_demande != nombre_a_trouver){
	// a chaque tour de jeu, on demande le nombre et on appelle la fonction tour
	nombre_demande = Number(prompt("Nombre"));
	tour(nombre_demande)
}

console.log("Bravo");

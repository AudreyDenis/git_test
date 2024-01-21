from arme import * 
from personnage import * 


player1.affiche_etat()
player2.affiche_etat()

player1.attaquer(player2)

player1.affiche_etat()
player2.affiche_etat()

player2.attaquer(player1)


player1.affiche_etat()
player2.affiche_etat()

player2.attaquer(player1)

player1.affiche_etat()
player2.affiche_etat()
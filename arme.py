from prettytable import PrettyTable
from random import randint
TYPE_WEAPON = {
    1:"_ATK_",
    2:"_DEF_"
}

class Arme:
    def __init__( self,
                  name  ="Arme",
                  genre ="DEF",
                  power =0):
        self.name  = name 
        self.genre = genre
        self.power = power
    
    def se_detruire(self):
        self.power = 0 
        print(f" l'arme {self.name} a ete detruite :( ... ")
        
    def ameliorer(self,point):
        print(f" {self.name}( power +{point})")
        self.power += point 
    
    def affiche_info(self):
        table = PrettyTable()
        table.field_names = ["name", 
                             "type", 
                             "Power"]
        table.add_row(      [f"{self.name}",
                             f"{self.genre}",
                             f"{self.power}"]
                      )
        print("\n",table,"\n")
        
weapons = {
    1 : Arme("Epee",
              TYPE_WEAPON[1],
              randint(10,100)),
    2 : Arme("Bouclier",
              TYPE_WEAPON[2],
              randint(10,100)),
    3 : Arme("Dague",
              TYPE_WEAPON[1],
              randint(10,50)), 
    4 : Arme("Armure",
              TYPE_WEAPON[2],
              randint(100,1500)),
    5 : Arme("Samaeda",
              TYPE_WEAPON[1],
              randint(100,500))
}


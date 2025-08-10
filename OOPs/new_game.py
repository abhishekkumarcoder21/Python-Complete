class Character:
    def __init__ (self,name,health,attack,blood):
        self.name=name
        self.health=health
        self.attack=attack
        self.blood=blood
    def attack_enemy(self):
        print(f"{self.name} attacks with power {self.attack} and has blood colour {self.blood}")

warrior=Character('Thor',100,50,'red')
mage=Character('Gandalf',80,70,'blue')
Archer=Character('BittuArcher',100,80,'green')
warrior.attack_enemy()
mage.attack_enemy()
Archer.attack_enemy()




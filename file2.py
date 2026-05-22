class Item:
    def __init__(self, name, value):
        self.name = name
        self.value = value

class Enemy:
    def __init__(self, name, health,damage):
        self.name=name
        self.health=health
        self.damage =damage
    def attack(self, player):
            player.health -= self.damage
            print(f"{self.name} атакує {player.name} на {self.damage} шкоди!")


class Character:
    def __init__(self, name, health,damage):
        self.name=name
        self.health=health
        self.damage= damage
        self.inventory = []
    def add_item(self,item):
        self.inventory.append(item)
    def show_inventory(self):
            print("Інвентар:")
            if len(self.inventory) == 0:
                print("Порожньо")
            else:
                for item in self.inventory:
                    print(f"- {item.name} (цінність: {item.value})")
    def attack(self, enemy):
            enemy.health -= self.damage
            print(f"{self.name} атакує {enemy.name} на {self.damage} шкоди!")

Geroi = Character("Hero",100,10)
vrag = Enemy("Enemy",60,5)
Treasure = Item("Сокровище",100)
Geroi.add_item(Treasure)
Geroi.show_inventory()
while Geroi.health>vrag.health:
    Geroi.attack(vrag)
    if vrag.health<=0:
        print(f"{vrag.name} переможений!")
        break
    vrag.attack(Geroi)
    print(f"{Geroi.name} HP: {Geroi.health}")

    if Geroi.health <= 0:
        print(f"{Geroi.name} програв!")
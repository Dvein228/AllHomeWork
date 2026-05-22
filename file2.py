class Enemy:
    def __init__(self, name, health,damage):
        self.name=name
        self.health=health
        self.damage =damage
    def attack(self, enemy):
            enemy.hp -= self.damage
            print(f"{self.name} атакує {enemy.name} на {self.damage} шкоди!")


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
            enemy.hp -= self.damage
            print(f"{self.name} атакує {enemy.name} на {self.damage} шкоди!")

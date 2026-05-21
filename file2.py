class Enemy:
    def __init__(self, name, health,damage):
        self.name=name
        self.health=health
        self.damage =damage


class Character:
    def __init__(self, name, health,damage):
        self.name=name
        self.health=health
        self.damage= damage
        self.inventory = []
    def addInInventory(self,item):
        self.inventory.append(item)
    def show_inventory(self):
            print("Інвентар:")
            if len(self.inventory) == 0:
                print("Порожньо")
            else:
                for item in self.inventory:
                    print(f"- {item.name} (цінність: {item.value})")

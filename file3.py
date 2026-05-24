class Spell:
    def __init__(self,name,damage):
        self.name = name
        self.damage = damage

class Item(Spell):
    def __init__(self,name,damage,size):
        super().__init__(name,damage)
        self.size = size

class Character:
    def __init__(self,name,level,hp,damage):
        self.name = name
        self.level =level
        self.hp = hp
        self.damage = damage
    def info(self):
        print(self.name,self.level,self.hp,self.damage)

    def on_hit(self,damage):
        self.hp -= damage

    def attack(self, enemy):
        enemy.on_hit(self.damage)

class Warior(Character):
    def __init__(self,name,level,hp,damage,rage):
        super().__init__(self.name,level,hp,damage)
        self.rage = rage
        self.inventory =[]
    def info(self):
        print(self.name, self.level, self.hp, self.damage,self.rage)
    def attack(self,enemy):
        enemy.on_hit(self.damage*self.rage)
    def add_in_inventory(self,item):
        self.inventory.append(item)
    def show_inventory(self):
        print(self.inventory)

    def on_hit(self, damage):
        self.hp -= damage
        self.rage += 10
        print(self.name, "злится! Ярость =", self.rage)

class Mage(Character):
    def __init__(self,name,level,hp,damage,knowledge):
        super().__init__(self.name,level,hp,damage,)
        self.knowledge =knowledge
        self.spells = []
    def learn_spell(self,spell):
        if len(self.spells) < self.knowledge:
            self.spells.append(spell)
            print(self.name, "выучил", spell)
    def increase_knowledge(self, amount):
        self.knowledge += amount
        print("Знания увеличены до", self.knowledge)
    def info(self):
        print(self.name, self.level, self.hp, self.damage, self.knowledge)

    def attack(self,enemy,spell =None):
        if spell is None:
            enemy.hp -= self.damage
            print(self.name, "атакует обычной атакой")
        else:
            if spell in self.spells:
                enemy.hp -= self.damage + spell.damage
                print(self.name, "использует", spell.name, "и наносит", self.damage + spell.damage, "урона")
            else:
                print(self.name, "не знает это заклинание!")

class Archer(Character):
    def __init__(self, name, level, hp, damage, miss):
        super().__init__(self.name, level, hp, damage)
        self.miss = miss
        self.inventory = []

    def info(self):
        print(self.name, self.level, self.hp, self.damage, self.miss)

    def add_in_inventory(self, item):
        self.inventory.append(item)

    def show_inventory(self):
        print(self.inventory)

    def attack(self,enemy):



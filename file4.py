class BankAccount:
    def __init__(self, money):
        self.money = money
    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Не можна знімати мінус")
        if amount > self.money:
            raise ValueError("Недостатньо грошей")
        if amount==0:
            raise ValueError("ошиибко")
        self.money -= amount
        print("Знято:", amount)
        print("Залишок:", self.money)

    def addMoney(self, amount):
        if amount < 0:
            raise ValueError("Нельзя минус закидывать")
        if amount == 0:
            raise ValueError("ошиибко")
        self.money += amount

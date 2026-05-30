class BankAccount:
    def __init__(self, money):
        self.money = money

    def withdraw(self, amount):
        if amount == 0:
            raise ValueError("Сума знімання не може бути 0")
        if amount < 0:
            raise ValueError("Сума знімання не може бути від'ємною")

        if amount > self.money:
            y_n = input("Недостатньо коштів. Оформити кредит? (y/n): ")
            if y_n.strip().lower() == "y":
                credit = amount - self.money
                days = int(input("На скільки днів оформити кредит? "))

                if days <= 30:
                    rate = 0.03
                else:
                    rate = 0.04

                repayment = credit * (1 + rate)

                print(f"Кредит оформлено на: {credit} грн")
                print(f"Відсоткова ставка: {int(rate * 100)}%")
                print(f"Сума до повернення за {days} днів: {repayment} грн")

                self.money += credit
            else:
                print("Операцію скасовано")
                return

        self.money -= amount
        print(f"Знято: {amount} грн")
        print(f"Залишок: {self.money} грн")

    def add_money(self, amount):
        if amount < 0:
            raise ValueError("Сума поповнення не може бути від'ємною")
        if amount == 0:
            raise ValueError("Сума поповнення не може бути 0")
        self.money += amount
        print(f"Рахунок поповнено на: {amount} грн")
        print(f"Баланс: {self.money} грн")

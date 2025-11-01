from abc import ABC, abstractmethod

class Beverage(ABC):
    def prepare(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        if self.customer_wants_condiments():
            self.add_condiments()
    def boil_water(self):
        print("Су қайнатылды")
    @abstractmethod
    def brew(self): ...
    def pour_in_cup(self):
        print("Кесе толтырылды")
    @abstractmethod
    def add_condiments(self): ...
    def customer_wants_condiments(self):
        ans = input("Қосымша дәмдеуіш керек пе? (иә/жоқ): ").strip().lower()
        if ans in ["иә","иа","ya","ә","yes","y"]:
            return True
        if ans in ["жоқ","жок","no","n"]:
            return False
        print("Дұрыс емес енгізу, әдепкі: жоқ")
        return False

class Tea(Beverage):
    def brew(self):
        print("Шай тұндырылды")
    def add_condiments(self):
        print("Қант және лимон қосылды")

class Coffee(Beverage):
    def brew(self):
        print("Кофе қайнатылды")
    def add_condiments(self):
        print("Сүт пен қант қосылды")

class HotChocolate(Beverage):
    def brew(self):
        print("Какоа ұнтағы ерітілді")
    def add_condiments(self):
        print("Зефир және даршын қосылды")

def menu():
    while True:
        print("\nСусындар:")
        print("1) Шай")
        print("2) Кофе")
        print("3) Ыстық шоколад")
        print("0) Шығу")
        x = input("Таңдау: ").strip()
        if x == "1":
            Tea().prepare()
        elif x == "2":
            Coffee().prepare()
        elif x == "3":
            HotChocolate().prepare()
        elif x == "0":
            print("Бағдарлама аяқталды")
            break
        else:
            print("Дұрыс емес енгізу")

if __name__ == "__main__":
    menu()

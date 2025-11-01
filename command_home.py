from abc import ABC, abstractmethod

class ICommand(ABC):
    @abstractmethod
    def execute(self): ...
    @abstractmethod
    def undo(self): ...

class Light:
    def __init__(self):
        self.is_on = False
    def on(self):
        self.is_on = True
        print("Жарық: қосылды")
    def off(self):
        self.is_on = False
        print("Жарық: өшірілді")

class Door:
    def __init__(self):
        self.is_open = False
    def open(self):
        self.is_open = True
        print("Есік: ашылды")
    def close(self):
        self.is_open = False
        print("Есік: жабылды")

class Thermostat:
    def __init__(self):
        self.temp = 22
    def increase(self):
        self.temp += 1
        print(f"Термостат: температура {self.temp}°C")
    def decrease(self):
        self.temp -= 1
        print(f"Термостат: температура {self.temp}°C")

class LightOnCommand(ICommand):
    def __init__(self, light):
        self.light = light
    def execute(self):
        self.light.on()
    def undo(self):
        self.light.off()

class LightOffCommand(ICommand):
    def __init__(self, light):
        self.light = light
    def execute(self):
        self.light.off()
    def undo(self):
        self.light.on()

class DoorOpenCommand(ICommand):
    def __init__(self, door):
        self.door = door
    def execute(self):
        self.door.open()
    def undo(self):
        self.door.close()

class DoorCloseCommand(ICommand):
    def __init__(self, door):
        self.door = door
    def execute(self):
        self.door.close()
    def undo(self):
        self.door.open()

class ThermostatUpCommand(ICommand):
    def __init__(self, t):
        self.t = t
    def execute(self):
        self.t.increase()
    def undo(self):
        self.t.decrease()

class ThermostatDownCommand(ICommand):
    def __init__(self, t):
        self.t = t
    def execute(self):
        self.t.decrease()
    def undo(self):
        self.t.increase()

class Tv:
    def __init__(self):
        self.on_state = False
    def on(self):
        self.on_state = True
        print("Теледидар: қосылды")
    def off(self):
        self.on_state = False
        print("Теледидар: өшірілді")

class TvOnCommand(ICommand):
    def __init__(self, tv):
        self.tv = tv
    def execute(self):
        self.tv.on()
    def undo(self):
        self.tv.off()

class TvOffCommand(ICommand):
    def __init__(self, tv):
        self.tv = tv
    def execute(self):
        self.tv.off()
    def undo(self):
        self.tv.on()

class Invoker:
    def __init__(self):
        self.history = []
    def run(self, cmd):
        cmd.execute()
        self.history.append(cmd)
    def undo_last(self):
        if not self.history:
            print("Қате: болдырылатын команда жоқ")
            return
        last = self.history.pop()
        last.undo()

def menu():
    light = Light()
    door = Door()
    thermo = Thermostat()
    tv = Tv()
    inv = Invoker()
    while True:
        print("\nМәзір:")
        print("1) Жарық қосу")
        print("2) Жарық өшіру")
        print("3) Есік ашу")
        print("4) Есік жабу")
        print("5) Температура +1")
        print("6) Температура -1")
        print("7) Теледидар қосу")
        print("8) Теледидар өшіру")
        print("9) Соңғы команданы болдырмау")
        print("0) Шығу")
        x = input("Таңдау: ").strip()
        if x == "1":
            inv.run(LightOnCommand(light))
        elif x == "2":
            inv.run(LightOffCommand(light))
        elif x == "3":
            inv.run(DoorOpenCommand(door))
        elif x == "4":
            inv.run(DoorCloseCommand(door))
        elif x == "5":
            inv.run(ThermostatUpCommand(thermo))
        elif x == "6":
            inv.run(ThermostatDownCommand(thermo))
        elif x == "7":
            inv.run(TvOnCommand(tv))
        elif x == "8":
            inv.run(TvOffCommand(tv))
        elif x == "9":
            inv.undo_last()
        elif x == "0":
            print("Бағдарлама аяқталды")
            break
        else:
            print("Дұрыс емес енгізу")

if __name__ == "__main__":
    menu()

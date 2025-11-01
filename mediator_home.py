from abc import ABC, abstractmethod

class IMediator(ABC):
    @abstractmethod
    def send_public(self, sender, message): ...
    @abstractmethod
    def send_private(self, sender, receiver_name, message): ...
    @abstractmethod
    def join(self, user): ...
    @abstractmethod
    def leave(self, user): ...

class ChatRoom(IMediator):
    def __init__(self):
        self.users = {}
    def send_public(self, sender, message):
        for name, u in self.users.items():
            if name != sender.name:
                u.receive(f"{sender.name}: {message}")
    def send_private(self, sender, receiver_name, message):
        if receiver_name not in self.users:
            sender.receive("Қате: мұндай пайдаланушы жоқ")
            return
        self.users[receiver_name].receive(f"(Жеке) {sender.name}: {message}")
    def join(self, user):
        self.users[user.name] = user
        self.broadcast_system(f"{user.name} бөлмеге кірді")
    def leave(self, user):
        if user.name in self.users:
            del self.users[user.name]
            self.broadcast_system(f"{user.name} бөлмеден шықты")
    def broadcast_system(self, text):
        for u in self.users.values():
            u.receive(f"[Жүйе]: {text}")

class User:
    def __init__(self, name, mediator):
        self.name = name
        self.mediator = mediator
    def send(self, text):
        self.mediator.send_public(self, text)
    def send_private(self, to_name, text):
        self.mediator.send_private(self, to_name, text)
    def receive(self, text):
        print(f"{self.name} алды: {text}")

def demo():
    room = ChatRoom()
    a = User("Айдана", room)
    b = User("Ернар", room)
    c = User("Әли", room)
    room.join(a)
    room.join(b)
    room.join(c)
    a.send("Сәлем бәріне")
    b.send_private("Айдана", "Сен қалайсың?")
    c.send("Жиналыс 18:00-де")
    room.leave(b)
    a.send_private("Ернар", "Естіліп тұр ма?")
    c.send("Кездесу аяқталды")

if __name__ == "__main__":
    demo()

class Kid:
    def __init__(self, name: str, age: int):
        self.__name = name
        self.__age = age
    def getName(self):
        return self.__name
    def getAge(self):
        return self.__age
    def setName(self, name: str):
        self.__name = name
    def setAge(self, age: int):
        self.__age = age
    def __str__(self) -> str:
        return f"{self.__name}:{self.__age}"
class Trampoline:
    def __init__(self):
        self.playing: list[Kid | None] = []
        self.waiting: list[Kid] = []
    def arrive(self, kid: Kid):
        self.waiting.insert(0, kid)
    def enter(self):
        kid = self.waiting.pop()
        self.playing.insert(0, kid)
        del kid
    def leave(self):
        if len(self.playing) == 0:
            return
        kid = self.playing.pop()
        self.waiting.insert(0, kid)
        del kid
    def remove(self, name: str):
        for index, kid in enumerate(self.waiting):
            if kid.getName() == name:
                self.wa.pop(index)
                return
        for index, kid in enumerate(self.playing):
            if kid.getName() == name:
                self.playing.pop(index)
                return
        print(f"fail: {name} nao esta no pula-pula")
    def __str__(self) -> str:
        playing = ", ".join([str(x) for x in self.playing])
        waiting = ", ".join([str(x) for x in (self.waiting)])
        return f"[{waiting}] => [{playing}]"
def main():
    pulapula = Trampoline()
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")
        if args[0] == "end":
            break
        elif args[0] == "show":
            print(pulapula)
        elif args[0] == "arrive":
            name = (str(args[1]))
            age = (int(args[2]))
            pulapula.arrive(Kid(name, age))
        elif args[0] == "enter":
            pulapula.enter()
        elif args[0] == "leave":
            pulapula.leave()
        elif args[0] == "remove":
            remover = args[1]
            pulapula.remove(remover)
main()

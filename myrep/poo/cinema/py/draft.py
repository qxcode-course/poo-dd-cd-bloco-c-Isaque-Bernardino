class Client:
    def __init__(self, id: str, phone: int):
        self.__id = id
        self.__phone = phone
    def getId(self):
        return self.__id
    def setId(self, id: str):
        self.__id = id
    def getPhone(self):
        return self.__phone
    def setPhone(self, phone: int):
        self.__phone = phone
    def __str__(self) -> str:
        return f"{self.__id}:{self.__phone}"
class Theater:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.__seats: list[Client | None] = []
        for x in range(capacity):
            self.__seats.append(None)
    def verifyIndex(self, index: int) -> bool:
        if index < 0 or index >= len(self.__seats):
            return False
        else:
            return True
    def reserve(self, id: str, phone: int, index: int) -> bool:
        if self.verifyIndex(index) == False:
             print("fail: cadeira nao existe")
             return
        for i, client in enumerate(self.__seats):
            if client is not None and client.getId() == id:
                print("fail: cliente ja esta no cinema")
                return
        if self.__seats[index] != None:
            print("fail: cadeira ja esta ocupada")
            return False
        self.__seats[index] = (Client(id, phone))
        return True
    def cancel(self, id: str):
        for i, client in enumerate(self.__seats):
            if client is not None and client.getId() == id:
                self.__seats[i] = None
                return
        print("fail: cliente nao esta no cinema")
    def getSeats(self):
        return self.__seats
    def __str__(self) -> str:
        seats = " ".join("-" if x is None else str(x) for x in self.__seats)
        return f"[{seats}]"
def main():
    cinema = Theater(0)
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")
        if args[0] == "end":
            break
        if args[0] == "show":
            print(cinema)
        if args[0] == "init":
            cinema = Theater (int(args[1]))
        if args[0] == "reserve":
            id = str(args[1])
            phone = int(args[2])
            index = int(args[3])
            cinema.reserve(id, phone, index)
        if args[0] == "cancel":
            client = (str(args[1]))
            cinema.cancel(client)
main()
    
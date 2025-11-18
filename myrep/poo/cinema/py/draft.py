class Client:
    def __init__(self, id: str, phone: int):
        self.__id = id
        self.__phone = phone
    def getId(self):
        return self.__id
    def setId(self):
    def getPhone(self):
        return self.__phone
    def setPhone(self):
class Theater:
    def __init__(self, capacity: int):
        self.capacity = capacity
def main():

    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")
main()
    
class Lead:
    def __init__(self, thickness: float, hardness: str, size: int):
        self.__thickness = thickness
        self.__hardness = hardness
        self.__size = size
    def getThickness(self):
        return self.__thickness
    def getHardness(self):
        return self.__hardness
    def getSize(self):
        return self.__size
    def setSize(self, size: int):
        self.__size = size
    def usagePerSheet(self):
        if self.__hardness == "HB":
            return 1
        if self.__hardness == "2B":
            return 2
        if self.__hardness == "4B":
            return 4
        if self.__hardness == "6B":
            return 6
    def __str__(self) -> str:
        return f"[{self.__thickness}:{self.__hardness}:{self.__size}]"
class Pencil:
    def __init__(self, thickness: float):
        self.__thickness = thickness
        self.__tip = [ Lead | None] = []
        self.__barrel = [Lead] = []
    def init(self, thickness: float):
        self.__thickness = thickness
    def hasGrafite(self) -> bool:
        if self.__tip == None:
            return False
        else:
            return True
    def insert(self, thickness: float, hardness: str, size: int) -> bool:
        if self.__thickness != thickness:
            print("fail: calibre incompativel")
            return False
        if self.hasGrafite():
            print("fail: ja existe grafite")
            return False
        self.__tip = Lead(thickness, hardness, size)
        return True
    def insert(self, thickness: float, hardness: str, size: int) -> bool:
        if self.__thickness != thickness:
            print("fail: calibre incompativel")
            return False
        self.__barrel = Lead(thickness, hardness, size)
        return True
    def remove(self) -> Lead | None:
        if self.__tip == None:
            print("fail: nao existe grafite")
            return None
        lead = self.__tip
        self.__tip = None
    def writePage(self):
        if self.__tip == None:
            print("fail: nao existe grafite")
            return
        lead = self.__tip
        if lead.getSize() <= 10:
            print("fail: tamanho insuficiente")
            return
        cost = lead.usagePerSheet()
        newSize = lead.getSize() - cost
        if newSize < 10:
            self.__tip.setSize(10)
            print("fail: folha incompleta")
            return
        lead.setSize(newSize)
    def __str__(self) -> str:
        st = f"calibre: {self.__thickness}, "
        if self.__tip == None:
            st += f"grafite: null"
        else:
            st += f"grafite: {self.__tip}"
        return st
def main():
    pencil = Pencil (0, None)
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")
        if args[0] == "end":
            break
        if args[0] == "show":
            print(pencil)
        if args[0] == "init":
            thickness = float(args[1])
            pencil.init(thickness)
        if args[0] == "insert":
            thickness = float(args[1])
            hardness = str(args[2])
            size = int(args[3])
            pencil.insert(thickness, hardness, size)
        if args[0] == "remove":
            pencil.remove()
        if args[0] == "write":
            pencil.writePage()
main()
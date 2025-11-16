class Pessoa:
    def __init__(self, nome: str):
        self.nome = nome
    def __str__(self):
        return self.nome
class Budega:
    def __init__(self, numCaixas: int):
        self.caixas: list[Pessoa | None] = []
        for x in range(numCaixas):
            self.caixas.append(None)
        self.espera: list[Pessoa] = []
    def enter(self, pessoa: Pessoa):
        self.espera.append(pessoa)
    def call(self, index: int):
        if index < 0 or index >= len(self.caixas):
            print("fail: caixa inexistente")
            return
        if self.caixas[index] is not None:
            print("fail: caixa ocupado")
            return
        if len(self.espera) == 0:
            print("fail: sem clientes")
            return
        self.caixas[index] = self.espera[0]
        del self.espera[0]
    def finish(self, index: int):
        if index < 0 or index >= len(self.caixas):
            print("fail: caixa inexistente")
            return
        if self.caixas[index] is None:
            print("fail: caixa vazio")
            return
        self.caixas[index] = None
    def giveUp(self, nome: str) -> Pessoa | None:
        for index, pessoa in enumerate(self.espera):
            if pessoa.nome == nome:
                aux = self.espera[index]
                del self.espera[index]
                return aux
        return None
    def __str__(self):
        caixas = ", ".join(["-----" if x is None else str(x) for x in self.caixas])
        espera = ", ".join([str(x) for x in self.espera])
        return f"Caixas: [{caixas}]\nEspera: [{espera}]"
def main():
    budega = Budega (0)
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")
        if args[0] == "end":
            break
        elif args[0] == "show":
            print(budega)
        elif args[0] == "init":
            budega = Budega (int(args[1]))
        elif args[0] == "arrive":
            cliente = (args[1])
            budega.enter(Pessoa(cliente))
        elif args[0] == "call":
            fila = int(args[1])
            budega.call(fila)
        elif args[0] == "finish":
            finalizar = int(args[1])
            budega.finish(finalizar)
        else:
            print("fail: comando inválido")
main()
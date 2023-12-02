Seletiva = []

class Saco:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
        self.anterior = None

class CaminhaoDeLixo:
    def __init__(self):
        self.cabeca = None
        self.cauda = None

    def inserir_inicio(self, valor):
        novo_no = Saco(valor)
        novo_no.proximo = self.cabeca
        if self.cabeca:
            self.cabeca.anterior = novo_no
        else:
            self.cauda = novo_no
        self.cabeca = novo_no

    def inserir_meio(self, posicao, valor):
        if posicao == 0:
            self.inserir_inicio(valor)
            return

        novo_no = Saco(valor)
        atual = self.cabeca
        for i in range(posicao - 1):
            if atual is None:
                raise Exception("Posição inválida")
            atual = atual.proximo
        novo_no.proximo = atual.proximo
        novo_no.anterior = atual
        if atual.proximo:
            atual.proximo.anterior = novo_no
        else:
            self.cauda = novo_no
        atual.proximo = novo_no

    def inserir_final(self, valor):
        novo_no = Saco(valor)
        if not self.cabeca:
            self.cabeca = novo_no
            self.cauda = novo_no
            return
        self.cauda.proximo = novo_no
        novo_no.anterior = self.cauda
        self.cauda = novo_no

    def deletar_inicio(self):
        if not self.cabeca:
            return
        if self.cabeca.proximo:
            self.cabeca.proximo.anterior = None
        else:
            self.cauda = None
        self.cabeca = self.cabeca.proximo

    def deletar_meio(self, posicao):
        if posicao == 0:
            self.deletar_inicio()
            return
        atual = self.cabeca
        for i in range(posicao):
            if atual is None:
                raise Exception("Posição inválida")
            atual = atual.proximo
        if atual.anterior:
            atual.anterior.proximo = atual.proximo
        if atual.proximo:
            atual.proximo.anterior = atual.anterior
        else:
            self.cauda = atual.anterior

    def deletar_final(self):
        if not self.cabeca:
            return
        if not self.cabeca.proximo:
            self.cabeca = None
            self.cauda = None
            return
        self.cauda.anterior.proximo = None
        self.cauda = self.cauda.anterior

    def buscar(self, valor):
        atual = self.cabeca
        while atual:
            if atual.valor == valor:
                return True
            atual = atual.proximo
        return False

    def travessia(self):
        atual = self.cabeca
        while atual:
            print(atual.valor)
            atual = atual.proximo

    def SepararLixo(self):
        atual = self.cabeca
        while atual:
            Seletiva.append(atual.valor)
            atual = atual.proximo

class LixosPares:
    def __init__(self):
        self.cabeca = None
        self.cauda = None

    def JogaPar(self, valor):
        novo_no = Saco(valor)
        if not self.cabeca:
            self.cabeca = novo_no
            self.cauda = novo_no
            return
        self.cauda.proximo = novo_no
        novo_no.anterior = self.cauda
        self.cauda = novo_no

    def travessia(self):
        atual = self.cabeca
        while atual:
            print(atual.valor)
            atual = atual.proximo

    def buscar(self, valor):
        atual = self.cabeca
        while atual:
            if atual.valor == valor:
                return True
            atual = atual.proximo
        return False

class LixosImpares:
    def __init__(self):
        self.cabeca = None
        self.cauda = None

    def JogaImpar(self, valor):
        novo_no = Saco(valor)
        if not self.cabeca:
            self.cabeca = novo_no
            self.cauda = novo_no
            return
        self.cauda.proximo = novo_no
        novo_no.anterior = self.cauda
        self.cauda = novo_no

    def travessia(self):
        atual = self.cabeca
        while atual:
            print(atual.valor)
            atual = atual.proximo

    def buscar(self, valor):
        atual = self.cabeca
        while atual:
            if atual.valor == valor:
                return True
            atual = atual.proximo
        return False

class LixosPrimos:
    def __init__(self):
        self.cabeca = None
        self.cauda = None

    def JogaPrimo(self, valor):
        novo_no = Saco(valor)
        if not self.cabeca:
            self.cabeca = novo_no
            self.cauda = novo_no
            return
        self.cauda.proximo = novo_no
        novo_no.anterior = self.cauda
        self.cauda = novo_no

    def travessia(self):
        atual = self.cabeca
        while atual:
            print(atual.valor)
            atual = atual.proximo

    def buscar(self, valor):
        atual = self.cabeca
        while atual:
            if atual.valor == valor:
                return True
            atual = atual.proximo
        return False

def mergeSort(lis):
    if len(lis)>1:
        mid = len(lis)//2
        lefthalf = lis[:mid]
        righthalf = lis[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                lis[k]=lefthalf[i]
                i=i+1
            else:
                lis[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            lis[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            lis[k]=righthalf[j]
            j=j+1
            k=k+1
    return lis

def TestePrimo(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


Caminhao = CaminhaoDeLixo()
LixoPar = LixosPares()
LixoImpar = LixosImpares()
LixoPrimo = LixosPrimos()


def Separação():
    for i in Seletiva:
        if TestePrimo(i):
            LixoPrimo.JogaPrimo(i)

        elif i % 2 == 0:
            LixoPar.JogaPar(i)

        elif i % 2 == 1:
            LixoImpar.JogaImpar(i)


#"""FRONT END"""
#INSERÇÃO 
print("Olá, esse programa foi realizado para separar o seu lixo.")
print("Para inserir o seu lixo basta colocar o seu numero e nós iremos cuidar da organização para você, quando você terminar de inserir basta digitar FIM. 0 e numeros iguais não são selecionaveis")
lixoinput = input()

while lixoinput != "FIM":

    Seletiva.append(int(lixoinput))

    lixoinput = input()
Seletiva = mergeSort(Seletiva)

for i in Seletiva:
    Caminhao.inserir_final(i)




#REMOÇÃO
print("Agora você poderá remover o lixo caso algum erro tenha sido cometido durante a inserção, quando acabar coloque FIM.")
print("Para você retirar um valor coloque a posição dele. Obs: as posições podem mudar quando você remover algum valor. E não tente remover algo que você não colocou.")


print(*Seletiva)
retirainput = input()

while retirainput != "FIM":
    if int(retirainput) == 0:
        Caminhao.deletar_inicio()
        Seletiva.pop(0)

    elif int(retirainput) == (len(Seletiva)-1) :
        Caminhao.deletar_final()
        Seletiva.pop(int(retirainput))
    else:
        Caminhao.deletar_meio(int(retirainput))
        Seletiva.pop(int(retirainput))

    print(*Seletiva)
    retirainput = input()

Separação()

print("Agora todo o lixo que você jogou ja está separado e em seu devido lugar.")
print("Para ver em qual lixeira foram colocados seu lixo basta digitar:")
print("Org: Lixos Organicos(Pares)")
print("Pap: Papeís(Impares)")
print("Pla: Plasticos(Primos)")
print("Se quiser apenas buscar um lixo espesifico, e ver se ele está presente em alguma lixeira digite seu Numero")
print("Para encerrar o programa digite FIM.")

BT = input()

while BT != 'FIM':
    if BT == "Org":

        LixoPar.travessia()
    elif BT == "Pap":

        LixoImpar.travessia()

    elif BT == "Pla":

        LixoPrimo.travessia()
    
    else:
        if LixoPar.buscar(int(BT)):
            print("O lixo", BT, "esta no lixo organico!")

        elif LixoImpar.buscar(int(BT)):
            print("O lixo", BT, "esta no lixo de papel!")
        
        elif LixoPrimo.buscar(int(BT)):
            print("O lixo", BT, "esta no lixo de plastico!")

        else:
            print("O lixo", BT, "não esta em nenhuma lixeira. ;-;")

    BT = input()

#"""TESTES"""
'''Caminhao.inserir_final(1)
Caminhao.inserir_final(2)
Caminhao.inserir_final(3)
Caminhao.inserir_inicio(0)
Caminhao.inserir_meio(2, 1.5)
Caminhao.inserir_final(4)
Caminhao.inserir_final(5)
Caminhao.inserir_final(6)
Caminhao.inserir_final(7)
Caminhao.inserir_final(8)
Caminhao.inserir_final(9)
Caminhao.inserir_final(10)
Caminhao.inserir_final(11)
Caminhao.inserir_final(12)
Caminhao.inserir_final(13)
Caminhao.inserir_final(15)
Caminhao.inserir_final(21)



Caminhao.travessia()

print("separador")
LixoPar.travessia()
print("separador")
LixoImpar.travessia()
print("separador")
LixoPrimo.travessia()
print("separador")
print(Seletiva)
'''
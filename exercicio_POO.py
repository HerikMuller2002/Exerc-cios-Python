class Fabricante:
    def __init__(self,nome):
        self.nome = nome


class Motor:
    def __init__(self,nome):
        self.nome = nome


class Carro:
    def __init__(self,nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None
    
    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self,valor):
        self._motor = valor

    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self,valor):
        self._fabricante = valor



motor_1_0 = Motor("1.0")
fabricante1 = Fabricante("Fiat")
carro1 = Carro("Palio")

carro1.motor = motor_1_0
carro1.fabricante = fabricante1

print(carro1.fabricante.nome,carro1.nome,carro1.motor.nome)


motor_2_0 = Motor("2.0")
fabricante2 = Fabricante("chevrolet")
carro2 = Carro("frontier")

carro2.motor = motor_2_0
carro2.fabricante = fabricante2

print(carro2.fabricante.nome,carro2.nome,carro2.motor.nome)


fabricante3 = Fabricante("honda")
carro3 = Carro("civic")

carro3.motor = motor_1_0
carro3.fabricante = fabricante3

print(carro3.fabricante.nome,carro3.nome,carro3.motor.nome)
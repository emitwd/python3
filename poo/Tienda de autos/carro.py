class Carro:
    def __init__(self, marca, modelo, color, precio, estado) -> None:
        self.MARCA = marca # Constantes en python se asignan con mayus
        self.MODELO = modelo
        self.color = color
        self.precio = precio
        self.estado = estado
        self.__variableprivada = 10 # Variables privadas se usa doble barra baja 
        
    def __str__(self) -> str:
        return f""" 
    MARCA: {self.MARCA}\n 
    MODELO: {self.MODELO}\n 
    COLOR: {self.color}\n 
    PRECIO: {self.precio}
    ESTADO: {self.estado}"""

        
        

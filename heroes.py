from abc import ABC, abstractmethod

class Hero(ABC):
    def __init__(self, nome, raca, classe, forca, inteligencia, destreza):
        self.nome = nome
        self.raca = raca
        self.classe = classe
        self.forca = forca
        self.inteligencia = inteligencia
        self.destreza = destreza

    @abstractmethod
    def apresentar_habilidades(self):
        pass

class HumanoGuerreiro(Hero):
    def __init__(self, nome):
        super().__init__(nome, "Humano", "Guerreiro", forca=10, inteligencia=6, destreza=8)

    def apresentar_habilidades(self):
        return "Habilidades: Ataque Rápido, Escudo Defensivo"

class ElfoMago(Hero):
    def __init__(self, nome):
        super().__init__(nome, "Elfo", "Mago", forca=4, inteligencia=12, destreza=9)

    def apresentar_habilidades(self):
        return "Habilidades: Bola de Fogo, Teleporte"

class OrcLadino(Hero):
    def __init__(self, nome):
        super().__init__(nome, "Orc", "Ladino", forca=8, inteligencia=5, destreza=10)

    def apresentar_habilidades(self):
        return "Habilidades: Ataque Furtivo, Furtividade"

class HumanoMago(Hero):
    def __init__(self, nome):
        super().__init__(nome, "Humano", "Mago", forca=5, inteligencia=10, destreza=7)

    def apresentar_habilidades(self):
        return "Habilidades: Cura Mágica, Explosão Arcana"

class ElfoGuerreiro(Hero):
    def __init__(self, nome):
        super().__init__(nome, "Elfo", "Guerreiro", forca=7, inteligencia=8, destreza=11)

    def apresentar_habilidades(self):
        return "Habilidades: Arco Preciso, Esquiva Ágil"

class OrcGuerreiro(Hero):
    def __init__(self, nome):
        super().__init__(nome, "Orc", "Guerreiro", forca=12, inteligencia=3, destreza=6)

    def apresentar_habilidades(self):
        return "Habilidades: Fúria Incontrolável, Força Bruta"

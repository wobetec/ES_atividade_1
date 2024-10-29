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

    def __str__(self):
        return f"""Nome: {self.nome}
Raça: {self.raca}
Classe: {self.classe}
Força: {self.forca}
Inteligência: {self.inteligencia}
Destreza: {self.destreza}
{self.apresentar_habilidades()}"""


class HumanoGuerreiro(Hero):
    def __init__(self, nome):
        super().__init__(
            nome, "Humano", "Guerreiro", forca=10, inteligencia=6, destreza=8
        )

    def apresentar_habilidades(self):
        return "Habilidades: Ataque Rápido, Escudo Defensivo"


class HumanoMago(Hero):
    def __init__(self, nome):
        super().__init__(
            nome, "Humano", "Mago", forca=5, inteligencia=10, destreza=7
        )

    def apresentar_habilidades(self):
        return "Habilidades: Cura Mágica, Explosão Arcana"


class HumanoLadino(Hero):
    def __init__(self, nome):
        super().__init__(
            nome, "Humano", "Ladino", forca=5, inteligencia=10, destreza=7
        )

    def apresentar_habilidades(self):
        return "Habilidades: Ataque Furtivo, Furtividade"


class ElfoGuerreiro(Hero):
    def __init__(self, nome):
        super().__init__(
            nome, "Elfo", "Guerreiro", forca=7, inteligencia=8, destreza=11
        )

    def apresentar_habilidades(self):
        return "Habilidades: Arco Preciso, Esquiva Ágil"


class ElfoMago(Hero):
    def __init__(self, nome):
        super().__init__(
            nome, "Elfo", "Mago", forca=4, inteligencia=12, destreza=9
        )

    def apresentar_habilidades(self):
        return "Habilidades: Bola de Fogo, Teleporte"


class ElfoLadino(Hero):
    def __init__(self, nome):
        super().__init__(
            nome, "Elfo", "Ladino", forca=4, inteligencia=12, destreza=9
        )

    def apresentar_habilidades(self):
        return "Habilidades: Flecha Envenenada, Furtividade"


class OrcGuerreiro(Hero):
    def __init__(self, nome):
        super().__init__(
            nome, "Orc", "Guerreiro", forca=12, inteligencia=3, destreza=6
        )

    def apresentar_habilidades(self):
        return "Habilidades: Fúria Incontrolável, Força Bruta"


class OrcMago(Hero):
    def __init__(self, nome):
        super().__init__(
            nome, "Orc", "Mago", forca=12, inteligencia=3, destreza=6
        )

    def apresentar_habilidades(self):
        return "Habilidades: Bola de Fogo, Teleporte"


class OrcLadino(Hero):
    def __init__(self, nome):
        super().__init__(
            nome, "Orc", "Ladino", forca=8, inteligencia=5, destreza=10
        )

    def apresentar_habilidades(self):
        return "Habilidades: Ataque Furtivo, Furtividade"


class AnaoGuerreiro(Hero):
    def __init__(self, nome):
        super().__init__(
            nome, "Anao", "Guerreiro", forca=12, inteligencia=3, destreza=6
        )

    def apresentar_habilidades(self):
        return "Habilidades: Machado Duplo, Escudo Defensivo"


class AnaoMago(Hero):
    def __init__(self, nome):
        super().__init__(
            nome, "Anao", "Mago", forca=12, inteligencia=3, destreza=6
        )

    def apresentar_habilidades(self):
        return "Habilidades: Cura dos Ancestrais, Explosão Arcana"


class AnaoLadino(Hero):
    def __init__(self, nome):
        super().__init__(
            nome, "Anao", "Ladino", forca=8, inteligencia=5, destreza=10
        )

    def apresentar_habilidades(self):
        return "Habilidades: Passos Silenciosos, Sono Profundo"

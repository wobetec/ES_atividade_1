from heroes import (
    HumanoGuerreiro,
    HumanoMago,
    HumanoLadino,
    ElfoGuerreiro,
    ElfoMago,
    ElfoLadino,
    OrcGuerreiro,
    OrcMago,
    OrcLadino
)


class HeroFactory:
    @staticmethod
    def create_hero(raca, classe, nome):
        if raca == "Humano":
            if classe == "Guerreiro":
                class_ = HumanoGuerreiro
            elif classe == "Mago":
                class_ = HumanoMago
            elif classe == "Ladino":
                class_ = HumanoLadino
            else:
                raise NotImplementedError(f"CLasse {classe} não implementada")
        elif raca == "Elfo":
            if classe == "Guerreiro":
                class_ = ElfoGuerreiro
            elif classe == "Mago":
                class_ = ElfoMago
            elif classe == "Ladino":
                class_ = ElfoLadino
            else:
                raise NotImplementedError(f"CLasse {classe} não implementada")
        elif raca == "Orc":
            if classe == "Guerreiro":
                class_ = OrcGuerreiro
            elif classe == "Mago":
                class_ = OrcMago
            elif classe == "Ladino":
                class_ = OrcLadino
            else:
                raise NotImplementedError(f"CLasse {classe} não implementada")
        else:
            raise NotImplementedError(f"Raça {raca} não implementada")

        return class_(nome)

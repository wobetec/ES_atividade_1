# ES_atividade_1

## Requisitos

1. Criamos uma classe abstrata `Hero` que recebe os parâmetros solicitados e possui o método abstrato apresentar_habilidade.

2. Criamos 9 classes concretas para o produto cartesinao (Raça)x(Classe) e implementamos o método apresentar_habilidade.

3. Elaboramos um script `main.py` que funciona como driver code e pode ser executado como:

    python main.py <raça> <classe> <nome>

4. Para facilitar esse processo utilizamos o design pattern Factory Method no arquivo `heroes_factory.py`. Então para criar uma nova Raça por exemplo, basta criar uma nova classe concreta e adicionar no método `create_hero` da classe `HeroesFactory`.

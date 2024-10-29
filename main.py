import sys
from heroes_factory import HeroFactory


def help():
    print("Uso: python main.py <raça> <classe> <nome>")
    sys.exit(1)


def get_args():
    if len(sys.argv) < 4:
        help()

    raca = sys.argv[1]
    classe = sys.argv[2]
    nome = sys.argv[3]

    return raca, classe, nome


def main():
    raca, classe, nome = get_args()

    hero = HeroFactory.create_hero(raca, classe, nome)

    print(hero)


if __name__ == "__main__":
    main()

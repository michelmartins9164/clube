from multiprocessing.context import Process
from utils import validar_parametros
from crawlers import carguero
import json
import sys


def _main(parametros):
    validar_parametros(parametros)
    carguero.MultiplosProcessosCarguero(config=parametros).iniciar()


def main():
    args = sys.argv[1]
    _main(args)


if __name__ == "__main__":
    main()
    # _main("0,,,,")


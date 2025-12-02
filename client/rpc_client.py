import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from common.rpc_utils import RPCClient

client = RPCClient()

while True:
    print("1 - Soma")
    print("2 - Média")
    print("3 - Busca simulada")
    print("4 - Dobro")
    print("0 - Sair")

    op = input("Escolha: ")

    if op == "0":
        break

    if op == "1":
        a = float(input("A: "))
        b = float(input("B: "))
        print(client.call("rpc_soma", {"a": a, "b": b}))

    elif op == "2":
        nums = input("Valores separados por vírgula: ")
        lista = [float(x) for x in nums.split(",")]
        print(client.call("rpc_media", {"lista": lista}))

    elif op == "3":
        termo = input("Buscar: ")
        print(client.call("rpc_busca", {"query": termo}))

    elif op == "4":
        n = float(input("Número: "))
        print(client.call("rpc_dobro", {"n": n}))

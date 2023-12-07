# No arquivo main.py

from utils import Candidato, listar_candidatos, iniciar_votacao, contabilizar_votos, zerar_votos, apurar_votos, mostrar_resultados

def main():
    # Criar candidatos para prefeito
    prefeitos = [
        Candidato("22", "Bolsonaro", "PartidoA", "prefeito"),
        Candidato("13", "Lula", "PartidoB", "prefeito"),
        Candidato("01", "Fulano", "PartidoF", "prefeito"),
        # Adicione mais candidatos conforme necessário
    ]

    # Criar candidatos para vereador
    vereadores = [
        Candidato("00001", "Ana", "PartidoA", "vereador"),
        Candidato("00002", "Allan", "PartidoB", "vereador"),
        Candidato("00003", "Joao", "PartidoC", "vereador"),
        Candidato("00004", "Giovanna", "PartidoD", "vereador"),
        Candidato("00005", "Leticia", "PartidoE", "vereador"),
        Candidato("00006", "Vitor", "PartidoF", "vereador"),
        Candidato("00007", "Matheus", "PartidoG", "vereador"),
        Candidato("00008", "Rosa", "PartidoH", "vereador"),
        Candidato("00009", "Joao", "PartidoI", "vereador"),
        Candidato("00010", "Denis", "PartidoJ", "vereador"),
    ]

    zerar_votos(prefeitos + vereadores)
    while True:
        print("\n------ Menu Principal ------")
        print("1. Iniciar Votação")
        print("2. Listar Candidatos")
        print("3. Mostrar Resultados")
        print("4. Zerar Votos")
        print("0. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
           iniciar_votacao(prefeitos + vereadores)
        elif escolha == "2":
            listar_candidatos(prefeitos + vereadores)
        elif escolha == "3":
            mostrar_resultados(prefeitos, vereadores)
        elif escolha == "4":
            zerar_votos(prefeitos + vereadores)
        elif escolha == "5":
            apurar_votos(prefeitos + vereadores)
        elif escolha == "0":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

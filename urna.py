from utils import cadastrar_candidato, zerar_votos, votacao, cadastrar_prefeitos_auto, cadastrar_vereadores_auto, listar_candidatos, mostrar_resultados

prefeitos = cadastrar_prefeitos_auto()
vereadores = cadastrar_vereadores_auto()
def iniciar_urna():

    while True:
        print("\n------ Urna Eletrônica ------")
        print("1. Votar")
        print("2. Zerar Votos")
        print("3. Mostrar Resultados")
        print("4. Listar Candidatos")
        print("0. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            votacao(prefeitos, vereadores)
        elif escolha == "2":
            zerar_votos(prefeitos + vereadores)
        elif escolha == "3":
            mostrar_resultados(prefeitos, vereadores)
        elif escolha == "4":
            listar_candidatos(prefeitos, vereadores)
        elif escolha == "0":
            print("Saindo da Urna Eletrônica.")
            break
        else:
            print("Opção inválida. Tente novamente.")

    def votacao(prefeitos, vereadores):
        while True:
            cargo = input("Digite o cargo para votar (prefeito/vereador) ou '0' para sair: ").lower()

            if cargo == '0':
                print("Votação encerrada.")
                break

            candidatos = prefeitos if cargo == 'prefeito' else vereadores
            numero_candidato = input("Digite o número do candidato ou '0' para cancelar: ")

            if numero_candidato == '0':
                print("Votação cancelada.")
                continue

            candidato = encontrar_candidato(numero_candidato, candidatos)

            if candidato:
                candidato.votos += 1
                print(f"Voto registrado para {candidato.nome} ({candidato.partido}).")
            else:
                print("Número de candidato inválido. Tente novamente.")
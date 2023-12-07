# classe de Candidato
class Candidato:
    def __init__(self, numero, nome, partido, cargo):
        self.numero = numero
        self.nome = nome
        self.partido = partido
        self.cargo = cargo  # 'prefeito' ou 'vereador'
        self.votos = []

    def adicionar_voto(self, eleitor):
        self.votos.append(eleitor)

    def zerar_votos(self):
        self.votos = []
        print(f"Zerésima realizada para {self.nome} ({self.partido}). Todos os votos foram resetados.")

def listar_candidatos(candidatos):
    print("\nLista de Prefeitos:")
    for candidato in candidatos:
        if candidato.cargo == "prefeito":
            print(f"Número: {candidato.numero}, Nome: {candidato.nome}, Partido: {candidato.partido}")
    print("\nLista de Vereadores:")
    for candidato in candidatos:
        if candidato.cargo == "vereador":
            print(f"Número: {candidato.numero}, Nome: {candidato.nome}, Partido: {candidato.partido}")

def zerar_votos(candidatos):
    for candidato in candidatos:
        candidato.zerar_votos()

    print("Zerésima realizada. Todos os votos foram resetados.")

def iniciar_votacao(candidatos):
    while True:
        print("\n------ Votação ------")
        print("Escolha o tipo de votação:")
        print("1. Prefeito")
        print("2. Vereador")
        print("0. Finalizar")
        opcao = input("Digite o número da opção desejada: ")

        if opcao == '0':
            print("Votação finalizada.")
            return None

        elif opcao == '1' or opcao == '2':
            cargo = "prefeito" if opcao == '1' else "vereador"
            numero_candidato = input("Digite o número do candidato ou '0' para cancelar: ")

            if numero_candidato == '0':
                print("Votação cancelada.")
                return None

            candidato = next((c for c in candidatos if c.numero == numero_candidato and c.cargo == cargo), None)

            if candidato:
                print(f"\nCandidato encontrado:")
                print(f"Nome: {candidato.nome}")
                confirmacao = input("Digite 'S' para confirmar, 'N' para continuar votando ou '0' para cancelar: ").upper()

                if confirmacao == 'S':
                    eleitor = input("Digite o número do eleitor: ")
                    candidato.adicionar_voto(eleitor)  # Correção: Passando o argumento eleitor
                    print(f"Voto registrado para {candidato.nome} ({candidato.partido}).")

                elif confirmacao == '0':
                    print("Votação cancelada.")
                    return None

                continuar_votando = input("Deseja continuar votando? (S para sim, N para não): ").upper()

                if continuar_votando != 'S':
                    print("Votação encerrada.")
                    return None

            else:
                print("Número de candidato inválido ou cargo incorreto. Tente novamente.")

        else:
            print("Opção inválida. Tente novamente.")
def apurar_votos(resultados):
    resultados_ordenados = sorted(resultados, key=lambda x: x['votos'], reverse=True)

    eleitos = []
    segundo_turno = False

    for candidato in resultados_ordenados:
        if candidato['votos'] > 0:
            eleitos.append(candidato['nome'])

        if len(eleitos) == 2 and eleitos[0] == eleitos[1]:
            segundo_turno = True
            break

    return eleitos, segundo_turno

def mostrar_resultados(resultados_prefeitos, resultados_vereadores):
    prefeito_eleito, segundo_turno_prefeito = apurar_votos(resultados_prefeitos)
    vereadores_eleitos = apurar_votos(resultados_vereadores, cargo='vereador')

    print("\n------ Resultados ------")
    
    print("\nPrefeitos:")
    for resultado in resultados_prefeitos:
        print(f"  {resultado['nome']} ({resultado['cargo']}): {resultado['votos']} votos")

    print("\nVereadores:")
    for resultado in resultados_vereadores:
        print(f"  {resultado['nome']} ({resultado['cargo']}): {resultado['votos']} votos")

    print("\n------ Eleitos ------")

    print("\nPrefeito Eleito:")
    if segundo_turno_prefeito:
        print("Segundo turno necessário.")
    else:
        print(prefeito_eleito['nome'] if prefeito_eleito else "Nenhum eleito.")

    print("\nVereadores Eleitos:")
    for vereador in vereadores_eleitos:
        print(f"  {vereador['nome']} ({vereador['cargo']}): {vereador['votos']} votos")

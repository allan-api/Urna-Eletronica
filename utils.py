# No arquivo utils.py

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

def contabilizar_votos(candidatos):
    resultados = []
    for candidato in candidatos:
        resultados.append({
            'numero': candidato.numero,
            'nome': candidato.nome,
            'cargo': candidato.cargo,
            'votos': len(candidato.votos)
        })
    return resultados

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
                confirmacao = input("Digite 'S' para confirmar: ").upper()

                if confirmacao == 'S':
                    eleitor = input("Digite o número do eleitor: ")
                    candidato.adicionar_voto(eleitor)  # Aqui é onde o voto é registrado
                    print(f"Voto registrado para {candidato.nome} ({candidato.partido}).")
                    continuar = input("Deseja continuar votando? (S para sim, N para não): ").upper()
                    if continuar != 'S':
                        print("Votação encerrada.")
                        return None
                else:
                    print("Votação cancelada.")
            else:
                print("Número de candidato inválido ou cargo incorreto. Tente novamente.")
        else:
            print("Opção inválida. Tente novamente.")

def mostrar_resultados(prefeitos, vereadores):
    resultados_prefeitos = contabilizar_votos(prefeitos)
    resultados_vereadores = contabilizar_votos(vereadores)

    resultados = {'prefeitos': resultados_prefeitos, 'vereadores': resultados_vereadores}

    print("\n------ Resultados ------")

    print("Prefeitos:")
    for resultado in resultados_prefeitos:
        print(f"  {resultado['nome']}: {resultado['votos']} votos")

    print("\nVereadores:")
    for resultado in resultados_vereadores:
        print(f"  {resultado['nome']}: {resultado['votos']} votos")

    opcao_apurar = input("\n1. Apurar votos\n0. Cancelar\nEscolha uma opção: ")

    if opcao_apurar == "1":
           apurar_votos(resultados)

        
    elif opcao_apurar == "0":
        print("Operação Cancelada.")
    else:
        print("Opção inválida.")
def apurar_votos(resultados):
    prefeitos_ordenados = sorted(resultados['prefeitos'], key=lambda x: x['votos'], reverse=True)
    vereadores_ordenados = sorted(resultados['vereadores'], key=lambda x: x['votos'], reverse=True)

    # Verifica se o prefeito eleito tem pelo menos um voto
    prefeito_eleito = prefeitos_ordenados[0]
    segundo_colocado = prefeitos_ordenados[1]

    if prefeito_eleito['votos'] > 0:
        print("\nPrefeito Eleito:")
        print(f"{prefeito_eleito['nome']} ({prefeito_eleito['cargo']}): {prefeito_eleito['votos']} votos")

        # Verifica se há empate entre os prefeitos mais votados
        if prefeito_eleito['votos'] == segundo_colocado['votos']:
            print(f"\nEmpate entre {prefeito_eleito['nome']} e {segundo_colocado['nome']}. Segundo turno necessário.")
            return None, None  # Retorna None, indicando a necessidade de segundo turno
    else:
        print("\nNenhum prefeito foi votado. A eleição é inválida.")
        return None, None

    # Verifica se pelo menos um vereador foi eleito
    vereadores_eleitos = [v for v in vereadores_ordenados if v['votos'] > 0][:10]
    if vereadores_eleitos:
        print("\nVereadores Eleitos:")
        for vereador in vereadores_eleitos:
            print(f"{vereador['nome']} ({vereador['cargo']}): {vereador['votos']} votos")
    else:
        print("\nNenhum vereador foi votado. A eleição é inválida.")
        return None, None

    return prefeito_eleito, vereadores_eleitos

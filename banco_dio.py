import json
import banco_interface

# Função para carregar os dados dos usuários do arquivo JSON


def carregar_usuarios():
    try:
        with open("usuarios.json", 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return {}

# Função para salvar os dados dos usuários no arquivo JSON


def salvar_usuarios(usuarios):
    with open("usuarios.json", 'w') as arquivo:
        json.dump(usuarios, arquivo)

# Função para carregar os dados das contas correntes do arquivo JSON


def carregar_contas_correntes():
    try:
        with open("contas_correntes.json", 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []

# Função para salvar os dados das contas correntes no arquivo JSON


def salvar_contas_correntes(contas_correntes):
    with open("contas_correntes.json", 'w') as arquivo:
        json.dump(contas_correntes, arquivo)

# Função para depositar em uma conta corrente


def depositar(numero_conta, valor):
    contas_correntes = carregar_contas_correntes()
    for conta in contas_correntes:
        if conta['numero_conta'] == numero_conta:
            conta['saldo'] += valor
            conta['extrato'] += f"Depósito: R$ {valor:.2f}\n"
            break
    salvar_contas_correntes(contas_correntes)

# Função para sacar de uma conta corrente


def sacar(numero_conta, valor):
    contas_correntes = carregar_contas_correntes()
    for conta in contas_correntes:
        if conta['numero_conta'] == numero_conta:
            if valor > conta['saldo']:
                print("Operação falhou! Você não tem saldo suficiente.")
            else:
                conta['saldo'] -= valor
                conta['extrato'] += f"Saque: R$ {valor:.2f}\n"
            break
    salvar_contas_correntes(contas_correntes)

# Função para exibir o extrato de uma conta corrente


def extrato(numero_conta):
    contas_correntes = carregar_contas_correntes()
    for conta in contas_correntes:
        if conta['numero_conta'] == numero_conta:
            print("\n================ EXTRATO ================")
            print(
                "Não foram realizadas movimentações." if not conta['extrato'] else conta['extrato'])
            print(f"\nSaldo: R$ {conta['saldo']:.2f}")
            print("==========================================")
            break

# Função para criar uma conta corrente


def criar_conta_corrente(usuario):
    contas_correntes = carregar_contas_correntes()
    numero_conta = str(len(contas_correntes) + 1)
    contas_correntes.append({
        "agencia": "0001",
        "numero_conta": numero_conta,
        "usuario": usuario,
        "saldo": 0,
        "limite": 500,
        "extrato": "",
        "numero_saques": 0,
        "LIMITE_SAQUES": 3
    })
    salvar_contas_correntes(contas_correntes)
    return numero_conta

# Função para criar um usuário


def criar_usuario(nome, cpf, data_nascimento, endereco):
    usuarios = carregar_usuarios()
    cpf = cpf.replace(".", "").replace("-", "")
    if cpf in usuarios:
        print("CPF já cadastrado.")
    else:
        usuarios[cpf] = {
            "nome": nome,
            "cpf": cpf,
            "data_nascimento": data_nascimento,
            "endereco": endereco
        }
        salvar_usuarios(usuarios)
        print("Usuário cadastrado com sucesso.")

# Função para listar todas as contas correntes


def listar_contas():
    contas_correntes = carregar_contas_correntes()
    print("\n================ CONTAS CORRENTES ================")
    for conta in contas_correntes:
        print(
            f"Agência: {conta['agencia']} - Conta: {conta['numero_conta']} - Cliente: {conta['usuario']['nome']}")
    print("===================================================")


# Chamar a função main
if __name__ == "__main__":
    banco_interface.main()

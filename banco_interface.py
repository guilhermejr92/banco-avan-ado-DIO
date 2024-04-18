import tkinter as tk
from tkinter import messagebox
import banco_dio

# Função para depositar


def depositar():
    valor_str = entry_valor.get()
    if valor_str.strip() != "":  # Verifica se o campo não está vazio
        # Converte para float apenas se não estiver vazio
        valor = float(valor_str)
        banco_dio.depositar(entry_numero_conta.get(), valor)
    else:
        messagebox.showerror("Erro", "Por favor, insira um valor válido.")

# Função para sacar


def sacar():
    valor_str = entry_valor.get()
    if valor_str.strip() != "":  # Verifica se o campo não está vazio
        # Converte para float apenas se não estiver vazio
        valor = float(valor_str)
        banco_dio.sacar(entry_numero_conta.get(), valor)
    else:
        messagebox.showerror("Erro", "Por favor, insira um valor válido.")

# Função para exibir o extrato


def extrato():
    numero_conta_str = entry_numero_conta.get()
    if numero_conta_str.strip() != "":
        banco_dio.extrato(numero_conta_str)
    else:
        messagebox.showerror(
            "Erro", "Por favor, insira um número de conta válido.")

# Função para criar uma conta corrente


def criar_conta_corrente():
    nome_usuario_str = entry_nome_usuario.get()
    if nome_usuario_str.strip() != "":
        banco_dio.criar_conta_corrente(nome_usuario_str)
    else:
        messagebox.showerror(
            "Erro", "Por favor, insira um nome de usuário válido.")

# Função para criar um usuário


def criar_usuario():
    nome_str = entry_nome.get()
    cpf_str = entry_cpf.get()
    data_nascimento_str = entry_data_nascimento.get()
    endereco_str = entry_endereco.get()

    if nome_str.strip() != "" and cpf_str.strip() != "" and data_nascimento_str.strip() != "" and endereco_str.strip() != "":
        banco_dio.criar_usuario(
            nome_str, cpf_str, data_nascimento_str, endereco_str)
    else:
        messagebox.showerror("Erro", "Por favor, preencha todos os campos.")


# Criar janela principal
root = tk.Tk()
root.title("Sistema Bancário")

# Criar widgets de entrada e rótulos para cada operação
tk.Label(root, text="Número da Conta:").pack()
entry_numero_conta = tk.Entry(root)
entry_numero_conta.pack()

tk.Label(root, text="Valor:").pack()
entry_valor = tk.Entry(root)
entry_valor.pack()

tk.Label(root, text="Nome do Usuário:").pack()
entry_nome_usuario = tk.Entry(root)
entry_nome_usuario.pack()

tk.Label(root, text="Nome:").pack()
entry_nome = tk.Entry(root)
entry_nome.pack()

tk.Label(root, text="CPF:").pack()
entry_cpf = tk.Entry(root)
entry_cpf.pack()

tk.Label(root, text="Data de Nascimento:").pack()
entry_data_nascimento = tk.Entry(root)
entry_data_nascimento.pack()

tk.Label(root, text="Endereço:").pack()
entry_endereco = tk.Entry(root)
entry_endereco.pack()

# Criar botões para as operações
btn_depositar = tk.Button(root, text="Depositar", command=depositar)
btn_depositar.pack()

btn_sacar = tk.Button(root, text="Sacar", command=sacar)
btn_sacar.pack()

btn_extrato = tk.Button(root, text="Extrato", command=extrato)
btn_extrato.pack()

btn_criar_conta_corrente = tk.Button(
    root, text="Criar Conta Corrente", command=criar_conta_corrente)
btn_criar_conta_corrente.pack()

btn_criar_usuario = tk.Button(
    root, text="Criar Usuário", command=criar_usuario)
btn_criar_usuario.pack()

# Iniciar o loop de eventos
root.mainloop()

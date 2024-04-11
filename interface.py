import funcs
import tkinter as tk
from tkinter import messagebox

# Função para fechar o programa completamente
def close_program():
    root.destroy()

# Função para abrir a janela de adicionar dados
def open_adicionar_dados():
    root.withdraw()  # Oculta a janela atual
    adicionar_dados_window.deiconify()  # Exibe a nova janela

# Função para fechar a janela de adicionar dados
def close_adicionar_dados():
    adicionar_dados_window.withdraw()  # Oculta a janela de adicionar dados
    root.deiconify()  # Exibe a janela principal novamente

# Função para abrir a janela de conferir dados
def open_conferir_dados():
    root.withdraw()  # Oculta a janela atual
    conferir_dados_window.deiconify()  # Exibe a nova janela

# Função para fechar a janela de conferir dados
def close_conferir_dados():
    conferir_dados_window.withdraw()  # Oculta a janela de conferir dados
    root.deiconify()  # Exibe a janela principal novamente

# Função para abrir a janela de conferir dados
def open_remover_dados():
    root.withdraw()  # Oculta a janela atual
    remover_dados_window.deiconify()  # Exibe a nova janela

# Função para fechar a janela de conferir dados
def close_remover_dados():
    remover_dados_window.withdraw()  # Oculta a janela de conferir dados
    root.deiconify()  # Exibe a janela principal novamente

# Função para aumentar o tamanho da fonte
def aumentar_fonte(fonte, tamanho):
    return (fonte, int(tamanho * 1.2))


def cadastrar_fornecedor(cnpj_entry, nome_entry, telefone_entry, email_entry):
    cnpj = cnpj_entry.get()
    nome_fornecedor = nome_entry.get()
    telefone = telefone_entry.get()
    email = email_entry.get()
    funcs.cadastrar_fornecedor(cnpj, nome_fornecedor, telefone, email)
    messagebox.showinfo("Sucesso", "Fornecedor cadastrado com sucesso!")



def limpar_campos_funcionarios(cpf_entry, nome_entry, cargo_entry, salario_entry):
    cpf_entry.delete(0, tk.END)
    nome_entry.delete(0, tk.END)
    cargo_entry.delete(0, tk.END)
    salario_entry.delete(0, tk.END)

def limpar_campos_fornecedor(cnpj_entry, nome_entry, telefone_entry, email_entry):
    cnpj_entry.delete(0, tk.END)
    nome_entry.delete(0, tk.END)
    telefone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)

def limpar_campos_mercado(cnpj_entry, nome_entry, telefone_entry):
    cnpj_entry.delete(0, tk.END)
    nome_entry.delete(0, tk.END)
    telefone_entry.delete(0, tk.END)

def limpar_campos_pedido(id_pedido_entry, id_produto_entry, cnpj_mercado_entry, cpf_cliente_entry, quantidade_produto_entry, subtotal_entry):
    id_pedido_entry.delete(0, tk.END)
    id_produto_entry.delete(0, tk.END)
    cnpj_mercado_entry.delete(0, tk.END)
    cpf_cliente_entry.delete(0, tk.END)
    quantidade_produto_entry.delete(0, tk.END)
    subtotal_entry.delete(0, tk.END)

def limpar_campos_nota(id_pedido_entry, cpf_cliente_entry, data_pedido_entry, id_endereco_entry, preco_total_entry, forma_pagamento_entry, status_pedido_entry):
    id_pedido_entry.delete(0, tk.END)
    cpf_cliente_entry.delete(0, tk.END)
    data_pedido_entry.delete(0, tk.END)
    id_endereco_entry.delete(0, tk.END)
    preco_total_entry.delete(0, tk.END)
    forma_pagamento_entry.delete(0, tk.END)
    status_pedido_entry.delete(0, tk.END)

def limpar_campos_endereco(id_endereco_entry, cnpj_cpf_residente_entry, cep_entry, logradouro_entry, numero_entry, complemento_entry):
    id_endereco_entry.delete(0, tk.END)
    cnpj_cpf_residente_entry.delete(0, tk.END)
    cep_entry.delete(0, tk.END)
    logradouro_entry.delete(0, tk.END)
    numero_entry.delete(0, tk.END)
    complemento_entry.delete(0, tk.END)

def limpar_campos_produto(id_produto_entry, cnpj_fornecedor_entry, descricao_entry, categoria_entry, preco_entry):
    id_produto_entry.delete(0, tk.END)
    cnpj_fornecedor_entry.delete(0, tk.END)
    descricao_entry.delete(0, tk.END)
    categoria_entry.delete(0, tk.END)
    preco_entry.delete(0, tk.END)

def limpar_campos_cliente(cpf_entry, nome_entry, telefone_entry, email_entry, data_cadastro_entry):
    cpf_entry.delete(0, tk.END)
    nome_entry.delete(0, tk.END)
    telefone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    data_cadastro_entry.delete(0, tk.END)

def limpar_campos_lote(id_lote_entry, cnpj_unidade_entry, id_produto_entry, quantidade_estoque_entry, data_validade_entry, data_atualizacao_entry):
    id_lote_entry.delete(0, tk.END)
    cnpj_unidade_entry.delete(0, tk.END)
    id_produto_entry.delete(0, tk.END)
    quantidade_estoque_entry.delete(0, tk.END)
    data_validade_entry.delete(0, tk.END)
    data_atualizacao_entry.delete(0, tk.END)


def cadastrar_fornecedor_interno():
    root = tk.Tk()
    root.title("Cadastro de Fornecedor")

    # Labels
    tk.Label(root, text="CNPJ:").grid(row=0, column=0, sticky="w")
    tk.Label(root, text="Nome:").grid(row=1, column=0, sticky="w")
    tk.Label(root, text="Telefone:").grid(row=2, column=0, sticky="w")
    tk.Label(root, text="Email:").grid(row=3, column=0, sticky="w")
    
    cnpj_entry = tk.Entry(root)
    cnpj_entry.grid(row=0, column=1)
    nome_entry = tk.Entry(root)
    nome_entry.grid(row=1, column=1)
    telefone_entry = tk.Entry(root)
    telefone_entry.grid(row=2, column=1)
    email_entry = tk.Entry(root)
    email_entry.grid(row=3, column=1)

    # Buttons
    cadastrar_btn = tk.Button(root, text="Cadastrar", command=cadastrar_fornecedor(cnpj_entry, nome_entry, telefone_entry, email_entry))
    cadastrar_btn.grid(row=4, column=0, columnspan=2, pady=10)
    limpar_btn = tk.Button(root, text="Limpar", command=limpar_campos_fornecedor)
    limpar_btn.grid(row=5, column=0, columnspan=2)

    root.mainloop()


def cadastrar_mercado_interno():
    root = tk.Tk()
    root.title("Cadastro de Mercado")

    # Labels
    tk.Label(root, text="CNPJ:").grid(row=0, column=0, sticky="w")
    tk.Label(root, text="Nome Estabelecimento:").grid(row=1, column=0, sticky="w")
    tk.Label(root, text="Telefone:").grid(row=2, column=0, sticky="w")
    
    cnpj_entry = tk.Entry(root)
    cnpj_entry.grid(row=0, column=1)
    nome_estabelecimento_entry = tk.Entry(root)
    nome_estabelecimento_entry.grid(row=1, column=1)
    telefone_entry = tk.Entry(root)
    telefone_entry.grid(row=2, column=1)

    # Buttons
    cadastrar_btn = tk.Button(root, text="Cadastrar", command=lambda: funcs.cadastrar_mercado(
        cnpj_entry.get(), nome_estabelecimento_entry.get(), telefone_entry.get()))
    cadastrar_btn.grid(row=3, column=0, columnspan=2, pady=10)
    limpar_btn = tk.Button(root, text="Limpar", command=lambda: limpar_campos_mercado(cnpj_entry, nome_estabelecimento_entry, telefone_entry))
    limpar_btn.grid(row=4, column=0, columnspan=2)

    root.mainloop()




def cadastrar_produto_interno():
    root = tk.Tk()
    root.title("Cadastro de Produto")

    # Labels
    tk.Label(root, text="ID Produto:").grid(row=0, column=0, sticky="w")
    tk.Label(root, text="CNPJ Fornecedor:").grid(row=1, column=0, sticky="w")
    tk.Label(root, text="Descrição:").grid(row=2, column=0, sticky="w")
    tk.Label(root, text="Categoria:").grid(row=3, column=0, sticky="w")
    tk.Label(root, text="Preço:").grid(row=4, column=0, sticky="w")
    
    id_produto_entry = tk.Entry(root)
    id_produto_entry.grid(row=0, column=1)
    cnpj_fornecedor_entry = tk.Entry(root)
    cnpj_fornecedor_entry.grid(row=1, column=1)
    descricao_entry = tk.Entry(root)
    descricao_entry.grid(row=2, column=1)
    categoria_entry = tk.Entry(root)
    categoria_entry.grid(row=3, column=1)
    preco_entry = tk.Entry(root)
    preco_entry.grid(row=4, column=1)

    # Buttons
    cadastrar_btn = tk.Button(root, text="Cadastrar", command=lambda: funcs.cadastrar_produto(
        id_produto_entry.get(), cnpj_fornecedor_entry.get(), descricao_entry.get(), categoria_entry.get(), preco_entry.get()))
    cadastrar_btn.grid(row=5, column=0, columnspan=2, pady=10)
    limpar_btn = tk.Button(root, text="Limpar", command=lambda: limpar_campos_produto(
        id_produto_entry, cnpj_fornecedor_entry, descricao_entry, categoria_entry, preco_entry))
    limpar_btn.grid(row=6, column=0, columnspan=2)

    root.mainloop()
    
    
def cadastrar_pedido_interno():
    root = tk.Tk()
    root.title("Cadastro de Pedido")

    # Labels
    tk.Label(root, text="ID Pedido:").grid(row=0, column=0, sticky="w")
    tk.Label(root, text="ID Produto:").grid(row=1, column=0, sticky="w")
    tk.Label(root, text="CNPJ Mercado:").grid(row=2, column=0, sticky="w")
    tk.Label(root, text="CPF Cliente:").grid(row=3, column=0, sticky="w")
    tk.Label(root, text="Quantidade Produto:").grid(row=4, column=0, sticky="w")
    tk.Label(root, text="Subtotal:").grid(row=5, column=0, sticky="w")
    
    id_pedido_entry = tk.Entry(root)
    id_pedido_entry.grid(row=0, column=1)
    id_produto_entry = tk.Entry(root)
    id_produto_entry.grid(row=1, column=1)
    cnpj_mercado_entry = tk.Entry(root)
    cnpj_mercado_entry.grid(row=2, column=1)
    cpf_cliente_entry = tk.Entry(root)
    cpf_cliente_entry.grid(row=3, column=1)
    quantidade_produto_entry = tk.Entry(root)
    quantidade_produto_entry.grid(row=4, column=1)
    subtotal_entry = tk.Entry(root)
    subtotal_entry.grid(row=5, column=1)

    # Buttons
    cadastrar_btn = tk.Button(root, text="Cadastrar", command=lambda: funcs.cadastrar_pedido(
        id_pedido_entry.get(), id_produto_entry.get(), cnpj_mercado_entry.get(),
        cpf_cliente_entry.get(), quantidade_produto_entry.get(), subtotal_entry.get()))
    cadastrar_btn.grid(row=6, column=0, columnspan=2, pady=10)
    limpar_btn = tk.Button(root, text="Limpar", command=lambda: limpar_campos_pedido(
        id_pedido_entry, id_produto_entry, cnpj_mercado_entry,
        cpf_cliente_entry, quantidade_produto_entry, subtotal_entry))
    limpar_btn.grid(row=7, column=0, columnspan=2)

    root.mainloop()

 
def cadastrar_cliente_interno():
    root = tk.Tk()
    root.title("Cadastro de Cliente")

    # Labels
    tk.Label(root, text="CPF:").grid(row=0, column=0, sticky="w")
    tk.Label(root, text="Nome do Cliente:").grid(row=1, column=0, sticky="w")
    tk.Label(root, text="Telefone:").grid(row=2, column=0, sticky="w")
    tk.Label(root, text="Email:").grid(row=3, column=0, sticky="w")
    tk.Label(root, text="Data de Cadastro:").grid(row=4, column=0, sticky="w")
    
    cpf_entry = tk.Entry(root)
    cpf_entry.grid(row=0, column=1)
    nome_cliente_entry = tk.Entry(root)
    nome_cliente_entry.grid(row=1, column=1)
    telefone_entry = tk.Entry(root)
    telefone_entry.grid(row=2, column=1)
    email_entry = tk.Entry(root)
    email_entry.grid(row=3, column=1)
    data_cadastro_entry = tk.Entry(root)
    data_cadastro_entry.grid(row=4, column=1)

    # Buttons
    cadastrar_btn = tk.Button(root, text="Cadastrar", command=lambda: funcs.cadastrar_cliente(
        cpf_entry.get(), nome_cliente_entry.get(), telefone_entry.get(), email_entry.get(), data_cadastro_entry.get()))
    cadastrar_btn.grid(row=5, column=0, columnspan=2, pady=10)
    limpar_btn = tk.Button(root, text="Limpar", command=lambda: limpar_campos_cliente(
        cpf_entry, nome_cliente_entry, telefone_entry, email_entry, data_cadastro_entry))
    limpar_btn.grid(row=6, column=0, columnspan=2)

    root.mainloop()


def cadastrar_lote_interno():
    root = tk.Tk()
    root.title("Cadastro de Lote")

    # Labels
    tk.Label(root, text="ID do Lote:").grid(row=0, column=0, sticky="w")
    tk.Label(root, text="CNPJ da Unidade:").grid(row=1, column=0, sticky="w")
    tk.Label(root, text="ID do Produto:").grid(row=2, column=0, sticky="w")
    tk.Label(root, text="Quantidade em Estoque:").grid(row=3, column=0, sticky="w")
    tk.Label(root, text="Data de Validade:").grid(row=4, column=0, sticky="w")
    tk.Label(root, text="Data de Atualização:").grid(row=5, column=0, sticky="w")
    
    id_lote_entry = tk.Entry(root)
    id_lote_entry.grid(row=0, column=1)
    cnpj_unidade_entry = tk.Entry(root)
    cnpj_unidade_entry.grid(row=1, column=1)
    id_produto_entry = tk.Entry(root)
    id_produto_entry.grid(row=2, column=1)
    quantidade_estoque_entry = tk.Entry(root)
    quantidade_estoque_entry.grid(row=3, column=1)
    data_validade_entry = tk.Entry(root)
    data_validade_entry.grid(row=4, column=1)
    data_atualizacao_entry = tk.Entry(root)
    data_atualizacao_entry.grid(row=5, column=1)

    # Buttons
    cadastrar_btn = tk.Button(root, text="Cadastrar", command=lambda: funcs.cadastrar_lote(
        id_lote_entry.get(), cnpj_unidade_entry.get(), id_produto_entry.get(), quantidade_estoque_entry.get(), data_validade_entry.get(), data_atualizacao_entry.get()))
    cadastrar_btn.grid(row=6, column=0, columnspan=2, pady=10)
    limpar_btn = tk.Button(root, text="Limpar", command=lambda: limpar_campos_lote(
        id_lote_entry, cnpj_unidade_entry, id_produto_entry, quantidade_estoque_entry, data_validade_entry, data_atualizacao_entry))
    limpar_btn.grid(row=7, column=0, columnspan=2)

    root.mainloop()


def cadastrar_endereco_interno():
    root = tk.Tk()
    root.title("Cadastro de Endereço")

    # Labels
    tk.Label(root, text="ID do Endereço:").grid(row=0, column=0, sticky="w")
    tk.Label(root, text="CNPJ/CPF do Residente:").grid(row=1, column=0, sticky="w")
    tk.Label(root, text="CEP:").grid(row=2, column=0, sticky="w")
    tk.Label(root, text="Logradouro:").grid(row=3, column=0, sticky="w")
    tk.Label(root, text="Número:").grid(row=4, column=0, sticky="w")
    tk.Label(root, text="Complemento:").grid(row=5, column=0, sticky="w")
    
    id_endereco_entry = tk.Entry(root)
    id_endereco_entry.grid(row=0, column=1)
    cnpj_cpf_residente_entry = tk.Entry(root)
    cnpj_cpf_residente_entry.grid(row=1, column=1)
    cep_entry = tk.Entry(root)
    cep_entry.grid(row=2, column=1)
    logradouro_entry = tk.Entry(root)
    logradouro_entry.grid(row=3, column=1)
    numero_entry = tk.Entry(root)
    numero_entry.grid(row=4, column=1)
    complemento_entry = tk.Entry(root)
    complemento_entry.grid(row=5, column=1)

    # Buttons
    cadastrar_btn = tk.Button(root, text="Cadastrar", command=lambda: funcs.cadastrar_endereco(
        id_endereco_entry.get(), cnpj_cpf_residente_entry.get(), cep_entry.get(), logradouro_entry.get(), numero_entry.get(), complemento_entry.get()))
    cadastrar_btn.grid(row=6, column=0, columnspan=2, pady=10)
    limpar_btn = tk.Button(root, text="Limpar", command=lambda: limpar_campos_endereco(
        id_endereco_entry, cnpj_cpf_residente_entry, cep_entry, logradouro_entry, numero_entry, complemento_entry))
    limpar_btn.grid(row=7, column=0, columnspan=2)

    root.mainloop()

def cadastrar_nota_interno():
    root = tk.Tk()
    root.title("Cadastro de Nota")

    # Labels
    tk.Label(root, text="ID do Pedido:").grid(row=0, column=0, sticky="w")
    tk.Label(root, text="CPF do Cliente:").grid(row=1, column=0, sticky="w")
    tk.Label(root, text="Data do Pedido:").grid(row=2, column=0, sticky="w")
    tk.Label(root, text="ID do Endereço:").grid(row=3, column=0, sticky="w")
    tk.Label(root, text="Preço Total:").grid(row=4, column=0, sticky="w")
    tk.Label(root, text="Forma de Pagamento:").grid(row=5, column=0, sticky="w")
    tk.Label(root, text="Status do Pedido:").grid(row=6, column=0, sticky="w")
    
    id_pedido_entry = tk.Entry(root)
    id_pedido_entry.grid(row=0, column=1)
    cpf_cliente_entry = tk.Entry(root)
    cpf_cliente_entry.grid(row=1, column=1)
    data_pedido_entry = tk.Entry(root)
    data_pedido_entry.grid(row=2, column=1)
    id_endereco_entry = tk.Entry(root)
    id_endereco_entry.grid(row=3, column=1)
    preco_total_entry = tk.Entry(root)
    preco_total_entry.grid(row=4, column=1)
    forma_pagamento_entry = tk.Entry(root)
    forma_pagamento_entry.grid(row=5, column=1)
    status_pedido_entry = tk.Entry(root)
    status_pedido_entry.grid(row=6, column=1)

    # Buttons
    cadastrar_btn = tk.Button(root, text="Cadastrar", command=lambda: funcs.cadastrar_nota(
        id_pedido_entry.get(), cpf_cliente_entry.get(), data_pedido_entry.get(), id_endereco_entry.get(), preco_total_entry.get(), forma_pagamento_entry.get(), status_pedido_entry.get()))
    cadastrar_btn.grid(row=7, column=0, columnspan=2, pady=10)
    limpar_btn = tk.Button(root, text="Limpar", command=lambda: limpar_campos_nota(
        id_pedido_entry, cpf_cliente_entry, data_pedido_entry, id_endereco_entry, preco_total_entry, forma_pagamento_entry, status_pedido_entry))
    limpar_btn.grid(row=8, column=0, columnspan=2)

    root.mainloop()


def cadastrar_funcionario_interno():
    root = tk.Tk()
    root.title("Cadastro de Funcionário")

    # Labels
    tk.Label(root, text="ID do Funcionário:").grid(row=0, column=0, sticky="w")
    tk.Label(root, text="Nome do Funcionário:").grid(row=1, column=0, sticky="w")
    tk.Label(root, text="Cargo:").grid(row=2, column=0, sticky="w")
    tk.Label(root, text="Salário:").grid(row=3, column=0, sticky="w")
    
    id_funcionario_entry = tk.Entry(root)
    id_funcionario_entry.grid(row=0, column=1)
    nome_funcionario_entry = tk.Entry(root)
    nome_funcionario_entry.grid(row=1, column=1)
    cargo_entry = tk.Entry(root)
    cargo_entry.grid(row=2, column=1)
    salario_entry = tk.Entry(root)
    salario_entry.grid(row=3, column=1)

    # Buttons
    cadastrar_btn = tk.Button(root, text="Cadastrar", command=lambda: funcs.cadastrar_funcionario(
        id_funcionario_entry.get(), nome_funcionario_entry.get(), cargo_entry.get(), salario_entry.get()))
    cadastrar_btn.grid(row=4, column=0, columnspan=2, pady=10)
    limpar_btn = tk.Button(root, text="Limpar", command=lambda: limpar_campos_funcionarios(
        id_funcionario_entry, nome_funcionario_entry, cargo_entry, salario_entry))
    limpar_btn.grid(row=5, column=0, columnspan=2)

    root.mainloop()


def mostrar_resultado(resultado):
    if resultado:
        formatted_result = "\n".join([f"{key}: {value}" for key, value in resultado.items()])
        messagebox.showinfo("Resultado", f"Resultado da consulta:\n\n{formatted_result}")
    else:
        messagebox.showinfo("Resultado", "Nenhum resultado encontrado.")

def conferir_fornecedor_interno():
    root = tk.Tk()
    root.title("Conferir Fornecedor")

    # Labels
    tk.Label(root, text="CNPJ:").grid(row=0, column=0, sticky="w")

    cnpj_entry = tk.Entry(root)
    cnpj_entry.grid(row=0, column=1)

    # Button
    conferir_btn = tk.Button(root, text="Conferir", command=lambda: mostrar_resultado(funcs.conferir_fornecedor(cnpj_entry.get())))
    conferir_btn.grid(row=1, column=0, columnspan=2, pady=10)

    root.mainloop()

def conferir_mercado_interno():
    root = tk.Tk()
    root.title("Conferir Mercado")

    # Labels
    tk.Label(root, text="CNPJ:").grid(row=0, column=0, sticky="w")

    cnpj_entry = tk.Entry(root)
    cnpj_entry.grid(row=0, column=1)

    # Button
    conferir_btn = tk.Button(root, text="Conferir", command=lambda: mostrar_resultado(funcs.conferir_mercado(cnpj_entry.get())))
    conferir_btn.grid(row=1, column=0, columnspan=2, pady=10)

    root.mainloop()

def conferir_pedido_interno():
    root = tk.Tk()
    root.title("Conferir Pedido")

    # Labels
    tk.Label(root, text="ID do Pedido:").grid(row=0, column=0, sticky="w")
    tk.Label(root, text="ID do Produto:").grid(row=1, column=0, sticky="w")

    id_pedido_entry = tk.Entry(root)
    id_pedido_entry.grid(row=0, column=1)
    id_produto_entry = tk.Entry(root)
    id_produto_entry.grid(row=1, column=1)

    # Button
    conferir_btn = tk.Button(root, text="Conferir", command=lambda: mostrar_resultado(funcs.conferir_pedido(id_pedido_entry.get(), id_produto_entry.get())))
    conferir_btn.grid(row=2, column=0, columnspan=2, pady=10)

    root.mainloop()

def conferir_produto_interno():
    root = tk.Tk()
    root.title("Conferir Produto")

    # Labels
    tk.Label(root, text="ID Produto:").grid(row=0, column=0, sticky="w")

    id_produto_entry = tk.Entry(root)
    id_produto_entry.grid(row=0, column=1)

    # Button
    conferir_btn = tk.Button(root, text="Conferir", command=lambda: mostrar_resultado(funcs.conferir_produto(id_produto_entry.get())))
    conferir_btn.grid(row=1, column=0, columnspan=2, pady=10)

    root.mainloop()

def conferir_cliente_interno():
    root = tk.Tk()
    root.title("Conferir Cliente")

    # Labels
    tk.Label(root, text="CPF:").grid(row=0, column=0, sticky="w")

    cpf_entry = tk.Entry(root)
    cpf_entry.grid(row=0, column=1)

    # Button
    conferir_btn = tk.Button(root, text="Conferir", command=lambda: mostrar_resultado(funcs.conferir_cliente(cpf_entry.get())))
    conferir_btn.grid(row=1, column=0, columnspan=2, pady=10)

    root.mainloop()

def conferir_lote_interno():
    root = tk.Tk()
    root.title("Conferir Lote")

    # Labels
    tk.Label(root, text="ID do Lote:").grid(row=0, column=0, sticky="w")

    id_lote_entry = tk.Entry(root)
    id_lote_entry.grid(row=0, column=1)

    # Button
    conferir_btn = tk.Button(root, text="Conferir", command=lambda: mostrar_resultado(funcs.conferir_lote(id_lote_entry.get())))
    conferir_btn.grid(row=1, column=0, columnspan=2, pady=10)

    root.mainloop()

def conferir_endereco_interno():
    root = tk.Tk()
    root.title("Conferir Endereço")

    # Labels
    tk.Label(root, text="ID do Endereço:").grid(row=0, column=0, sticky="w")

    id_endereco_entry = tk.Entry(root)
    id_endereco_entry.grid(row=0, column=1)

    # Button
    conferir_btn = tk.Button(root, text="Conferir", command=lambda: mostrar_resultado(funcs.conferir_endereco(id_endereco_entry.get())))
    conferir_btn.grid(row=1, column=0, columnspan=2, pady=10)

    root.mainloop()

def conferir_nota_interno():
    root = tk.Tk()
    root.title("Conferir Nota")

    # Labels
    tk.Label(root, text="ID do Pedido:").grid(row=0, column=0, sticky="w")

    id_pedido_entry = tk.Entry(root)
    id_pedido_entry.grid(row=0, column=1)

    # Button
    conferir_btn = tk.Button(root, text="Conferir", command=lambda: mostrar_resultado(funcs.conferir_nota(id_pedido_entry.get())))
    conferir_btn.grid(row=1, column=0, columnspan=2, pady=10)

    root.mainloop()

def conferir_funcionarios_interno():
    root = tk.Tk()
    root.title("Conferir Funcionários")

    # Labels
    tk.Label(root, text="ID do Funcionário:").grid(row=0, column=0, sticky="w")

    id_funcionario_entry = tk.Entry(root)
    id_funcionario_entry.grid(row=0, column=1)

    # Button
    conferir_btn = tk.Button(root, text="Conferir", command=lambda: mostrar_resultado(funcs.conferir_funcionario(id_funcionario_entry.get())))
    conferir_btn.grid(row=1, column=0, columnspan=2, pady=10)

    root.mainloop()

def remover_nota_interno():
    root = tk.Tk()
    root.title("Remover Nota")

    # Labels
    tk.Label(root, text="ID do pedido:").grid(row=0, column=0, sticky="w")

    id_entry = tk.Entry(root)
    id_entry.grid(row=0, column=1)

    # Button
    remover_btn = tk.Button(root, text="Remover", command=lambda: funcs.remover_nota(id_entry.get()))
    remover_btn.grid(row=1, column=0, columnspan=2, pady=10)

    root.mainloop()

def remover_endereco_interno():
    root = tk.Tk()
    root.title("Remover Endereço")

    # Labels
    tk.Label(root, text="ID do endereço:").grid(row=0, column=0, sticky="w")

    id_entry = tk.Entry(root)
    id_entry.grid(row=0, column=1)

    # Button
    remover_btn = tk.Button(root, text="Remover", command=lambda: funcs.remover_endereco(id_entry.get()))
    remover_btn.grid(row=1, column=0, columnspan=2, pady=10)
    
def remover_fornecedor_interno():
    root = tk.Tk()
    root.title("Remover Fornecedor")

    # Labels
    tk.Label(root, text="CNPJ do fornecedor:").grid(row=0, column=0, sticky="w")

    cnpj_entry = tk.Entry(root)
    cnpj_entry.grid(row=0, column=1)

    # Button
    remover_btn = tk.Button(root, text="Remover", command=lambda: funcs.remover_fornecedor(cnpj_entry.get()))
    remover_btn.grid(row=1, column=0, columnspan=2, pady=10)

    root.mainloop()



# Função para remover um mercado do banco de dados
def remover_mercado_interno():
    root = tk.Tk()
    root.title("Remover Mercado")

    # Labels
    tk.Label(root, text="CNPJ do mercado:").grid(row=0, column=0, sticky="w")

    cnpj_entry = tk.Entry(root)
    cnpj_entry.grid(row=0, column=1)

    # Button
    remover_btn = tk.Button(root, text="Remover", command=lambda: funcs.remover_mercado(cnpj_entry.get()))
    remover_btn.grid(row=1, column=0, columnspan=2, pady=10)

    root.mainloop()



# Função para remover um pedido do banco de dados
def remover_pedido_interno():
    root = tk.Tk()
    root.title("Remover Pedido")

    # Labels
    tk.Label(root, text="ID do pedido:").grid(row=0, column=0, sticky="w")

    id_entry = tk.Entry(root)
    id_entry.grid(row=0, column=1)

    # Button
    remover_btn = tk.Button(root, text="Remover", command=lambda: funcs.remover_pedido(id_entry.get()))
    remover_btn.grid(row=1, column=0, columnspan=2, pady=10)

    root.mainloop()


# Função para remover um cliente do banco de dados
def remover_cliente_interno():
    root = tk.Tk()
    root.title("Remover Cliente")

    # Labels
    tk.Label(root, text="CPF do cliente:").grid(row=0, column=0, sticky="w")

    cpf_entry = tk.Entry(root)
    cpf_entry.grid(row=0, column=1)

    # Button
    remover_btn = tk.Button(root, text="Remover", command=lambda: funcs.remover_cliente(cpf_entry.get()))
    remover_btn.grid(row=1, column=0, columnspan=2, pady=10)

    root.mainloop()



# Função para remover um funcionário do banco de dados
def remover_funcionario_interno():
    root = tk.Tk()
    root.title("Remover Funcionário")

    # Labels
    tk.Label(root, text="CPF do funcionário:").grid(row=0, column=0, sticky="w")

    cpf_entry = tk.Entry(root)
    cpf_entry.grid(row=0, column=1)

    # Button
    remover_btn = tk.Button(root, text="Remover", command=lambda: funcs.remover_funcionario(cpf_entry.get()))
    remover_btn.grid(row=1, column=0, columnspan=2, pady=10)

    root.mainloop()



# Função para remover um produto do banco de dados
def remover_produto_interno():
    root = tk.Tk()
    root.title("Remover Produto")

    # Labels
    tk.Label(root, text="ID do produto:").grid(row=0, column=0, sticky="w")

    id_entry = tk.Entry(root)
    id_entry.grid(row=0, column=1)

    # Button
    remover_btn = tk.Button(root, text="Remover", command=lambda: funcs.remover_produto(id_entry.get()))
    remover_btn.grid(row=1, column=0, columnspan=2, pady=10)

    root.mainloop()


# Função para remover um lote de estoque do banco de dados
def remover_lote_estoque_interno():
    root = tk.Tk()
    root.title("Remover Lote de Estoque")

    # Labels
    tk.Label(root, text="ID do lote:").grid(row=0, column=0, sticky="w")

    id_entry = tk.Entry(root)
    id_entry.grid(row=0, column=1)

    # Button
    remover_btn = tk.Button(root, text="Remover", command=lambda: funcs.remover_lote_estoque(id_entry.get()))
    remover_btn.grid(row=1, column=0, columnspan=2, pady=10)

    root.mainloop()


# Janela principal
root = tk.Tk()
root.title("Banco de Dados Supermercados")
root.configure(background='white')
root.geometry("800x640")  # Define o tamanho da janela principal

# Nomes dos responsáveis
responsaveis = ["Gabriel Pereira", "Gabriel Vilas", "Henrique Corazza", "Lucas Papoti", "Miguel Schwengber"]
for nome in responsaveis:
    tk.Label(root, text=nome, font=aumentar_fonte("Helvetica", 8), bg="white").pack(side='bottom', anchor="sw", padx=10, pady=5)

# Título
titulo = tk.Label(root, text="Banco de Dados Supermercados", font=aumentar_fonte("Helvetica", 20), bg="white")
titulo.pack(pady=100)

# Botões
btn_adicionar_dados = tk.Button(root, text="Adicionar Dados", font=aumentar_fonte("Helvetica", 12), command=open_adicionar_dados)
btn_adicionar_dados.pack(pady=5)

btn_conferir_dados = tk.Button(root, text="Conferir Dados", font=aumentar_fonte("Helvetica", 12), command=open_conferir_dados)
btn_conferir_dados.pack(pady=5)

btn_conferir_dados = tk.Button(root, text="Remover Dados", font=aumentar_fonte("Helvetica", 12), command=open_remover_dados)
btn_conferir_dados.pack(pady=5)

# Janela para adicionar dados
adicionar_dados_window = tk.Toplevel(root)
adicionar_dados_window.title("Adicionar Elementos")
adicionar_dados_window.configure(background='white')
adicionar_dados_window.withdraw()  # Mantém a janela oculta inicialmente
adicionar_dados_window.geometry("800x640")  # Define o tamanho da janela

# Botão Voltar
btn_voltar_adicionar = tk.Button(adicionar_dados_window, text="Voltar", font=aumentar_fonte("Helvetica", 12), command=close_adicionar_dados)
btn_voltar_adicionar.pack(pady=10, padx=10, anchor='w')

# Título
titulo_adicionar = tk.Label(adicionar_dados_window, text="Adicionar Elementos", font=aumentar_fonte("Helvetica", 16), bg="white")
titulo_adicionar.pack(pady=50)

# Botões para cadastrar
btn_cadastrar_fornecedor = tk.Button(adicionar_dados_window, text="Cadastrar Fornecedor", font=aumentar_fonte("Helvetica", 12), command=cadastrar_fornecedor_interno)
btn_cadastrar_fornecedor.pack(pady=10)

btn_cadastrar_mercado = tk.Button(adicionar_dados_window, text="Cadastrar Mercado", font=aumentar_fonte("Helvetica", 12), command=cadastrar_mercado_interno)
btn_cadastrar_mercado.pack(pady=10)

btn_cadastrar_pedido = tk.Button(adicionar_dados_window, text="Cadastrar Pedido", font=aumentar_fonte("Helvetica", 12), command=cadastrar_pedido_interno)
btn_cadastrar_pedido.pack(pady=10)

btn_cadastrar_produto = tk.Button(adicionar_dados_window, text="Cadastrar Produto", font=aumentar_fonte("Helvetica", 12), command=cadastrar_produto_interno)
btn_cadastrar_produto.pack(pady=10)

btn_cadastrar_cliente = tk.Button(adicionar_dados_window, text="Cadastrar Cliente", font=aumentar_fonte("Helvetica", 12), command=cadastrar_cliente_interno)
btn_cadastrar_cliente.pack(pady=10)

btn_cadastrar_lote = tk.Button(adicionar_dados_window, text="Cadastrar Lote", font=aumentar_fonte("Helvetica", 12), command=cadastrar_lote_interno)
btn_cadastrar_lote.pack(pady=10)

btn_cadastrar_lote = tk.Button(adicionar_dados_window, text="Cadastrar Endereço", font=aumentar_fonte("Helvetica", 12), command=cadastrar_endereco_interno)
btn_cadastrar_lote.pack(pady=10)

btn_cadastrar_lote = tk.Button(adicionar_dados_window, text="Cadastrar Nota", font=aumentar_fonte("Helvetica", 12), command=cadastrar_nota_interno)
btn_cadastrar_lote.pack(pady=10)

btn_cadastrar_lote = tk.Button(adicionar_dados_window, text="Cadastrar Funcionario", font=aumentar_fonte("Helvetica", 12), command=cadastrar_funcionario_interno)
btn_cadastrar_lote.pack(pady=10)

# Janela para conferir dados
conferir_dados_window = tk.Toplevel(root)
conferir_dados_window.title("Conferir Tabelas")
conferir_dados_window.configure(background='white')
conferir_dados_window.withdraw()  # Mantém a janela oculta inicialmente
conferir_dados_window.geometry("800x640")  # Define o tamanho da janela


# Botão Voltar
btn_voltar_conferir = tk.Button(conferir_dados_window, text="Voltar", font=aumentar_fonte("Helvetica", 12), command=close_conferir_dados)
btn_voltar_conferir.pack(pady=10, padx=10, anchor='w')

# Título
titulo_conferir = tk.Label(conferir_dados_window, text="Conferir Tabelas", font=aumentar_fonte("Helvetica", 16), bg="white")
titulo_conferir.pack(pady=50)

# Botões para conferir
btn_conferir_fornecedor = tk.Button(conferir_dados_window, text="Conferir Fornecedor", font=aumentar_fonte("Helvetica", 12), command=conferir_fornecedor_interno)
btn_conferir_fornecedor.pack(pady=10)

btn_conferir_mercado = tk.Button(conferir_dados_window, text="Conferir Mercado", font=aumentar_fonte("Helvetica", 12), command=conferir_mercado_interno)
btn_conferir_mercado.pack(pady=10)

btn_conferir_pedido = tk.Button(conferir_dados_window, text="Conferir Pedido", font=aumentar_fonte("Helvetica", 12), command=conferir_pedido_interno)
btn_conferir_pedido.pack(pady=10)

btn_conferir_produto = tk.Button(conferir_dados_window, text="Conferir Produto", font=aumentar_fonte("Helvetica", 12), command=conferir_produto_interno)
btn_conferir_produto.pack(pady=10)

btn_conferir_cliente = tk.Button(conferir_dados_window, text="Conferir Cliente", font=aumentar_fonte("Helvetica", 12), command=conferir_cliente_interno)
btn_conferir_cliente.pack(pady=10)

btn_conferir_lote = tk.Button(conferir_dados_window, text="Conferir Lote", font=aumentar_fonte("Helvetica", 12), command=conferir_lote_interno)
btn_conferir_lote.pack(pady=10)

btn_conferir_lote = tk.Button(conferir_dados_window, text="Conferir Nota", font=aumentar_fonte("Helvetica", 12), command=conferir_nota_interno)
btn_conferir_lote.pack(pady=10)

btn_conferir_lote = tk.Button(conferir_dados_window, text="Conferir Endereço", font=aumentar_fonte("Helvetica", 12), command=conferir_endereco_interno)
btn_conferir_lote.pack(pady=10)

btn_conferir_lote = tk.Button(conferir_dados_window, text="Conferir Funcionarios", font=aumentar_fonte("Helvetica", 12), command=conferir_funcionarios_interno)
btn_conferir_lote.pack(pady=10)


# Janela para remover dados
remover_dados_window = tk.Toplevel(root)
remover_dados_window.title("Remover Elementos")
remover_dados_window.configure(background='white')
remover_dados_window.withdraw()  # Mantém a janela oculta inicialmente
remover_dados_window.geometry("800x640")  # Define o tamanho da janela


# Botão Voltar
btn_voltar_remover = tk.Button(remover_dados_window, text="Voltar", font=aumentar_fonte("Helvetica", 12), command=close_remover_dados)
btn_voltar_remover.pack(pady=10, padx=10, anchor='w')

# Título
titulo_remover = tk.Label(remover_dados_window, text="Remover Tabelas", font=aumentar_fonte("Helvetica", 16), bg="white")
titulo_remover.pack(pady=50)

#Botões para remover
btn_remover_fornecedor = tk.Button(remover_dados_window, text="Remover Fornecedor", font=aumentar_fonte("Helvetica", 12), command=remover_fornecedor_interno)
btn_remover_fornecedor.pack(pady=10)

btn_remover_mercado = tk.Button(remover_dados_window, text="Remover Mercado", font=aumentar_fonte("Helvetica", 12), command=remover_mercado_interno)
btn_remover_mercado.pack(pady=10)

btn_remover_pedido = tk.Button(remover_dados_window, text="Remover Pedido", font=aumentar_fonte("Helvetica", 12), command=remover_pedido_interno)
btn_remover_pedido.pack(pady=10)

btn_remover_produto = tk.Button(remover_dados_window, text="Remover Produto", font=aumentar_fonte("Helvetica", 12), command=remover_produto_interno)
btn_remover_produto.pack(pady=10)

btn_remover_cliente = tk.Button(remover_dados_window, text="Remover Cliente", font=aumentar_fonte("Helvetica", 12), command=remover_cliente_interno)
btn_remover_cliente.pack(pady=10)

btn_remover_lote = tk.Button(remover_dados_window, text="Remover Lote", font=aumentar_fonte("Helvetica", 12), command=remover_lote_estoque_interno)
btn_remover_lote.pack(pady=10)

btn_remover_lote = tk.Button(remover_dados_window, text="Remover Funcionarios", font=aumentar_fonte("Helvetica", 12), command=remover_funcionario_interno)
btn_remover_lote.pack(pady=10)

btn_remover_lote = tk.Button(remover_dados_window, text="Remover Endereço", font=aumentar_fonte("Helvetica", 12), command=remover_endereco_interno)
btn_remover_lote.pack(pady=10)

btn_remover_lote = tk.Button(remover_dados_window, text="Remover Nota", font=aumentar_fonte("Helvetica", 12), command=remover_nota_interno)
btn_remover_lote.pack(pady=10)


# Configurar a ação de fechar todas as janelas quando a janela principal for fechada
root.protocol("WM_DELETE_WINDOW", close_program)

root.mainloop()

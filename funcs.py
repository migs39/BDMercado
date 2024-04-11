import psycopg2
from tkinter import messagebox

# funcs.py

import psycopg2

def conectar_banco():
    # Conectar ao banco de dados
    try:
        conn = psycopg2.connect(
            dbname="db_Trabalho_BD", 
            user="postgres", 
            password="3121", 
            host="localhost",  # ou o endereço IP do seu servidor PostgreSQL
            port="5432"        # porta padrão do PostgreSQL
        )
        return conn
    except psycopg2.Error as e:
        print("Erro ao conectar ao banco de dados:", e)
        return None

# Função para cadastrar fornecedor
def cadastrar_fornecedor(cnpj, nome_fornecedor, telefone, email):
    conn = conectar_banco()
    if conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO fornecedores (cnpj, nome_fornecedor, telefone, email) VALUES (%s, %s, %s, %s)", (cnpj, nome_fornecedor, telefone, email))
        conn.commit()
        conn.close()

# Função para cadastrar mercado
def cadastrar_mercado(cnpj, nome_estabelecimento, telefone):
    conn = conectar_banco()
    if conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO mercado (cnpj, nome_estabelecimento, telefone) VALUES (%s, %s, %s)", (cnpj, nome_estabelecimento, telefone))
        conn.commit()
        conn.close()

# Função para cadastrar pedido
def cadastrar_pedido(id_pedido, id_produto, cnpj_mercado, cpf_cliente, quantidade_produto, subtotal):
    conn = conectar_banco()
    if conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO pedido (id_pedido, id_produto, cnpj_mercado, cpf_cliente, quantidade_produto, subtotal) VALUES (%s, %s, %s, %s, %s, %s)", (id_pedido, id_produto, cnpj_mercado, cpf_cliente, quantidade_produto, subtotal))
        conn.commit()
        conn.close()

# Função para cadastrar nota
def cadastrar_nota(id_pedido, cpf_cliente, data_pedido, id_endereco, preco_total, forma_pagamento, status_pedido):
    conn = conectar_banco()
    if conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO nota (id_pedido, cpf_cliente, data_pedido, id_endereco, preco_total, forma_pagamento, status_pedido) VALUES (%s, %s, %s, %s, %s, %s, %s)", (id_pedido, cpf_cliente, data_pedido, id_endereco, preco_total, forma_pagamento, status_pedido))
        conn.commit()
        conn.close()

# Função para cadastrar endereço
def cadastrar_endereco(id_endereco, cnpj_cpf_residente, cep, logradouro, numero, complemento):
    conn = conectar_banco()
    if conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO enderecos (id_endereco, cnpj_cpf_residente, cep, logradouro, numero, complemento) VALUES (%s, %s, %s, %s, %s, %s)", (id_endereco, cnpj_cpf_residente, cep, logradouro, numero, complemento))
        conn.commit()
        conn.close()

# Função para cadastrar produto
def cadastrar_produto(id_produto, cnpj_fornecedor, descricao, categoria, preco):
    conn = conectar_banco()
    if conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO produtos (id_produto, cnpj_fornecedor, descricao, categoria, preco) VALUES (%s, %s, %s, %s, %s)", (id_produto, cnpj_fornecedor, descricao, categoria, preco))
        conn.commit()
        conn.close()

# Função para cadastrar cliente
def cadastrar_cliente(cpf, nome_cliente, telefone, email, data_cadastro):
    conn = conectar_banco()
    if conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tabela_de_clientes (cpf, nome_cliente, telefone, email, data_cadastro) VALUES (%s, %s, %s, %s, %s)", (cpf, nome_cliente, telefone, email, data_cadastro))
        conn.commit()
        conn.close()

# Função para cadastrar lote
def cadastrar_lote(id_lote, cnpj_unidade, id_produto, quantidade_estoque, data_validade, data_atualizacao):
    conn = conectar_banco()
    if conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO controle_de_estoque (id_lote, cnpj_unidade, id_produto, quantidade_estoque, data_validade, data_atualizacao) VALUES (%s, %s, %s, %s, %s, %s)", (id_lote, cnpj_unidade, id_produto, quantidade_estoque, data_validade, data_atualizacao))
        conn.commit()
        conn.close()

# Função para conferir fornecedor
# def conferir_fornecedor(cnpj):
#     conn = conectar_banco()
#     if conn:
#         cursor = conn.cursor()
#         cursor.execute("SELECT * FROM fornecedores WHERE cnpj = %s", (cnpj,))
#         fornecedor = cursor.fetchone()
#         conn.close()
#         return fornecedor

def conferir_fornecedor(cnpj):
    conn = conectar_banco()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM fornecedores WHERE cnpj = %s", (cnpj,))
        fornecedor = cursor.fetchone()
        conn.close()
        
        if fornecedor:
            column_names = [col[0] for col in cursor.description]
            fornecedor_dict = {column_names[i]: fornecedor[i] for i in range(len(column_names))}
            return fornecedor_dict
        else:
            return None


# Função para conferir mercado
def conferir_mercado(cnpj):
    conn = conectar_banco()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM mercado WHERE cnpj = %s", (cnpj,))
        mercado = cursor.fetchone()
        conn.close()
    
        if mercado:
            column_names = [col[0] for col in cursor.description]
            mercado_dict = {column_names[i]: mercado[i] for i in range(len(column_names))}
            return mercado_dict
        else:
            return None

# Função para conferir pedido
def conferir_pedido(id_pedido, id_produto):
    conn = conectar_banco()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM pedido WHERE id_pedido = %s AND id_produto = %s", (id_pedido, id_produto))
        pedido = cursor.fetchone()
        conn.close()
    
        if pedido:
            column_names = [col[0] for col in cursor.description]
            pedido_dict = {column_names[i]: pedido[i] for i in range(len(column_names))}
            return pedido_dict
        else:
            return None

# Função para conferir nota
def conferir_nota(id_pedido):
    conn = conectar_banco()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM nota WHERE id_pedido = %s", (id_pedido,))
        nota = cursor.fetchone()
        conn.close()
        if nota:
            column_names = [col[0] for col in cursor.description]
            nota_dict = {column_names[i]: nota[i] for i in range(len(column_names))}
            return nota_dict
        else:
            return None

# Função para conferir endereço
def conferir_endereco(id_endereco):
    conn = conectar_banco()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM enderecos WHERE id_endereco = %s", (id_endereco,))
        endereco = cursor.fetchone()
        conn.close()
        if endereco:
            column_names = [col[0] for col in cursor.description]
            endereco_dict = {column_names[i]: endereco[i] for i in range(len(column_names))}
            return endereco_dict
        else:
            return None

# Função para conferir produto
def conferir_produto(id_produto):
    conn = conectar_banco()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM produtos WHERE id_produto = %s", (id_produto,))
        produto = cursor.fetchone()
        conn.close()
        if produto:
            column_names = [col[0] for col in cursor.description]
            produto_dict = {column_names[i]: produto[i] for i in range(len(column_names))}
            return produto_dict
        else:
            return None

# Função para conferir cliente
def conferir_cliente(cpf):
    conn = conectar_banco()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tabela_de_clientes WHERE cpf = %s", (cpf,))
        cliente = cursor.fetchone()
        conn.close()
        if cliente:
            column_names = [col[0] for col in cursor.description]
            cliente_dict = {column_names[i]: cliente[i] for i in range(len(column_names))}
            return cliente_dict
        else:
            return None

# Função para conferir lote
def conferir_lote(id_lote):
    conn = conectar_banco()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM controle_de_estoque WHERE id_lote = %s", (id_lote,))
        lote = cursor.fetchone()
        conn.close()
        if lote:
            column_names = [col[0] for col in cursor.description]
            lote_dict = {column_names[i]: lote[i] for i in range(len(column_names))}
            return lote_dict
        else:
            return None

# Função para conferir fun
def conferir_funcionarios(id_funcionarios):
    conn = conectar_banco()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM controle_de_estoque WHERE id_lote = %s", (id_funcionarios,))
        funcionario = cursor.fetchone()
        conn.close()
        if funcionario:
            column_names = [col[0] for col in cursor.description]
            funcionario_dict = {column_names[i]: funcionario[i] for i in range(len(column_names))}
            return funcionario_dict
        else:
            return None



            
# Funções para remove
# def remover_fornecedor():
#     print("Remover fornecedor")
#     conn = conectar_banco()
#     if conn:
#         cursor = conn.cursor()
#         cnpj = input("Digite o cnpj do fornecedor a ser removido:")
#         try:
#             cursor.execute("DELETE FROM fornecedores WHERE cnpj = %s", (cnpj,))
#             conn.commit()
#             print("Fornecedor removido com sucesso!")
#         except psycopg2.Error as e:
#             print("Erro ao remover fornecedor:", e)
#         finally:
#             conn.close()

# def remover_mercado():
#     print("Remover mercado")
#     conn = conectar_banco()
#     if conn:
#         cnpj = input("Digite o cnpj do mercado a ser removido:")
#         cursor = conn.cursor()
#         try:
#             cursor.execute("DELETE FROM mercado WHERE cnpj = %s", (cnpj,))
#             conn.commit()
#             print("Mercado removido com sucesso!")
#         except psycopg2.Error as e:
#             print("Erro ao remover mercado:", e)
#         finally:
#             conn.close()

# def remover_pedido():
#     print("Remover pedido")
#     conn = conectar_banco()
#     if conn:
#         id_pedido = input("Digite o id_pedido do pedido a ser removido:")
#         cursor = conn.cursor()
#         try:
#             cursor.execute("DELETE FROM pedido WHERE id_pedido = %s", (id_pedido,))
#             conn.commit()
#             print("Pedido removido com sucesso!")
#         except psycopg2.Error as e:
#             print("Erro ao remover pedido:", e)
#         finally:
#             conn.close()

# def remover_nota():
#     print("Remover nota")
#     conn = conectar_banco()
#     if conn:
#         id_pedido = input("Digite o id_pedido da nota a ser removido:")
#         cursor = conn.cursor()
#         try:
#             cursor.execute("DELETE FROM nota WHERE id_pedido = %s", (id_pedido,))
#             conn.commit()
#             print("Nota removida com sucesso!")
#         except psycopg2.Error as e:
#             print("Erro ao remover nota:", e)
#         finally:
#             conn.close()

def remover_nota(id_nota):
    conn = conectar_banco()
    if conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM notas WHERE id = %s", (id_nota,))
        conn.commit()  # Confirma a operação no banco de dados
        conn.close()
        messagebox.showinfo("Sucesso", "Nota removida com sucesso.")

        # opcional: se deseja tratar o caso onde nenhum registro foi deletado
        if cursor.rowcount == 0:
            messagebox.showinfo("Aviso", "Nenhuma nota encontrada com este ID.")
        
def remover_endereco(id_endereco):
    conn = conectar_banco()
    if conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Enderecos WHERE id_endereco = %s", (id_endereco,))
        conn.commit()  # Confirma a operação no banco de dados
        conn.close()
        messagebox.showinfo("Sucesso", "Endereço removido com sucesso.")

        # Opcional: tratar o caso onde nenhum registro foi deletado
        if cursor.rowcount == 0:
            messagebox.showinfo("Aviso", "Nenhum endereço encontrado com este ID.")

def remover_fornecedor(cnpj):
    conn = conectar_banco()
    if conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Fornecedores WHERE cnpj = %s", (cnpj,))
        conn.commit()  # Confirma a operação no banco de dados
        conn.close()
        messagebox.showinfo("Sucesso", "Fornecedor removido com sucesso.")

        # Opcional: tratar o caso onde nenhum registro foi deletado
        if cursor.rowcount == 0:
            messagebox.showinfo("Aviso", "Nenhum fornecedor encontrado com este CNPJ.")

def remover_mercado(cnpj):
    conn = conectar_banco()
    if conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Mercado WHERE cnpj = %s", (cnpj,))
        conn.commit()  # Confirma a operação no banco de dados
        conn.close()
        messagebox.showinfo("Sucesso", "Mercado removido com sucesso.")

        # Opcional: tratar o caso onde nenhum registro foi deletado
        if cursor.rowcount == 0:
            messagebox.showinfo("Aviso", "Nenhum mercado encontrado com este CNPJ.")

def remover_pedido(id_pedido):
    conn = conectar_banco()
    if conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Pedido WHERE id_pedido = %s", (id_pedido,))
        conn.commit()  # Confirma a operação no banco de dados
        conn.close()
        messagebox.showinfo("Sucesso", "Pedido removido com sucesso.")

        # Opcional: tratar o caso onde nenhum registro foi deletado
        if cursor.rowcount == 0:
            messagebox.showinfo("Aviso", "Nenhum pedido encontrado com este ID.")

def remover_cliente(cpf):
    conn = conectar_banco()
    if conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Tabela_de_clientes WHERE cpf = %s", (cpf,))
        conn.commit()  # Confirma a operação no banco de dados
        conn.close()
        messagebox.showinfo("Sucesso", "Cliente removido com sucesso.")

        # Opcional: tratar o caso onde nenhum registro foi deletado
        if cursor.rowcount == 0:
            messagebox.showinfo("Aviso", "Nenhum cliente encontrado com este CPF.")

def remover_funcionario(cpf):
    conn = conectar_banco()
    if conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Controle_do_Quadro_de_Funcionários WHERE cpf = %s", (cpf,))
        conn.commit()  # Confirma a operação no banco de dados
        conn.close()
        messagebox.showinfo("Sucesso", "Funcionário removido com sucesso.")

        # Opcional: tratar o caso onde nenhum registro foi deletado
        if cursor.rowcount == 0:
            messagebox.showinfo("Aviso", "Nenhum funcionário encontrado com este CPF.")


def remover_produto(id_produto):
    conn = conectar_banco()
    if conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM produtos WHERE id_Produto = %s", (id_produto,))
        conn.commit()  # Confirma a operação no banco de dados
        conn.close()
        messagebox.showinfo("Sucesso", "Produto removido com sucesso.")

        # Opcional: tratar o caso onde nenhum registro foi deletado
        if cursor.rowcount == 0:
            messagebox.showinfo("Aviso", "Nenhum produto encontrado com este ID.")

def remover_lote_estoque(id_lote):
    conn = conectar_banco()
    if conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Controle_de_Estoque WHERE id_lote = %s", (id_lote,))
        conn.commit()  # Confirma a operação no banco de dados
        conn.close()
        messagebox.showinfo("Sucesso", "Lote de estoque removido com sucesso.")

        # Opcional: tratar o caso onde nenhum registro foi deletado
        if cursor.rowcount == 0:
            messagebox.showinfo("Aviso", "Nenhum lote de estoque encontrado com este ID.")





# def remover_produto():
#     print("Remover produto")
#     conn = conectar_banco()
#     if conn:
#         id_produto = input("Digite o id_produto do produto a ser removido:")
#         cursor = conn.cursor()
#         try:
#             cursor.execute("DELETE FROM produtos WHERE id_produto = %s", (id_produto,))
#             conn.commit()
#             print("Produto removido com sucesso!")
#         except psycopg2.Error as e:
#             print("Erro ao remover produto:", e)
#         finally:
#             conn.close()

# def remover_cliente():
#     print("Remover cliente")
#     conn = conectar_banco()
#     if conn:
#         cpf = input("Digite o cpf do cliente a ser removido:")
#         cursor = conn.cursor()
#         try:
#             cursor.execute("DELETE FROM tabela_de_clientes WHERE cpf = %s", (cpf,))
#             conn.commit()
#             print("Cliente removido com sucesso!")
#         except psycopg2.Error as e:
#             print("Erro ao remover cliente:", e)
#         finally:
#             conn.close()

# def remover_lote():
#     print("Remover lote")
#     conn = conectar_banco()
#     if conn:
#         id_lote = input("Digite o id_lote do lote a ser removido:")
#         cursor = conn.cursor()
#         try:
#             cursor.execute("DELETE FROM controle_de_estoque WHERE id_lote = %s", (id_lote,))
#             conn.commit()
#             print("Lote removido com sucesso!")
#         except psycopg2.Error as e:
#             print("Erro ao remover lote:", e)
#         finally:
#             conn.close()

# def remover_endereco():
#     print("Remover endereço")
#     conn = conectar_banco()
#     if conn:
#         id_endereco = input("Digite o id_endereco do endereco a ser removido:")
#         cursor = conn.cursor()
#         try:
#             cursor.execute("DELETE FROM enderecos WHERE id_endereco = %s", (id_endereco,))
#             conn.commit()
#             print("Endereço removido com sucesso!")
#         except psycopg2.Error as e:
#             print("Erro ao remover endereço:", e)
#         finally:
#             conn.close()

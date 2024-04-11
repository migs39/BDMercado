import psycopg2

def conectar_banco():
    # Conectar ao banco de dados
    try:
        conn = psycopg2.connect(
            dbname="nome_do_banco", 
            user="nome_do_usuario", 
            password="senha_do_usuario", 
            host="localhost",  # ou o endereço IP do seu servidor PostgreSQL
            port="5432"        # porta padrão do PostgreSQL
        )
        print("Conexão bem-sucedida!")
        return conn
    except psycopg2.Error as e:
        print("Erro ao conectar ao banco de dados:", e)
        return None

# Funções para cadastrar
def cadastrar_fornecedor():
    print("Cadastrar fornecedor")
    conn = conectar_banco()
    if conn:
        cursor = conn.cursor()

        # Solicitar os valores ao usuário
        cnpj = input("Digite o CNPJ do fornecedor: ")
        nome_fornecedor = input("Digite o nome do fornecedor: ")
        telefone = input("Digite o telefone do fornecedor: ")
        email = input("Digite o email do fornecedor: ")

        # Inserir os valores na tabela de fornecedores
        cursor.execute("INSERT INTO fornecedores (cnpj, nome_fornecedor, telefone, email) VALUES (%s, %s, %s, %s)", (cnpj, nome_fornecedor, telefone, email))

        conn.commit()
        conn.close()

def cadastrar_mercado():
    print("Cadastrar mercado")
    conn = conectar_banco()
    if conn:
        cursor = conn.cursor()

        # Solicitar os valores ao usuário
        cnpj = input("Digite o CNPJ do mercado: ")
        nome_estabelecimento = input("Digite o nome do estabelecimento: ")
        telefone = input("Digite o telefone do mercado: ")

        # Inserir os valores na tabela de mercado
        cursor.execute("INSERT INTO mercado (cnpj, nome_estabelecimento, telefone) VALUES (%s, %s, %s)", (cnpj, nome_estabelecimento, telefone))

        conn.commit()
        conn.close()
        
def cadastrar_pedido():
    print("Cadastrar pedido")
    conn = conectar_banco()
    if conn:
        cursor = conn.cursor()

        # Solicitar os valores ao usuário
        id_pedido = input("Digite o ID do pedido: ")
        id_produto = input("Digite o ID do produto: ")
        cnpj_mercado = input("Digite o CNPJ do mercado: ")
        cpf_cliente = input("Digite o CPF do cliente: ")
        quantidade_produto = input("Digite a quantidade do produto: ")
        subtotal = input("Digite o subtotal: ")

        # Inserir os valores na tabela de pedido
        cursor.execute("INSERT INTO pedido (id_pedido, id_produto, cnpj_mercado, cpf_cliente, quantidade_produto, subtotal) VALUES (%s, %s, %s, %s, %s, %s)", (id_pedido, id_produto, cnpj_mercado, cpf_cliente, quantidade_produto, subtotal))

        conn.commit()
        conn.close()
        
def cadastrar_nota():
    print("Cadastrar nota")
    conn = conectar_banco()
    if conn:
        cursor = conn.cursor()

        # Solicitar os valores ao usuário
        id_pedido = input("Digite o ID do pedido: ")
        cpf_cliente = input("Digite o CPF do cliente: ")
        data_pedido = input("Digite a data do pedido: ")
        id_endereco = input("Digite o ID do endereço: ")
        preco_total = input("Digite o preço total: ")
        forma_pagamento = input("Digite a forma de pagamento: ")
        status_pedido = input("Digite o status do pedido: ")

        # Inserir os valores na tabela de nota
        cursor.execute("INSERT INTO nota (id_pedido, cpf_cliente, data_pedido, id_endereco, preco_total, forma_pagamento, status_pedido) VALUES (%s, %s, %s, %s, %s, %s, %s)", (id_pedido, cpf_cliente, data_pedido, id_endereco, preco_total, forma_pagamento, status_pedido))

        conn.commit()
        conn.close()
        
def cadastrar_endereco():
    print("Cadastrar endereço")
    conn = conectar_banco()
    if conn:
        cursor = conn.cursor()

        # Solicitar os valores ao usuário
        id_endereco = input("Digite o ID do endereço: ")
        cnpj_cpf_residente = input("Digite o CNPJ ou CPF do residente: ")
        cep = input("Digite o CEP: ")
        logradouro = input("Digite o logradouro: ")
        numero = input("Digite o número: ")
        complemento = input("Digite o complemento (opcional): ")

        # Inserir os valores na tabela de endereço
        cursor.execute("INSERT INTO enderecos (id_endereco, cnpj_cpf_residente, cep, logradouro, numero, complemento) VALUES (%s, %s, %s, %s, %s, %s)", (id_endereco, cnpj_cpf_residente, cep, logradouro, numero, complemento))

        conn.commit()
        conn.close()
        
def cadastrar_produto():
    print("Cadastrar produto")
    conn = conectar_banco()
    if conn:
        cursor = conn.cursor()

        # Solicitar os valores ao usuário
        id_produto = input("Digite o ID do produto: ")
        cnpj_fornecedor = input("Digite o CNPJ do fornecedor: ")
        descricao = input("Digite a descrição do produto: ")
        categoria = input("Digite a categoria do produto: ")
        preco = input("Digite o preço do produto: ")

        # Inserir os valores na tabela de produto
        cursor.execute("INSERT INTO produtos (id_produto, cnpj_fornecedor, descricao, categoria, preco) VALUES (%s, %s, %s, %s, %s)", (id_produto, cnpj_fornecedor, descricao, categoria, preco))

        conn.commit()
        conn.close()
        
def cadastrar_cliente():
    print("Cadastrar cliente")
    conn = conectar_banco()
    if conn:
        cursor = conn.cursor()

        # Solicitar os valores ao usuário
        cpf = input("Digite o CPF do cliente: ")
        nome_cliente = input("Digite o nome do cliente: ")
        telefone = input("Digite o telefone do cliente: ")
        email = input("Digite o email do cliente: ")
        data_cadastro = input("Digite a data de cadastro do cliente: ")

        # Inserir os valores na tabela de cliente
        cursor.execute("INSERT INTO tabela_de_clientes (cpf, nome_cliente, telefone, email, data_cadastro) VALUES (%s, %s, %s, %s, %s)", (cpf, nome_cliente, telefone, email, data_cadastro))

        conn.commit()
        conn.close()
        
def cadastrar_lote():
    print("Cadastrar lote")
    conn = conectar_banco()
    if conn:
        cursor = conn.cursor()

        # Solicitar os valores ao usuário
        id_lote = input("Digite o ID do lote: ")
        cnpj_unidade = input("Digite o CNPJ da unidade: ")
        id_produto = input("Digite o ID do produto: ")
        quantidade_estoque = input("Digite a quantidade em estoque: ")
        data_validade = input("Digite a data de validade: ")
        data_atualizacao = input("Digite a data de atualização: ")

        # Inserir os valores na tabela de lote
        cursor.execute("INSERT INTO controle_de_estoque (id_lote, cnpj_unidade, id_produto, quantidade_estoque, data_validade, data_atualizacao) VALUES (%s, %s, %s, %s, %s, %s)", (id_lote, cnpj_unidade, id_produto, quantidade_estoque, data_validade, data_atualizacao))

        conn.commit()
        conn.close()
        
        
# Funções para conferir
def conferir_fornecedor():
    print("Conferir fornecedor")
    conn = conectar_banco()
    if conn:
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM fornecedores")
        fornecedores = cursor.fetchall()
        for fornecedor in fornecedores:
            print("CNPJ:", fornecedor[0])
            print("Nome do Fornecedor:", fornecedor[1])
            print("Telefone:", fornecedor[2])
            print("Email:", fornecedor[3])

        conn.close()

def conferir_mercado():
    print("Conferir mercado")
    conn = conectar_banco()
    if conn:
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM mercado")
        mercados = cursor.fetchall()
        for mercado in mercados:
            print("CNPJ:", mercado[0])
            print("Nome do Estabelecimento:", mercado[1])
            print("Telefone:", mercado[2])

        conn.close()

def conferir_pedido():
    print("Conferir pedido")
    conn = conectar_banco()
    if conn:
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM pedido")
        pedidos = cursor.fetchall()
        for pedido in pedidos:
            print("ID do Pedido:", pedido[0])
            print("ID do Produto:", pedido[1])
            print("CNPJ do Mercado:", pedido[2])
            print("CPF do Cliente:", pedido[3])
            print("Quantidade do Produto:", pedido[4])
            print("Subtotal:", pedido[5])

        conn.close()

def conferir_nota():
    print("Conferir nota")
    conn = conectar_banco()
    if conn:
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM nota")
        notas = cursor.fetchall()
        for nota in notas:
            print("ID do Pedido:", nota[0])
            print("CPF do Cliente:", nota[1])
            print("Data do Pedido:", nota[2])
            print("ID do Endereço:", nota[3])
            print("Preço Total:", nota[4])
            print("Forma de Pagamento:", nota[5])
            print("Status do Pedido:", nota[6])

        conn.close()

def conferir_endereco():
    print("Conferir endereço")
    conn = conectar_banco()
    if conn:
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM enderecos")
        enderecos = cursor.fetchall()
        for endereco in enderecos:
            print("ID do Endereço:", endereco[0])
            print("CPF/CNPJ do Residente:", endereco[1])
            print("CEP:", endereco[2])
            print("Logradouro:", endereco[3])
            print("Número:", endereco[4])
            print("Complemento:", endereco[5])

        conn.close()

def conferir_produto():
    print("Conferir produto")
    conn = conectar_banco()
    if conn:
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM produtos")
        produtos = cursor.fetchall()
        for produto in produtos:
            print("ID do Produto:", produto[0])
            print("CNPJ do Fornecedor:", produto[1])
            print("Descrição:", produto[2])
            print("Categoria:", produto[3])
            print("Preço:", produto[4])

        conn.close()

def conferir_cliente():
    print("Conferir cliente")
    conn = conectar_banco()
    if conn:
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM tabela_de_clientes")
        clientes = cursor.fetchall()
        for cliente in clientes:
            print("CPF:", cliente[0])
            print("Nome do Cliente:", cliente[1])
            print("Telefone:", cliente[2])
            print("Email:", cliente[3])
            print("Data de Cadastro:", cliente[4])

        conn.close()

def conferir_lote():
    print("Conferir lote")
    conn = conectar_banco()
    if conn:
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM controle_de_estoque")
        lotes = cursor.fetchall()
        for lote in lotes:
            print("ID do Lote:", lote[0])
            print("CNPJ da Unidade:", lote[1])
            print("ID do Produto:", lote[2])
            print("Quantidade em Estoque:", lote[3])
            print("Data de Validade:", lote[4])
            print("Data de Atualização:", lote[5])

        conn.close()

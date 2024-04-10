import funcs
import tkinter as tk

def open_adicionar_dados():
    root.withdraw()  # Oculta a janela atual
    adicionar_dados_window.deiconify()  # Exibe a nova janela

def close_adicionar_dados():
    adicionar_dados_window.withdraw()  # Oculta a janela de adicionar dados
    root.deiconify()  # Exibe a janela principal novamente

def open_conferir_dados():
    root.withdraw()  # Oculta a janela atual
    conferir_dados_window.deiconify()  # Exibe a nova janela

def close_conferir_dados():
    conferir_dados_window.withdraw()  # Oculta a janela de conferir dados
    root.deiconify()  # Exibe a janela principal novamente


# Janela principal
root = tk.Tk()
root.title("Banco de Dados Supermercados")
root.configure(background='white')

# Título
titulo = tk.Label(root, text="Banco de Dados Supermercados", font=("Helvetica", 20), bg="white")
titulo.pack(pady=10)

# Botões
btn_adicionar_dados = tk.Button(root, text="Adicionar Dados", command=open_adicionar_dados)
btn_adicionar_dados.pack(pady=5)

btn_conferir_dados = tk.Button(root, text="Conferir Dados", command=open_conferir_dados)
btn_conferir_dados.pack(pady=5)

# Janela para adicionar dados
adicionar_dados_window = tk.Toplevel(root)
adicionar_dados_window.title("Adicionar Dados")
adicionar_dados_window.configure(background='white')
adicionar_dados_window.withdraw()  # Mantém a janela oculta inicialmente

# Botão Voltar
btn_voltar_adicionar = tk.Button(adicionar_dados_window, text="Voltar", command=close_adicionar_dados)
btn_voltar_adicionar.grid(row=0, column=0, sticky="nw", padx=10, pady=10)

# Botões para cadastrar
btn_cadastrar_fornecedor = tk.Button(adicionar_dados_window, text="Cadastrar Fornecedor", command=funcs.cadastrar_fornecedor)
btn_cadastrar_fornecedor.grid(row=1, column=0, pady=5)

btn_cadastrar_mercado = tk.Button(adicionar_dados_window, text="Cadastrar Mercado", command=funcs.cadastrar_mercado)
btn_cadastrar_mercado.grid(row=2, column=0, pady=5)

btn_cadastrar_pedido = tk.Button(adicionar_dados_window, text="Cadastrar Pedido", command=funcs.cadastrar_pedido)
btn_cadastrar_pedido.grid(row=3, column=0, pady=5)

btn_cadastrar_produto = tk.Button(adicionar_dados_window, text="Cadastrar Produto", command=funcs.cadastrar_produto)
btn_cadastrar_produto.grid(row=6, column=0, pady=5)

btn_cadastrar_cliente = tk.Button(adicionar_dados_window, text="Cadastrar Cliente", command=funcs.cadastrar_cliente)
btn_cadastrar_cliente.grid(row=7, column=0, pady=5)

btn_cadastrar_lote = tk.Button(adicionar_dados_window, text="Cadastrar Lote", command=funcs.cadastrar_lote)
btn_cadastrar_lote.grid(row=8, column=0, pady=5)

# Janela para conferir dados
conferir_dados_window = tk.Toplevel(root)
conferir_dados_window.title("Conferir Dados")
conferir_dados_window.configure(background='white')
conferir_dados_window.withdraw()  # Mantém a janela oculta inicialmente

# Botão Voltar
btn_voltar_conferir = tk.Button(conferir_dados_window, text="Voltar", command=close_conferir_dados)
btn_voltar_conferir.grid(row=0, column=0, sticky="nw", padx=10, pady=10)

# Botões para conferir
btn_conferir_fornecedor = tk.Button(conferir_dados_window, text="Conferir Fornecedor", command=funcs.conferir_fornecedor)
btn_conferir_fornecedor.grid(row=1, column=0, pady=5)

btn_conferir_mercado = tk.Button(conferir_dados_window, text="Conferir Mercado", command=funcs.conferir_mercado)
btn_conferir_mercado.grid(row=2, column=0, pady=5)

btn_conferir_pedido = tk.Button(conferir_dados_window, text="Conferir Pedido", command=funcs.conferir_pedido)
btn_conferir_pedido.grid(row=3, column=0, pady=5)

btn_conferir_produto = tk.Button(conferir_dados_window, text="Conferir Produto", command=funcs.conferir_produto)
btn_conferir_produto.grid(row=6, column=0, pady=5)

btn_conferir_cliente = tk.Button(conferir_dados_window, text="Conferir Cliente", command=funcs.conferir_cliente)
btn_conferir_cliente.grid(row=7, column=0, pady=5)

btn_conferir_lote = tk.Button(conferir_dados_window, text="Conferir Lote", command=funcs.conferir_lote)
btn_conferir_lote.grid(row=8, column=0, pady=5)

root.mainloop()

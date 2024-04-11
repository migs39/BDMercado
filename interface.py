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

# Função para aumentar o tamanho da fonte
def aumentar_fonte(fonte, tamanho):
    return (fonte, int(tamanho * 1.2))

# Janela principal
root = tk.Tk()
root.title("Banco de Dados Supermercados")
root.configure(background='white')
root.geometry("800x640")  # Define o tamanho da janela principal

# Nomes dos responsáveis
responsaveis = ["Gabriel Pereira", "Gabriel Vilas", "Henrique Corazza", "Lucas Papoti", "Miguel Schwengber"]
for nome in responsaveis:
    tk.Label(root, text=nome, font=aumentar_fonte("Helvetica", 8), bg="white").pack(side = 'bottom', anchor ="sw", padx=10, pady=5)

# Título
titulo = tk.Label(root, text="Banco de Dados Supermercados", font=aumentar_fonte("Helvetica", 20), bg="white")
titulo.pack(pady=100)

# Botões
btn_adicionar_dados = tk.Button(root, text="Adicionar Dados", font=aumentar_fonte("Helvetica", 12), command=open_adicionar_dados)
btn_adicionar_dados.pack(pady=5)

btn_conferir_dados = tk.Button(root, text="Conferir Dados", font=aumentar_fonte("Helvetica", 12), command=open_conferir_dados)
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
btn_cadastrar_fornecedor = tk.Button(adicionar_dados_window, text="Cadastrar Fornecedor", font=aumentar_fonte("Helvetica", 12), command=funcs.cadastrar_fornecedor)
btn_cadastrar_fornecedor.pack(pady=10)

btn_cadastrar_mercado = tk.Button(adicionar_dados_window, text="Cadastrar Mercado", font=aumentar_fonte("Helvetica", 12), command=funcs.cadastrar_mercado)
btn_cadastrar_mercado.pack(pady=10)

btn_cadastrar_pedido = tk.Button(adicionar_dados_window, text="Cadastrar Pedido", font=aumentar_fonte("Helvetica", 12), command=funcs.cadastrar_pedido)
btn_cadastrar_pedido.pack(pady=10)

btn_cadastrar_produto = tk.Button(adicionar_dados_window, text="Cadastrar Produto", font=aumentar_fonte("Helvetica", 12), command=funcs.cadastrar_produto)
btn_cadastrar_produto.pack(pady=10)

btn_cadastrar_cliente = tk.Button(adicionar_dados_window, text="Cadastrar Cliente", font=aumentar_fonte("Helvetica", 12), command=funcs.cadastrar_cliente)
btn_cadastrar_cliente.pack(pady=10)

btn_cadastrar_lote = tk.Button(adicionar_dados_window, text="Cadastrar Lote", font=aumentar_fonte("Helvetica", 12), command=funcs.cadastrar_lote)
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
btn_conferir_fornecedor = tk.Button(conferir_dados_window, text="Conferir Fornecedor", font=aumentar_fonte("Helvetica", 12), command=funcs.conferir_fornecedor)
btn_conferir_fornecedor.pack(pady=10)

btn_conferir_mercado = tk.Button(conferir_dados_window, text="Conferir Mercado", font=aumentar_fonte("Helvetica", 12), command=funcs.conferir_mercado)
btn_conferir_mercado.pack(pady=10)

btn_conferir_pedido = tk.Button(conferir_dados_window, text="Conferir Pedido", font=aumentar_fonte("Helvetica", 12), command=funcs.conferir_pedido)
btn_conferir_pedido.pack(pady=10)

btn_conferir_produto = tk.Button(conferir_dados_window, text="Conferir Produto", font=aumentar_fonte("Helvetica", 12), command=funcs.conferir_produto)
btn_conferir_produto.pack(pady=10)

btn_conferir_cliente = tk.Button(conferir_dados_window, text="Conferir Cliente", font=aumentar_fonte("Helvetica", 12), command=funcs.conferir_cliente)
btn_conferir_cliente.pack(pady=10)

btn_conferir_lote = tk.Button(conferir_dados_window, text="Conferir Lote", font=aumentar_fonte("Helvetica", 12), command=funcs.conferir_lote)
btn_conferir_lote.pack(pady=10)

root.mainloop()

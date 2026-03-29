import tkinter as tk
from tkinter import messagebox

# Dicionário com comandos e descrições
comandos = {
    "cd": "Muda o diretório atual.",
    "mkdir": "Cria um novo diretório.",
    "clear": "Limpa a tela do terminal.",
    "mv": "Move ou renomeia arquivos e diretórios.",
    "cp": "Copia arquivos e diretórios.",
    "nano": "Editor de texto simples no terminal.",
    "ping": "Verifica a conectividade com outro host.",
    "ip": "Mostra/gerencia configurações de rede.",
    "find": "Busca arquivos e diretórios no sistema.",
    "cat": "Exibe o conteúdo de arquivos.",
    "chmod": "Altera permissões de arquivos e diretórios."
}

# Função para mostrar descrição
def mostrar_descricao(comando):
    descricao = comandos[comando]
    #O primeiro "comando" significa o nome cv,cp,nano e etc, já a descrição
    # é o endereço do dicionário que é associado ao comando 
    messagebox.showinfo(f"Comando: {comando}", descricao)

# Criar janela principal
janela = tk.Tk()
janela.title("Comandos Linux")
janela.config(bg="lightblue")
janela.geometry("400x400")

#Tag de título da página
titulo = tk.Label(
    janela,
    text="Comandos Linux",
    font=("Arial",18,"bold"),
    bg="lightblue",
    fg="black"
)
titulo.pack(pady=10)

# Loop para criar botões 
for comando in comandos:
    botao = tk.Button(
        janela,
        text=comando, #Vai pegar cada comando do dicionário e transformar em um botão
        width=25,
        height=3,
        command=lambda c=comando: mostrar_descricao(c) #função que quando o botão é clicado aparece a descrição
        #do comando
    )
    botao.pack(pady=5)#cria o botão 


# Rodar aplicação
janela.mainloop()
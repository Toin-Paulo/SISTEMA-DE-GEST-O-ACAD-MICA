import tkinter as tk
from tkinter import messagebox
import json
import os

# Nome do arquivo JSON
ARQUIVO_JSON = "alunos.json"

# Função para carregar os dados do JSON
def carregar_dados():
    if not os.path.exists(ARQUIVO_JSON):
        with open(ARQUIVO_JSON, "w") as f:
            json.dump([], f)
    
    with open(ARQUIVO_JSON, "r") as f:
        return json.load(f)

# Função para salvar os dados no JSON
def salvar_dados(dados):
    with open(ARQUIVO_JSON, "w") as f:
        json.dump(dados, f, indent=4)

# Função para adicionar matérias a um aluno existente
def abrir_tela_adicionar_materia():
    adicionar_janela = tk.Toplevel(root)
    adicionar_janela.title("Adicionar Matéria e Notas")
    adicionar_janela.geometry("600x400")
    adicionar_janela.configure(bg="#2C5545")

    # Campo para matrícula do aluno
    tk.Label(adicionar_janela, text="Matrícula do Aluno:", bg="#2C5545", fg="white").pack(pady=5)
    entry_matricula = tk.Entry(adicionar_janela)
    entry_matricula.pack(pady=5)

    # Campos para matéria e notas
    tk.Label(adicionar_janela, text="Nome da Matéria:", bg="#2C5545", fg="white").pack(pady=5)
    entry_materia = tk.Entry(adicionar_janela)
    entry_materia.pack(pady=5)

    tk.Label(adicionar_janela, text="Nota 1:", bg="#2C5545", fg="white").pack(pady=5)
    entry_nota1 = tk.Entry(adicionar_janela)
    entry_nota1.pack(pady=5)

    tk.Label(adicionar_janela, text="Nota 2:", bg="#2C5545", fg="white").pack(pady=5)
    entry_nota2 = tk.Entry(adicionar_janela)
    entry_nota2.pack(pady=5)

    # Função para adicionar matéria ao aluno
    def adicionar_materia():
        matricula = entry_matricula.get()
        materia_nome = entry_materia.get()
        nota1 = entry_nota1.get()
        nota2 = entry_nota2.get()

        if not (matricula and materia_nome and nota1 and nota2):
            messagebox.showwarning("Erro", "Preencha todos os campos!")
            return

        try:
            nota1 = float(nota1)
            nota2 = float(nota2)
        except ValueError:
            messagebox.showwarning("Erro", "Notas devem ser valores numéricos!")
            return

        dados = carregar_dados()
        aluno_encontrado = False

        for aluno in dados:
            if aluno["matricula"] == matricula:
                aluno_encontrado = True
                # Verifica se a matéria já existe
                for materia in aluno["materias"]:
                    if materia["nome"].lower() == materia_nome.lower():
                        messagebox.showwarning("Erro", "Essa matéria já foi adicionada para o aluno!")
                        return

                # Adiciona a nova matéria
                aluno["materias"].append({"nome": materia_nome, "nota1": nota1, "nota2": nota2})
                salvar_dados(dados)
                messagebox.showinfo("Sucesso", f"Matéria {materia_nome} adicionada ao aluno {aluno['nome']}!")
                entry_materia.delete(0, tk.END)
                entry_nota1.delete(0, tk.END)
                entry_nota2.delete(0, tk.END)
                return

        if not aluno_encontrado:
            messagebox.showwarning("Erro", "Matrícula não encontrada!")

    tk.Button(adicionar_janela, text="Adicionar Matéria", command=adicionar_materia, bg="green", fg="white").pack(pady=10)

# Criando a janela principal
root = tk.Tk()
root.geometry("400x300")
root.title("Sistema de Alunos")

# Botão para abrir a tela de adicionar matéria
btn_adicionar_materia = tk.Button(root, text="Adicionar Matéria a Aluno", command=abrir_tela_adicionar_materia, bg="blue", fg="white")
btn_adicionar_materia.pack(pady=20)

root.mainloop()

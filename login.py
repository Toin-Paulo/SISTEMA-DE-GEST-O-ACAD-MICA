import tkinter as tk
from tkinter import Entry, Label, Button, Entry, messagebox, Frame
import modulo_aluno

usuarios = modulo_aluno.carregar_dados()

def sair():
    root.destroy()

# FAZER LOGIN
def login():
    user = entry_user.get()
    password = int(entry_pass.get())
    aluno_login = modulo_aluno.pesqusar_aluno(user,password)

    #JANELA APOS LOGIN
    def janela_pos_login():

        def sair_janela():
            janela.destroy()

        # Criando a janela principal
        janela = tk.Toplevel()
        janela.title("SGA - Painel Principal")
        janela.geometry("800x500")
        janela.configure(bg="#f5f5f5")

        aluno = modulo_aluno.obter_alunos(user,password)
        if not aluno:
            messagebox.showwarning("Erro", "Usuário não encontrado!")
            return

        menu_frame = Frame(janela, bg="#1e3d3a", width=200, height=500)
        menu_frame.pack(side="left", fill="y")
        
        Label(menu_frame, text=aluno["nome"], fg="white", bg="#1e3d3a", font=("Arial", 12, "bold")).pack(pady=20)
        Button(menu_frame, text="Sair", bg="#ff4d4d", fg="white", command=sair_janela).pack(pady=20)
        
        main_frame = Frame(janela, bg="white", width=600, height=500)
        main_frame.pack(side="right", fill="both", expand=True)
        
        Label(main_frame, text="Ensino", font=("Arial", 12, "bold"), bg="white").pack(pady=10)
        Button(main_frame, text="Meus Dados", width=20).pack(pady=2)
        
        if "materias" in aluno and aluno["materias"]:
            Label(main_frame, text="Suas Matérias", font=("Arial", 12, "bold"), bg="white").pack(pady=10)
            for materia in aluno["materias"]:
                Label(main_frame, text=f"{materia['nome']} - Média: {materia['media']}", bg="white").pack()
        else:
            Label(main_frame, text="Aluno sem matérias cadastradas",font=("Arial", 12, "bold"), bg="white").pack(pady=10)

        janela.mainloop()
    
    if aluno_login == True:
        messagebox.showinfo(janela_pos_login())
    else:
        messagebox.showwarning("Login", "Usuário ou senha incorretos!")

# Lista para armazenar as matérias e notas
materias = []

# Função para adicionar matéria
def abrir_tela_adicionar_materia():
    materia_janela = tk.Toplevel()  # Criar uma janela secundária corretamente
    materia_janela.title("Registrar Matéria")
    materia_janela.geometry("600x500")
    materia_janela.configure(bg="#2C5545")

    # Labels e Campos de entrada
    tk.Label(materia_janela, text="Matrícula do Aluno:", bg="#2C5545", fg="white").pack(pady=5)
    entry_matricula = tk.Entry(materia_janela)
    entry_matricula.pack(pady=5)

    tk.Label(materia_janela, text="Adicionar Matéria:", bg="#2C5545", fg="white").pack(pady=5)
    entry_materia = tk.Entry(materia_janela)
    entry_materia.pack(pady=5)

    tk.Label(materia_janela, text="Nota 1:", bg="#2C5545", fg="white").pack(pady=5)
    entry_nota1 = tk.Entry(materia_janela)
    entry_nota1.pack(pady=5)

    tk.Label(materia_janela, text="Nota 2:", bg="#2C5545", fg="white").pack(pady=5)
    entry_nota2 = tk.Entry(materia_janela)
    entry_nota2.pack(pady=5)

    def adicionar_materia():
        matricula = entry_matricula.get()
        materia_nome = entry_materia.get()
        nota1 = entry_nota1.get()
        nota2 = entry_nota2.get()


        dados = modulo_aluno.carregar_dados()
        aluno_encontrado = False

        if not (matricula and materia_nome and nota1 and nota2):
            messagebox.showwarning("Erro", "Preencha todos os campos!")
            return

        try:
            nota1 = float(nota1)
            nota2 = float(nota2)
        except ValueError:
            messagebox.showwarning("Erro", "Notas devem ser valores numéricos!")
            return

        dados = modulo_aluno.carregar_dados()
        aluno_encontrado = False

        for aluno in dados:
            if aluno["id"] == matricula:
                aluno_encontrado = True
                # Verifica se a matéria já existe
                for materia in aluno["materias"]:
                    if materia["nome"].lower() == materia_nome.lower():
                        messagebox.showwarning("Erro", "Essa matéria já foi adicionada para o aluno!")
                        return

                # Adiciona a nova matéria
                aluno["materias"].append({"nome": materia_nome, "nota1": nota1, "nota2": nota2})
                modulo_aluno.salvar_dados(dados)
                messagebox.showinfo("Sucesso", f"Matéria {materia_nome} adicionada ao aluno {aluno['nome']}!")
                entry_materia.delete(0, tk.END)
                entry_nota1.delete(0, tk.END)
                entry_nota2.delete(0, tk.END)
                return

        if not aluno_encontrado:
            messagebox.showwarning("Erro", "Matrícula não encontrada!")

    tk.Button(materia_janela, text="Adicionar Matéria", command=adicionar_materia, bg="green", fg="white").pack(pady=10)

#REGISTRAR ALUNOS E MATERIAS
def abrir_tela_registro():
    registro_janela = tk.Toplevel()
    registro_janela.title("Registrar Aluno")
    registro_janela.geometry("600x500")
    registro_janela.configure(bg="#2C5545")

    # Campos de entrada
    tk.Label(registro_janela, text="Nome do Aluno:", bg="#2C5545", fg="white").pack(pady=5)
    entry_nome = tk.Entry(registro_janela)
    entry_nome.pack(pady=5)

    tk.Label(registro_janela, text="Matrícula:", bg="#2C5545", fg="white").pack(pady=5)
    entry_matricula = tk.Entry(registro_janela)
    entry_matricula.pack(pady=5)

    tk.Label(registro_janela, text="Senha:", bg="#2C5545", fg="white").pack(pady=5)
    entry_senha = tk.Entry(registro_janela, show="*")
    entry_senha.pack(pady=5)

    tk.Button(registro_janela, text="Adicionar Matéria", command=abrir_tela_adicionar_materia, bg="green", fg="white").pack(pady=5)

    # Função para registrar aluno
    def registrar():
        nome = entry_nome.get()
        matricula = entry_matricula.get()
        senha = int(entry_senha.get())

        if not (nome and matricula  and senha):
            messagebox.showwarning("Erro", "Preencha todos os campos!")
            return

        dados = usuarios

        # Verifica se a matrícula já existe
        for aluno in dados:
            if aluno["id"] == matricula:
                messagebox.showwarning("Erro", "Matrícula já cadastrada!")
                return None

        # Adiciona o aluno ao JSON
        novo_aluno = {
            "matricula": matricula,
            "nome": nome,
            "senha": senha,
            "materias": materias
        }

        dados.append(novo_aluno)
        modulo_aluno.salvar_dados(dados)
        messagebox.showinfo("Registro", "Aluno registrado com sucesso!")
        registro_janela.destroy()

    tk.Button(registro_janela, text="Registrar Aluno", command=registrar, bg="blue", fg="white").pack(pady=10)

# Criando a janela login
root = tk.Tk()
root.title("Login - SGA")
root.geometry("800x600")
root.configure(bg="#1e3d3a")

# Título
label_title = Label(root, text="Login", fg="white", bg="#1e3d3a", font=("Arial", 16, "bold")).pack(pady=10)

label_subtitle = Label(root, text="Acesse o Sistema de gestão Acadêmica:", fg="white", bg="#1e3d3a", font=("Arial", 12)).pack()

# Campo Usuário
label_user = Label(root, text="Usuário:", fg="white", bg="#1e3d3a", font=("Arial", 10)).pack(pady=(20,0))
entry_user = Entry(root, width=40, font=("Arial", 12))
entry_user.pack()

# Campo Senha
label_pass = Label(root, text="Senha:", fg="white", bg="#1e3d3a", font=("Arial", 10)).pack(pady=(10,0))
entry_pass = Entry(root, width=40, font=("Arial", 12), show="*")
entry_pass.pack()

# Botão de Login
btn_login = Button(root, text="Acessar", font=("Arial", 12), bg="#00ff99", fg="black", width=20, command=login).pack(pady=20)

# Botão registrar
btn_registrar = tk.Button(root, text="Registrar", command=abrir_tela_registro, bg="#007A5E", fg="white").pack(pady=20)

# Botão de Sair
btn_sair = Button(root, text="Sair", bg="#ff4d4d", fg="white", command=sair).pack(pady=20)

root.mainloop()

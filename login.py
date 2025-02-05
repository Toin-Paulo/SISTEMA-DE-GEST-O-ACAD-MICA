import tkinter as tk
from tkinter import Entry, Label, Button, Entry, messagebox, Frame, Listbox
import modulo_aluno as md

usuarios = md.carregar_dados()
aluno = md.listar_alunos()

def abrir_chamado():
    print("Abrindo chamado...")

def trocar_tela(frame):
    frame.tkraise()

def janela_principal():
    
    # Criando a janela principal
    root = tk.Tk()
    root.title("SGA - Painel Principal")
    root.geometry("800x500")
    root.configure(bg="#f5f5f5")

    # Criando o menu lateral
    menu_frame = Frame(root, bg="#1e3d3a", width=200, height=500)
    menu_frame.pack(side="left", fill="y")

    # Nome do usuário
    label_user = Label(menu_frame, text=aluno["nome"], fg="white", bg="#1e3d3a", font=("Arial", 12, "bold"))
    label_user.pack(pady=20)

    # Lista de opções do menu
    #menu_options = ["Início", "Documentos/Processos", "Ensino", "Pesquisa", "Extensão", "Tec. da Informação",
    #                "Central de Serviços", "Atividades Estudantis", "Saúde", "Comunicação Social", "Des. Institucional"]
   # listbox_menu = Listbox(menu_frame, bg="#1e3d3a", fg="white", font=("Arial", 10), height=len(menu_options))
   # for option in menu_options:
   #     listbox_menu.insert("end", option)
   # listbox_menu.pack(pady=10)

    # Botão de Sair
    btn_sair = Button(menu_frame, text="Sair", bg="#ff4d4d", fg="white", command=sair)
    btn_sair.pack(pady=20)

    # Painel principal
    main_frame = Frame(root, bg="white", width=600, height=500)
    main_frame.pack(side="right", fill="both", expand=True)

    # Seção Ensino
    label_ensino = Label(main_frame, text="Ensino", font=("Arial", 12, "bold"), bg="white")
    label_ensino.pack(pady=10)

    btn_meus_dados = Button(main_frame, text="Meus Dados", width=20)
    btn_meus_dados.pack(pady=2)

    btn_horarios = Button(main_frame, text="Locais e Horários de Aula", width=20)
    btn_horarios.pack(pady=2)

    btn_requerimentos = Button(main_frame, text="Meus Requerimentos", width=20)
    btn_requerimentos.pack(pady=2)

    # Seção Central de Serviços
    label_servicos = Label(main_frame, text="Central de Serviços", font=("Arial", 12, "bold"), bg="white")
    label_servicos.pack(pady=10)

    btn_meus_chamados = Button(main_frame, text="Meus Chamados", width=20)
    btn_meus_chamados.pack(pady=2)

    btn_abrir_chamado = Button(main_frame, text="Abrir Chamado", width=20, bg="#008000", fg="white", command=abrir_chamado)
    btn_abrir_chamado.pack(pady=2)

    root.mainloop()

def sair():
    root.quit()

def login():
    user = int(entry_user.get())
    password = int(entry_pass.get())
    aluno_login = md.pesqusar_aluno(user,password)
    if aluno_login == True:
        messagebox.showinfo(janela_principal())
    else:
        messagebox.showwarning("Login", "Usuário ou senha incorretos!")

def abrir_tela_registro():
    registro_janela = tk.Toplevel(root)
    registro_janela.title("Registrar Usuário")
    registro_janela.geometry("600x400")
    registro_janela.configure(bg="#2C5545")
    
    tk.Label(registro_janela, text="Usuário:", bg="#2C5545", fg="white").pack(pady=5)
    entry_novo_usuario = tk.Entry(registro_janela)
    entry_novo_usuario.pack(pady=10)
    
    tk.Label(registro_janela, text="Senha:", bg="#2C5545", fg="white").pack(pady=5)
    entry_nova_senha = tk.Entry(registro_janela, show="*")
    entry_nova_senha.pack(pady=10)

    def registrar():
        usuario = entry_novo_usuario.get()
        senha = entry_nova_senha.get()
        
        if usuario in usuarios:
            messagebox.showwarning("Registro", "Usuário já existe!")
        else:
            usuarios[usuario] = senha
            messagebox.showinfo("Registro", "Usuário registrado com sucesso!")
            registro_janela.destroy()

    btn_confirmar = tk.Button(registro_janela, text="Registrar", command=registrar, bg="#007A5E", fg="white")
    btn_confirmar.pack(pady=10)

# Criando a janela login
root = tk.Tk()
root.title("Login - SGA")
root.geometry("800x600")
root.configure(bg="#1e3d3a")

# Título
label_title = Label(root, text="Login", fg="white", bg="#1e3d3a", font=("Arial", 16, "bold"))
label_title.pack(pady=10)

label_subtitle = Label(root, text="Acesse o Sistema de gestão Acadêmica:", fg="white", bg="#1e3d3a", font=("Arial", 12))
label_subtitle.pack()

# Campo Usuário
label_user = Label(root, text="Usuário:", fg="white", bg="#1e3d3a", font=("Arial", 10))
label_user.pack(pady=(20,0))
entry_user = Entry(root, width=40, font=("Arial", 12))
entry_user.pack()

# Campo Senha
label_pass = Label(root, text="Senha:", fg="white", bg="#1e3d3a", font=("Arial", 10))
label_pass.pack(pady=(10,0))
entry_pass = Entry(root, width=40, font=("Arial", 12), show="*")
entry_pass.pack()

# Botão de Login
btn_login = Button(root, text="Acessar", font=("Arial", 12), bg="#00ff99", fg="black", width=20, command=login)
btn_login.pack(pady=20)

# Botão registrar
btn_registrar = tk.Button(root, text="Registrar", command=abrir_tela_registro, bg="#007A5E", fg="white")
btn_registrar.pack(pady=20)

# Botão de Sair
btn_sair = Button(root, text="Sair", bg="#ff4d4d", fg="white", command=sair)
btn_sair.pack(pady=20)

# Link para recuperação de senha
label_forgot = Button(root, text="Esqueceu ou deseja alterar sua senha?", fg="white", bg="#1e3d3a", font=("Arial", 9))
label_forgot.pack()

root.mainloop()
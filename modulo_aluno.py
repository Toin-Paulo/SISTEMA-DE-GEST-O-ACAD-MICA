import json
import os

# Nome do arquivo JSON que armazenará os dados
FILE_NAME = "alunos.json"

# Carrega os dados do JSON, se o arquivo existir
def carregar_dados():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)
    return []

# Salva os dados no arquivo JSON
def salvar_dados(alunos):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(alunos, file, indent=4, ensure_ascii=False)

# Adiciona um novo aluno
def adicionar_aluno(nome, idade, curso):
    alunos = carregar_dados()
    novo_id = len(alunos) + 1
    alunos.append({"id": novo_id, "nome": nome, "idade": idade, "curso": curso})
    salvar_dados(alunos)
    print(f"Aluno {nome} cadastrado com sucesso!")


# Lista todos os alunos
def listar_alunos():
    alunos = carregar_dados()
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return None
    else:
        for aluno in alunos:
            return aluno
        
def pesqusar_aluno(id,senha):
    alunos = carregar_dados()
    for aluno in alunos:
        if id == aluno["matricula"] and senha == aluno["senha"]:
            return True
        
        
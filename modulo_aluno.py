import json

# Nome do arquivo JSON que armazenará os dados
Arquivo = "alunos.json"

# Carrega os dados do JSON, se o arquivo existir
def carregar_dados():
    with open(Arquivo, "r", encoding="utf-8") as file:
        return json.load(file)

# Salva os dados no arquivo JSON
def salvar_dados(alunos):
    with open(Arquivo, "w", encoding="utf-8") as file:
        json.dump(alunos, file, indent=4, ensure_ascii=False)

# Lista todos os alunos
def listar_alunos(id,senha):
    alunos = carregar_dados()
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return
    for aluno in alunos:
       if id == aluno["id"] and senha == aluno["senha"]:
           return aluno["nome"]

def pesqusar_aluno(id,senha):
    alunos = carregar_dados()
    for aluno in alunos:
        if id == aluno["id"] and senha == aluno["senha"]:
            return Trueluno
        
def pesqusar_aluno(id,senha):
    alunos = carregar_dados()
    for aluno in alunos:
        if id == aluno["matricula"] and senha == aluno["senha"]:
            return True
        
        

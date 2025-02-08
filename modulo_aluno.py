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


def media_aluno():
    alunos = carregar_dados()  # Função para carregar os dados dos alunos
    for aluno in alunos:
        for materia in aluno["materias"]:
            media = (materia["nota1"] + materia["nota2"]) / 2  # Calculando a média
            materia["media"] = media  # Adicionando a média diretamente na matéria
        #aluno["materias_com_media"] = aluno["materias"]  # Adicionando a lista de matérias com as médias ao dicionário do aluno

    return alunos  # Retorna a lista de alunos com as médias incluídas

def salvar_dados(alunos):
    with open("alunos.json", "w", encoding="utf-8") as file:
        json.dump(alunos, file, indent=4, ensure_ascii=False)

# Carrega, calcula as médias e salva os dados
alunos_com_media = media_aluno()
salvar_dados(alunos_com_media)
        

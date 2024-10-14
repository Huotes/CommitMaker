import os
import random
import subprocess
from datetime import datetime

# Obter o diretório do script atual
REPO_PATH = os.path.dirname(os.path.abspath(__file__))

# Função para alterar o arquivo de commit
def modificar_arquivo():
    arquivo = os.path.join(REPO_PATH, "commit.txt")
    with open(arquivo, "a") as f:
        f.write(f"Commit aleatório em {datetime.now()}\n")

# Função para realizar o commit
def realizar_commit():
    os.chdir(REPO_PATH)
    
    # Adiciona os arquivos para commit
    subprocess.run(["git", "add", "."])
    
    # Gera uma mensagem de commit semântica aleatória
    mensagens = [
        "feat: adiciona nova funcionalidade para gerar commits automáticos",
        "fix: corrige script de automação de commits",
        "docs: atualiza documentação do projeto",
        "style: ajusta formatação do arquivo commit.txt",
        "refactor: melhora estrutura do script de automação",
        "test: adiciona testes automatizados para o CommitMaker",
        "chore: atualiza dependências e limpa código"
    ]
    mensagem = random.choice(mensagens)
    
    # Faz o commit
    subprocess.run(["git", "commit", "-m", mensagem])
    
    # Faz o push para o repositório remoto
    subprocess.run(["git", "push", "origin", "main"])

# Função para registrar no arquivo de log
def registrar_log(mensagem):
    log_file = os.path.join(REPO_PATH, "log.txt")
    with open(log_file, "a") as f:
        f.write(f"{datetime.now()}: {mensagem}\n")

# Função principal que chama todas as funções
def main():
    try:
        modificar_arquivo()
        realizar_commit()
        registrar_log("Commit realizado com sucesso")
        print(f"Commit realizado com sucesso em {datetime.now()}")
    except Exception as e:
        registrar_log(f"Erro ao realizar o commit: {e}")
        print(f"Erro ao realizar o commit: {e}")

if __name__ == "__main__":
    main()

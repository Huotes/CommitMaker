import os
import subprocess
import random
from .logger import registrar_log

REPO_PATH = os.path.dirname(os.path.abspath(__file__))

def realizar_commit():
    try:
        os.chdir(REPO_PATH)

        # Adiciona os arquivos ao índice
        subprocess.run(["git", "add", "."], check=True)

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

        # Realiza o commit
        subprocess.run(["git", "commit", "-m", mensagem], check=True)

        # Realiza o push
        subprocess.run(["git", "push", "origin", "main"], check=True)

        # Log de sucesso
        registrar_log(
            event="commit",
            status="success",
            details="Commit realizado com sucesso.",
            extra={"mensagem": mensagem}
        )
        print(f"🚀 Commit realizado com sucesso: {mensagem}")

    except subprocess.CalledProcessError as e:
        registrar_log(
            event="commit",
            status="error",
            details=f"Erro ao executar comando Git: {e}"
        )
        print(f"❌ Erro ao executar comando Git: {e}")
    except Exception as e:
        registrar_log(
            event="commit",
            status="error",
            details=f"Erro inesperado: {e}"
        )
        print(f"❌ Erro inesperado: {e}")

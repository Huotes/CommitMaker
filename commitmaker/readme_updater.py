import os
from .api_client import obter_frase_meme
from .logger import registrar_log

# Caminho da raiz do projeto
REPO_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def atualizar_readme():
    """
    Atualiza o arquivo README.md com uma frase de meme obtida via API.
    """
    try:
        # Define o caminho para o README.md na raiz do projeto
        readme_path = os.path.join(REPO_PATH, "README.md")
        print(f"📂 Caminho do README.md: {readme_path}")

        # Obtém uma frase de meme da API
        frase = obter_frase_meme()
        print(f"📝 Frase obtida: {frase}")

        if not frase:
            raise ValueError("Nenhuma frase foi obtida da API.")

        # Verifica se o arquivo README.md existe
        if not os.path.exists(readme_path):
            print("❌ O arquivo README.md não existe. Criando um novo arquivo.")
            open(readme_path, "w").close()

        # Adiciona a frase ao final do arquivo README.md
        with open(readme_path, "a") as f:
            f.write(f"\n{frase}\n")
        print(f"✅ Frase adicionada ao README.md: {frase}")

        # Log de sucesso
        registrar_log(
            event="readme_update",
            status="success",
            details="README.md atualizado com sucesso.",
            extra={"frase": frase}
        )
    except Exception as e:
        # Log de erro
        registrar_log(
            event="readme_update",
            status="error",
            details=f"Erro ao atualizar README.md: {e}"
        )
        print(f"❌ Erro ao atualizar README.md: {e}")

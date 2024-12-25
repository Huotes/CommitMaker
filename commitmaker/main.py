from .logger import registrar_log
from .commit import realizar_commit
from .readme_updater import atualizar_readme


def main():
    try:
        # Atualiza o README com uma frase de meme
        atualizar_readme()
        
        # Realiza o commit e push
        realizar_commit()
        
        # Registra o sucesso no log
        registrar_log("Commit realizado com sucesso.")
        
        print("🚀 Commit realizado com sucesso!")
    except Exception as e:
        # Registra qualquer erro no log
        registrar_log(f"Erro: {e}")
        print(f"❌ Erro: {e}")

if __name__ == "__main__":
    main()

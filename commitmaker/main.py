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
        registrar_log(
            event="main_execution",
            status="success",
            details="Commit realizado com sucesso.",
            extra=None
        )
        
        print("🚀 Commit realizado com sucesso!")
    except Exception as e:
        # Registra qualquer erro no log
        registrar_log(
            event="main_execution",
            status="error",
            details=f"Erro durante a execução principal: {e}",
            extra=None
        )
        print(f"❌ Erro: {e}")

if __name__ == "__main__":
    main()

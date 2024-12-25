import requests
from .logger import registrar_log

def obter_frase_meme():
    try:
        response = requests.get("https://geek-jokes.sameerkumar.website/api?format=json")
        if response.status_code == 200:
            data = response.json()
            joke = data.get("joke", "Não foi possível obter uma frase de meme agora.")
            
            registrar_log(
                event="api_call",
                status="success",
                details="Frase de meme obtida com sucesso.",
                extra={"frase": joke}
            )
            
            return joke
        else:
            registrar_log(
                event="api_call",
                status="error",
                details="Erro ao obter frase de meme da API.",
                extra={"status_code": response.status_code}
            )
            return "Erro ao obter frase de meme da API."
    except Exception as e:
        registrar_log(
            event="api_call",
            status="error",
            details=f"Erro na chamada da API: {e}"
        )
        return f"Erro na API: {e}"

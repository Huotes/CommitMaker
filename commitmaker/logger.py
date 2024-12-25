import os
import json
from datetime import datetime

REPO_PATH = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(REPO_PATH, "log.json")

def registrar_log(event, status, details, extra=None):
    """
    Registra um evento no arquivo de log JSON.

    :param event: Nome do evento (ex: 'commit', 'readme_update', 'api_call')
    :param status: Status do evento (ex: 'success', 'error')
    :param details: Detalhes adicionais sobre o evento
    :param extra: Dicionário opcional com informações extras
    """
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "event": event,
        "status": status,
        "details": details,
        "extra": extra or {}
    }

    # Verifica se o arquivo de log já existe e contém dados
    if os.path.exists(LOG_FILE):
        try:
            with open(LOG_FILE, "r") as f:
                logs = json.load(f)
        except json.JSONDecodeError:
            # Se o arquivo está corrompido ou vazio, começa uma nova lista de logs
            logs = []
    else:
        logs = []

    # Adiciona o novo log
    logs.append(log_entry)

    # Salva os logs atualizados no arquivo
    with open(LOG_FILE, "w") as f:
        json.dump(logs, f, indent=4)

    print(f"📝 Log registrado: {log_entry}")

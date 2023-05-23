from pathlib import Path
import json
import logging
import requests

meteo_endpoint = "https://api.open-meteo.com/v1/forecast?latitude=-25.43&longitude=-49.27&hourly=temperature_2m&daily=sunrise,sunset&timezone=America%2FSao_Paulo"


# Define como faremos o log das ações
logging.basicConfig()
logger = logging.getLogger("Interagi Popular")
logger.setLevel(logging.INFO)

session = requests.Session()

PASTA_ATUAL = Path(__file__).parent.resolve()
PASTA_DADOS = PASTA_ATUAL / "data"

if not PASTA_DADOS.exists():
    PASTA_DADOS.mkdir(parents=True, exist_ok=True)
    logger.info(f"Criada a pasta {PASTA_DADOS}")

response = session.get(meteo_endpoint)

if not response.status_code == 200:
    raise ValueError(f"Algo deu errado, a openmeteo retornou {response.status_code}")

data = response.json()

result = {}

result["sunrise"] = data["daily"]["sunrise"][0]
result["sunset"] = data["daily"]["sunset"][0]
result["temperature"] = {}

for horario, i in data.hourly.time:
    result["temperature"][horario] = data["hourly"]["temperature_2m"][i]

arquivo_dados = PASTA_DADOS / f"meteo.json"

with open(arquivo_dados, "w") as fh:
    json.dump(result, fh, indent=2)
    logger.info(f"Dados salvos em {arquivo_dados}")

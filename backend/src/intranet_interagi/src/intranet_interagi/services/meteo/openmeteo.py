import requests


BASE_URL = "https://api.open-meteo.com/v1/forecast"


def _formatar_resposta(data: dict) -> dict:
    """Parseia os dados obtidos da OpenMeteo.

       retorna um dicionários com informações meteorológicas.
    """
    dados_diarios = data["daily"]
    dados_hora = data["hourly"]
    sunrise = dados_diarios["sunrise"]
    sunset = dados_diarios["sunset"]
    horarios = dados_hora["time"]
    sequencia = dados_hora["temperature_2m"]
    temperatura = {hora: temp for hora, temp in zip(horarios, sequencia)}
    return {
        "sunrise": sunrise,
        "sunset": sunset,
        "temperature": temperatura
    }



def get_forecast(latitude, longitude, timezone):
    """Obtem os dados da openmeteo."""
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "timezone": timezone,
        "hourly": "temperature_2m",
        "daily": "sunrise,sunset",
        "forecast_days":1
    }
    response = requests.get(
        BASE_URL,
        params=params
    )
    data = response.json()
    return _formatar_resposta(data)

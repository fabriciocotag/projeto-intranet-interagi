from plone import api
from plone.restapi.services import Service
from intranet_interagi.services.meteo import openmeteo as meteo

class MeteoGet(Service):

    def reply(self):
        portal_url = api.portal.get().absolute_url()
        latitude, longitude, timezone = ['-25.43', '-49.27', 'America/Sao_Paulo']
        data = meteo.get_forecast(latitude, longitude, timezone)
        data["@id"] = f"{portal_url}/@meteo"
        return data
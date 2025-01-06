from .base import APIEndpoint

from exactonline.models.me import Me, MeList

class MeMethods(APIEndpoint):

    def __init__(self, api):
        super().__init__(api, 'current/Me', Me, MeList)

    def get(self):
        url = "{endpoint}".format(endpoint=self.endpoint())
        status, headers, respJson = self.api.get(url)
        if status != 200: return self.singleObject().parseError(status, respJson)
        return self.singleObject().parse(respJson['d']['results'][0])

from .base import APIEndpoint

from exactonline.models.salesentries import SalesEntryLineList, SalesEntryList, SalesEntry, SalesEntryLine

class SalesEntryMethods(APIEndpoint):

    def __init__(self, api):
        super().__init__(api, 'salesentry/SalesEntries')
    
    def list(self, select=[]):
        url = self.endpoint
        if select: url = '{url}&$select={select}'.format(url=url, select=",".join(select))

        status, headers, respJson = self.api.get(url)

        if status != 200: return SalesEntryList().parseError(respJson)

        return SalesEntryList().parse(respJson['d']['results'])

    def get(self, id, select=[]):

        # Retrieve Sales Entry
        url = "{endpoint}?$filter=EntryID eq guid'{id}'".format(endpoint=self.endpoint, id=id)
        if select: url = '{url}&$select={select}'.format(url=url, select=",".join(select))

        status, headers, respJson = self.api.get(url)

        if status != 200: return SalesEntry().parseError(respJson)

        salesEntry = SalesEntry().parse(respJson['d']['results'][0])

        # Retrieve Sales Lines
        url = "{endpoint}(guid'{entryId}')/SalesEntryLines".format(endpoint=self.endpoint, entryId=salesEntry.EntryID)
        status, headers, respJson = self.api.get(url)

        if status != 200: return SalesEntryLineList().parseError(respJson)
        salesEntryLines = SalesEntryLineList().parse(respJson['d']['results'])

        salesEntry.SalesEntryLines = salesEntryLines

        return salesEntry
    
    def create(self, object):
        pass
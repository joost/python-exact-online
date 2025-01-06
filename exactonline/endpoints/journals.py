from .base import APIEndpointWithDivision

from exactonline.models.journals import Journal, JournalList

class JournalMethods(APIEndpointWithDivision):

    def __init__(self, api):
        super().__init__(api, 'financial/Journals', Journal, JournalList)
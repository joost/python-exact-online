from .base import APIEndpointWithDivision

from exactonline.models.contacts import Contact, ContactList

class ContactMethods(APIEndpointWithDivision):

    def __init__(self, api):
        super().__init__(api, 'crm/Contacts', Contact, ContactList)
from .base import APIEndpointWithDivision

from exactonline.models.accounts import Account, AccountList

class AccountMethods(APIEndpointWithDivision):

    def __init__(self, api):
        super().__init__(api, 'crm/Accounts', Account, AccountList)
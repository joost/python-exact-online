from .base import APIEndpointWithDivision

from exactonline.models.glaccounts import GLAccountList, GLAccount

class GLAccountMethods(APIEndpointWithDivision):

    def __init__(self, api):
        super().__init__(api, 'financial/GLAccounts', GLAccount, GLAccountList)
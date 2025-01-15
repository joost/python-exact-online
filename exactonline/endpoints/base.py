from .. import config

class APIEndpoint:

    def __init__(self, 
        api, 
        endpoint,
        singleObject,
        listObject,
        pkField='ID'
    ):

        self.api = api
        self.endpointString = endpoint
        self.singleObject = singleObject
        self.listObject = listObject
        self.pkField = pkField

    def endpoint(self):
        return self.endpointString

    def list(self, select=[], filter=None, filter_operator='and'):
        """
        Retrieve a list of objects from the endpoint.

        Parameters:
        select (list): List of fields to select.
        filter (str or dict): Filter criteria. Can be a string or a dictionary.
            - Example with dictionary: filter={ 'Blocked' : 'false' }
            - Example with string: filter="Account eq guid'{account.ID}'"
        filter_operator (str): Logical operator for combining filters. Can be 'and' or 'or'.

        Returns:
        listObject: List of objects retrieved from the endpoint.
        """
        url = self.endpoint()
        
        if filter:
            if filter_operator not in ['and', 'or']:
                raise ValueError("'filter_operator' can only be 'and' or 'or'.")

            url = '{url}?$filter='.format(url=url)
            count = 0 # FIXME: Why do we have count?
            # if field is a string simply add it to the url
            if isinstance(filter, str):
                url = "{url}{filter}".format(url=url, filter=filter)
                count += 1
            # if field is a dictionary, loop through it
            elif isinstance(filter, dict):
                for field, value in filter.items():

                    # if not boolean, put single quotes around value
                    if value.lower() not in ['false', 'true']:
                        value = "'{value}'".format(value=value)

                    if count == 0:
                        url = "{url}{field} eq {value}".format(url=url, field=field, value=value)
                    else:
                        url = "{url} {operator} {field} eq {value}".format(url=url, operator=filter_operator, field=field, value=value)

                    count += 1

        if select:
            url = '{url}&$select={select}'.format(url=url, select=",".join(select))
        
        status, headers, respJson = self.api.get(url)
        if status != 200: return self.listObject().parseError(status, respJson)
        listObj = self.listObject().parse(respJson['d']['results'])

        while('__next' in respJson['d']):
            nextUrl = respJson['d']['__next']
            nextUrl = nextUrl.replace('{0}/{1}/'.format(self.api.config.BASE_URL, self.api.division), '')

            status, headers, respJson = self.api.get(nextUrl)
            if status != 200: return self.listObject().parseError(status, respJson)
            tempListObj = self.listObject().parse(respJson['d']['results'])

            for entryObj in tempListObj.items():
                listObj.add(entryObj)
        
        return listObj

    def get(self, id, select=[]):

        url = "{endpoint}?$filter={pkField} eq guid'{id}'".format(endpoint=self.endpoint(), pkField=self.pkField, id=id)
        if select: url = '{url}&$select={select}'.format(url=url, select=",".join(select))

        status, headers, respJson = self.api.get(url)

        if status != 200: return self.singleObject().parseError(status, respJson)

        return self.singleObject().parse(respJson['d']['results'][0])
    
    def filter(self, field, value, select=[]):
        url = "{endpoint}?$filter={field} eq {value}".format(endpoint=self.endpoint(), field=field, value=value)
        if select: url = '{url}&$select={select}'.format(url=url, select=",".join(select))

        status, headers, respJson = self.api.get(url)
        if status != 200: return self.listObject().parseError(status, respJson)
        listObj = self.listObject().parse(respJson['d']['results'])

        while('__next' in respJson['d']):
            nextUrl = respJson['d']['__next']
            nextUrl = nextUrl.replace('{0}/{1}/'.format(self.api.config.BASE_URL, self.api.division), '')

            status, headers, respJson = self.api.get(nextUrl)
            if status != 200: return self.listObject().parseError(status, respJson)
            tempListObj = self.listObject().parse(respJson['d']['results'])

            for entryObj in tempListObj.items():
                listObj.add(entryObj)
        
        return listObj

    def create(self, object):
        self.api.config.logger.debug("CREATE")
        url = self.endpoint()
        data = object.getJSON()

        status, headers, respJson = self.api.post(url, data)

        self.api.config.logger.debug(f"status: {status}")
        self.api.config.logger.debug(f"headers: {headers}")
        self.api.config.logger.debug(f"respJson: {respJson}")

        if status not in [200, 201]: return self.singleObject().parseError(status, respJson)

        return self.singleObject().parse(respJson['d'])
    
    def update(self, object):
        id = getattr(object, self.pkField)
        url = "{endpoint}(guid'{id}')".format(endpoint=self.endpoint(), id=id)
        data = object.getJSON()

        status, headers, respJson = self.api.put(url, data)

        if status not in [200, 204]: return self.singleObject().parseError(status, respJson)
        return True

    def delete(self, id):
        url = "{endpoint}(guid'{id}')".format(endpoint=self.endpoint(), id=id)
        data = None

        status, headers, respJson = self.api.delete(url, data)

        if status not in [200, 204]: return self.singleObject().parseError(status, respJson)
        return True

class RequiresFiltering:
    def list(self, select=[], filter=None, filter_operator='and'):
        if not filter:
            raise ValueError("Listing requires mandatory filtering. Specify a filter using the filter param. Syntax: { 'filter_field' : 'filter_value' }. ")
        
        return super().list(select, filter, filter_operator)

class APIEndpointWithDivision(APIEndpoint):
    def endpoint(self):
        # if not self.api.division:
        #     raise ValueError("Division is not set. Set the division using the api.division property.")
        self.api.checkDivision()
        endpointWithDivision = '{division}/{endpoint}'.format(division=self.api.division, endpoint=super().endpoint())
        return endpointWithDivision

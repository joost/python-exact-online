import os
from .base import APIEndpointWithDivision

from exactonline.models.documents import Document, DocumentAttachment, DocumentAttachmentList, DocumentList, DocumentType, DocumentTypeCategory, DocumentTypeCategoryList, DocumentTypeList, DocumentCategoryList
from exactonline.utils import encodeFileToB64, getFileName, getUrlFileName, encodeURLToB64

class DocumentMethods(APIEndpointWithDivision):

    def __init__(self, api):
        super().__init__(api, 'documents', Document, DocumentList)
    
    def list(self, select=[]):
        url = f"{self.endpoint()}/Documents".format(endpoint=self.endpoint)
        if select: url = '{url}/Documents&$select={select}'.format(url=url, select=",".join(select))

        status, headers, respJson = self.api.get(url)

        if status != 200: return DocumentList().parseError(status, respJson)

        return DocumentList().parse(respJson['d']['results'])
    
    def listTypes(self, select=[]):
        url = f"{self.endpoint()}/DocumentTypes".format(endpoint=self.endpoint)
        if select: url = '{url}/DocumentTypes&$select={select}'.format(url=url, select=",".join(select))

        status, headers, respJson = self.api.get(url)

        if status != 200: return DocumentTypeList().parseError(status, respJson)
        
        return DocumentTypeList().parse(respJson['d']['results'])

    def listCategories(self):
        url = f"{self.endpoint()}/DocumentCategories".format(endpoint=self.endpoint)

        status, headers, respJson = self.api.get(url)

        if status != 200: return DocumentCategoryList().parseError(status, respJson)
        
        return DocumentCategoryList().parse(respJson['d']['results'])



    def listTypeCategories(self, select=[]):
        url = f"{self.endpoint()}/DocumentTypeCategories".format(endpoint=self.endpoint)
        if select: url = '{url}/DocumentTypeCategories&$select={select}'.format(url=url, select=",".join(select))

        status, headers, respJson = self.api.get(url)

        if status != 200: return DocumentTypeCategoryList().parseError(status, respJson)
        
        return DocumentTypeCategoryList().parse(respJson['d']['results'])

    def get(self, id, select=[]):

        url = f"{self.endpoint()}/Documents?$filter=ID eq guid'{id}'".format(endpoint=self.endpoint, id=id)
        if select: url = '{url}&$select={select}'.format(url=url, select=",".join(select))

        status, headers, respJson = self.api.get(url)

        if status != 200: return Document().parseError(status, respJson)

        return Document().parse(respJson['d']['results'][0])

    # Example:
    # doc = exactonline.models.Document(
    #     Account='2928ba92-0440-4409-a43b-cf1e8a4eadde', # Klant OK
    #     Type=10,
    #     Subject='New Document',
    # )
    # exactDocument = exact_api.documents.create(doc, ['/path/to/pdf/file.pdf'])
    def create(self, document, attachments=[]):
    
        url = f"{self.endpoint()}/Documents".format(endpoint=self.endpoint)
        data = document.getJSON()

        # 1: create Document
        status, headers, respJson = self.api.post(url, data)
        if status not in [200, 201]: return Document().parseError(status, respJson)
        
        document = Document().parse(respJson['d'])

        # 2: create and link Attachments
        for attachment in attachments:
            # Initialize variables outside the 'if' scope
            attachmentB64 = None
            attachmentFileName = None
            # Check if the attachment is a file
            if os.path.isfile(attachment):
                attachmentB64 = encodeFileToB64(attachment)
                attachmentFileName = getFileName(attachment)
            elif attachment.startswith("http"):
                attachmentB64 = encodeURLToB64(attachment)
                attachmentFileName = getUrlFileName(attachment)
            else:        
                raise Exception("Attachment is not a file or url")
                            
            dAttachment = DocumentAttachment(
                Attachment=attachmentB64,
                Document=document.ID,
                FileName=attachmentFileName
            )

            data = dAttachment.getJSON()
            url = f"{self.endpoint()}/DocumentAttachments".format(endpoint=self.endpoint)
            status, headers, respJson = self.api.post(url, data)
            print(status, respJson)
            
            if status in [200, 201]: document.Attachments.add(dAttachment)
        
        return document
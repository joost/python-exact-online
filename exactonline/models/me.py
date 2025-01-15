from .base import ObjectListModel, BaseModel

class MeList(ObjectListModel):

    def __init__(self):
        super().__init__(list=[], listObject=None)

# <d:CurrentDivision m:type="Edm.Int32">3973860</d:CurrentDivision>
# <d:DivisionCustomer m:type="Edm.Guid">16cfedaa-6f5c-4559-b8c3-6b208c63ee9b</d:DivisionCustomer>
# <d:DivisionCustomerCode xml:space="preserve">          64683068</d:DivisionCustomerCode>
# <d:DivisionCustomerName>AMIKA</d:DivisionCustomerName>
# <d:DivisionCustomerVatNumber m:null="true" />
# <d:DivisionCustomerSiretNumber m:null="true" />
# <d:DossierDivision m:type="Edm.Int32" m:null="true" />
# <d:AccountingDivision m:type="Edm.Int32">3973860</d:AccountingDivision>
# <d:IsEmployeeSelfServiceUser m:type="Edm.Boolean">false</d:IsEmployeeSelfServiceUser>
# <d:IsMyFirmLiteUser m:type="Edm.Boolean">false</d:IsMyFirmLiteUser>
# <d:IsStarterUser m:type="Edm.Boolean">false</d:IsStarterUser>
# <d:IsMyFirmPortalUser m:type="Edm.Boolean">false</d:IsMyFirmPortalUser>
# <d:IsClientUser m:type="Edm.Boolean">true</d:IsClientUser>
# <d:FullName>Rachid Lechheb</d:FullName>
# <d:PictureUrl>https://start.exactonline.nl//docs/images/placeholder_contact_myeol.png</d:PictureUrl>
# <d:ThumbnailPicture m:type="Edm.Binary" m:null="true" />
# <d:ThumbnailPictureFormat m:null="true" />
# <d:UserID m:type="Edm.Guid">d998567f-c083-411e-bbb3-09f4119b4b3b</d:UserID>
# <d:UserName>rachid@amika.tech</d:UserName>
# <d:LanguageCode>nl-NL</d:LanguageCode>
# <d:Legislation m:type="Edm.Int64">1</d:Legislation>
# <d:Email>rachid@amika.tech</d:Email>
# <d:Title>tav</d:Title>
# <d:Initials m:null="true" />
# <d:FirstName>Rachid</d:FirstName>
# <d:MiddleName m:null="true" />
# <d:LastName>Lechheb</d:LastName>
# <d:Gender>V</d:Gender>
# <d:Nationality m:null="true" />
# <d:Language>NL</d:Language>
# <d:Phone>06245733609</d:Phone>
# <d:PhoneExtension m:null="true" />
# <d:Mobile m:null="true" />
# <d:ServerTime>2025-01-05T21:13:45</d:ServerTime>
# <d:ServerUtcOffset m:type="Edm.Double">3600</d:ServerUtcOffset>
# <d:EmployeeID m:type="Edm.Guid">00000000-0000-0000-0000-000000000000</d:EmployeeID>
# <d:CustomerCode xml:space="preserve">          64683068</d:CustomerCode>
# <d:PackageCode>EOLDeveloper</d:PackageCode>
# <d:IsOEIMigrationMandatory m:type="Edm.Boolean">false</d:IsOEIMigrationMandatory>
class Me(BaseModel):

    def __init__(self,
        CurrentDivision=None,
        DivisionCustomer=None,
        DivisionCustomerCode=None,
        DivisionCustomerName=None,
        DivisionCustomerVatNumber=None,
        DivisionCustomerSiretNumber=None,
        DossierDivision=None,
        AccountingDivision=None,
        IsEmployeeSelfServiceUser=None,
        IsMyFirmLiteUser=None,
        IsStarterUser=None,
        IsMyFirmPortalUser=None,
        IsClientUser=None,
        FullName=None,
        PictureUrl=None,
        ThumbnailPicture=None,
        ThumbnailPictureFormat=None,
        UserID=None,
        UserName=None,
        LanguageCode=None,
        Legislation=None,
        Email=None,
        Title=None,
        Initials=None,
        FirstName=None,
        MiddleName=None,
        LastName=None,
        Gender=None,
        Nationality=None,
        Language=None,
        Phone=None,
        PhoneExtension=None,
        Mobile=None,
        ServerTime=None,
        ServerUtcOffset=None,
        EmployeeID=None,
        CustomerCode=None,
        PackageCode=None
    ):

        super().__init__()

        self.CurrentDivision = CurrentDivision
        self.DivisionCustomer = DivisionCustomer
        self.DivisionCustomerCode = DivisionCustomerCode
        self.DivisionCustomerName = DivisionCustomerName
        self.DivisionCustomerVatNumber = DivisionCustomerVatNumber
        self.DivisionCustomerSiretNumber = DivisionCustomerSiretNumber
        self.DossierDivision = DossierDivision
        self.AccountingDivision = AccountingDivision
        self.IsEmployeeSelfServiceUser = IsEmployeeSelfServiceUser
        self.IsMyFirmLiteUser = IsMyFirmLiteUser
        self.IsStarterUser = IsStarterUser
        self.IsMyFirmPortalUser = IsMyFirmPortalUser
        self.IsClientUser = IsClientUser
        self.FullName = FullName
        self.PictureUrl = PictureUrl
        self.ThumbnailPicture = ThumbnailPicture
        self.ThumbnailPictureFormat = ThumbnailPictureFormat
        self.UserID = UserID
        self.UserName = UserName
        self.LanguageCode = LanguageCode
        self.Legislation = Legislation
        self.Email = Email
        self.Title = Title
        self.Initials = Initials
        self.FirstName = FirstName
        self.MiddleName = MiddleName
        self.LastName = LastName
        self.Gender = Gender
        self.Nationality = Nationality
        self.Language = Language
        self.Phone = Phone
        self.PhoneExtension = PhoneExtension
        self.Mobile = Mobile
        self.ServerTime = ServerTime
        self.ServerUtcOffset = ServerUtcOffset
        self.EmployeeID = EmployeeID
        self.CustomerCode = CustomerCode
        self.PackageCode = PackageCode
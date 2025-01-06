from .base import ObjectListModel, BaseModel

class WebhookSubscriptionList(ObjectListModel):

    def __init__(self):
        super().__init__(list=[], listObject=WebhookSubscription)

class WebhookSubscription(BaseModel):

    def __init__(self,
        ID=None,
        ClientID=None,
        Created=None,
        Creator=None,
        CreatorFullName=None,
        Description=None,
        Division=None,
        CallbackURL=None,
        Topic=None,
        UserID=None
    ):

        super().__init__()

        self.ID = ID
        self.ClientID = ClientID
        self.Created = Created
        self.Creator = Creator
        self.CreatorFullName = CreatorFullName
        self.Description = Description
        self.Division = Division
        self.CallbackURL = CallbackURL
        self.Topic = Topic
        self.UserID = UserID

from .base import ObjectListModel, BaseModel

# https://start.exactonline.nl/docs/HlpRestAPIResourcesDetails.aspx?name=ActivitiesTasks
class TaskList(ObjectListModel):

    def __init__(self):
        super().__init__(list=[], listObject=Task)

class Task(BaseModel):

    def __init__(self,
        ID=None,
        Account=None,
        AccountName=None,
        ActionDate=None,
        Attachments=None, # RequestAttachments - Attachments linked to the task
        Contact=None,
        ContactFullName=None,
        Created=None,
        Creator=None,
        CreatorFullName=None,
        CustomTaskType=None,
        Description=None,
        Division=None,
        Document=None,
        DocumentSubject=None,
        Employee=None,
        HID=None,
        Modified=None,
        Modifier=None,
        ModifierFullName=None,
        Notes=None,
        Opportunity=None,
        OpportunityName=None,
        Project=None,
        ProjectDescription=None,
        Status=None,
        StatusDescription=None,
        TaskType=None,
        TaskTypeDescription=None,
        User=None,
        UserFullName=None
    ):

        super().__init__()
        
        self.ID = ID
        self.Account = Account
        self.AccountName = AccountName
        self.ActionDate = ActionDate
        self.Attachments = Attachments
        self.Contact = Contact
        self.ContactFullName = ContactFullName
        self.Created = Created
        self.Creator = Creator
        self.CreatorFullName = CreatorFullName
        self.CustomTaskType = CustomTaskType
        self.Description = Description
        self.Division = Division
        self.Document = Document
        self.DocumentSubject = DocumentSubject
        self.Employee = Employee
        self.HID = HID
        self.Modified = Modified
        self.Modifier = Modifier
        self.ModifierFullName = ModifierFullName
        self.Notes = Notes
        self.Opportunity = Opportunity
        self.OpportunityName = OpportunityName
        self.Project = Project
        self.ProjectDescription = ProjectDescription
        self.Status = Status
        self.StatusDescription = StatusDescription
        self.TaskType = TaskType
        self.TaskTypeDescription = TaskTypeDescription
        self.User = User
        self.UserFullName = UserFullName
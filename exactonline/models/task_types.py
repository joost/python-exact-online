from .base import ObjectListModel, BaseModel

class TaskTypeList(ObjectListModel):

    def __init__(self):
        super().__init__(list=[], listObject=TaskType)

class TaskType(BaseModel):

    def __init__(self,
        ID=None,
        Created=None,
        Creator=None,
        CreatorFullName=None,
        Description=None,
        DescriptionTermID=None,
        Division=None,
        Modified=None,
        Modifier=None,
        ModifierFullName=None
    ):

        super().__init__()
        
        self.ID = ID
        self.Created = Created
        self.Creator = Creator
        self.CreatorFullName = CreatorFullName
        self.Description = Description
        self.DescriptionTermID = DescriptionTermID
        self.Division = Division
        self.Modified = Modified
        self.Modifier = Modifier
        self.ModifierFullName = ModifierFullName
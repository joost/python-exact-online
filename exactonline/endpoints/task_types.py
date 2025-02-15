from .base import APIEndpointWithDivision

from exactonline.models.task_types import TaskType, TaskTypeList

# https://start.exactonline.nl/docs/HlpRestAPIResourcesDetails.aspx?name=AccountancyTaskTypes
# Seems unrelated to Tasks
class TaskMethods(APIEndpointWithDivision):

    def __init__(self, api):
        super().__init__(api, 'accountancy/TaskTypes', TaskType, TaskTypeList)
from .base import APIEndpointWithDivision

from exactonline.models.tasks import Task, TaskList

class TaskMethods(APIEndpointWithDivision):

    def __init__(self, api):
        super().__init__(api, 'activities/Tasks', Task, TaskList)
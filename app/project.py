from dataclasses import dataclass, field

PROJECT_STATUS = {
    'CLOSED_STATUS': 0,
    'NEW_STATUS': 1,
    'IN_PROGRESS_STATUS': 2,
}

class InvalidProjectStatus(Exception):
    pass

@dataclass
class ProjectData:
    name: str
    description: str
    status: str
    id: int = field(default=None, compare=False)

class ProjectManager:

    def __init__(self, project: ProjectData):
        self.project = project

    def get(self):
        return self.project

    def update_status(self, updated_project_status):
        if updated_project_status not in PROJECT_STATUS.values():
            raise InvalidProjectStatus(self.project.id)
        self.project.status = updated_project_status

    def close(self):
        self.project.status = PROJECT_STATUS['CLOSED_STATUS']
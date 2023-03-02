PROJECT_STATUS = {
    'CLOSED_STATUS': 0,
    'NEW_STATUS': 1,
    'IN_PROGRESS_STATUS': 2,
}

class InvalidProjectStatus(Exception):
    pass

class Project():
    def __init__(self, id, name, description, status='new'):
        self.id = id
        self.name = name
        self.description = description
        self.update_status(status)

    def update_status(self, updated_project_status):
        if updated_project_status not in PROJECT_STATUS.values():
            raise InvalidProjectStatus(self.id)
        self.status = updated_project_status

    def close(self):
        self.status = PROJECT_STATUS['CLOSED_STATUS']
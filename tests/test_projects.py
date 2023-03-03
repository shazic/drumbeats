import pytest
from app.project import ProjectData
from app.project import ProjectManager
from app.project import PROJECT_STATUS
from app.project import InvalidProjectStatus

#####################################################################################################
# Test Implementation                                                                               #
#####################################################################################################
@pytest.fixture()
def sample_project():
    p = ProjectData('project name', 'project description', PROJECT_STATUS['NEW_STATUS'], '1')
    yield ProjectManager(p)

def test_should_return_a_new_project(sample_project):
    project = ProjectData(sample_project.get().name,
                      sample_project.get().description,
                      sample_project.get().status,
                      '2',
                      )
    assert project.id == '2'
    assert project.name == 'project name'
    assert project.description == 'project description'
    assert project.status == PROJECT_STATUS['NEW_STATUS']

def test_should_update_project_status_to_in_progress(sample_project):
    sample_project.update_status(PROJECT_STATUS['IN_PROGRESS_STATUS'])
    assert sample_project.get().status == PROJECT_STATUS['IN_PROGRESS_STATUS']

def test_should_throw_exception_for_invalid_project_status(sample_project):
    with pytest.raises(InvalidProjectStatus):
        sample_project.update_status('invalid status code')

def test_should_update_status_as_closed_on_closing_project(sample_project):
    sample_project.close()
    assert sample_project.get().status == PROJECT_STATUS['CLOSED_STATUS']


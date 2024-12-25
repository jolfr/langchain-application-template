import os
import pytest

def assert_file(root_path, relative_path):
    """
    Asserts whether a file exists at a path

    Args:
        root_path (string): The absolute path to the folder which contains the file
        relative_path (string): The relative path and name of the file
    """
    assert os.path.exists(f"{root_path}/{relative_path}"), f"{relative_path} does not exist"

def test_project_structure(setup_and_teardown):
    """
    Test for the existence of various files expected to be in the project.
    """
    project_path = setup_and_teardown["project_path"]
    
    assert_file(project_path, "pyproject.toml")
    assert_file(project_path, "README.md")
    assert_file(project_path, ".python-version")
    assert_file(project_path, ".gitignore")
    assert_file(project_path, "app/main.py")
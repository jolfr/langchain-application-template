import os
import pytest
import subprocess

def assert_file(root_path, relative_path):
    """
    Asserts whether a file exists at a path

    Args:
        root_path (string): The absolute path to the folder which contains the file
        relative_path (string): The relative path and name of the file
    """
    assert os.path.exists(f"{root_path}/{relative_path}"), f"{relative_path} does not exist"

def test_project_structure(generate_project):
    """
    Test for the existence of various files expected to be in the project.
    """
    project_path = generate_project["project_path"]
    
    assert_file(project_path, "pyproject.toml")
    assert_file(project_path, "README.md")
    assert_file(project_path, ".python-version")
    assert_file(project_path, ".gitignore")
    assert_file(project_path, ".env")
    assert_file(project_path, "app/main.py")
    
def test_project_tests(generate_project):
    """
    Run tests within the project.
    """
    project_path = generate_project["project_path"]
    try:
        subprocess.run(["uv", "run", "pytest"], cwd=project_path, capture_output=True, check=True, text=True)
    except subprocess.CalledProcessError as e:
        print(e.stdout)
        assert False, "At least one included template test failed. See above for details."
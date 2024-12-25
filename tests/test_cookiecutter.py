import os

def test_project_structure(setup_and_teardown):
    project_path = setup_and_teardown["project_path"]
    
    pyproject = f"{project_path}/pyproject.toml"
    assert os.path.exists(pyproject), "pyproject.toml does not exist"
    
    readme = f"{project_path}/README.md"
    assert os.path.exists(readme), "README.md does not exist"
    
    python_version = f"{project_path}/.python-version"
    assert os.path.exists(python_version), ".python-version does not exist"
    
    main = f"{project_path}/app/main.py"
    assert os.path.exists(main), "app/main.py does not exist"
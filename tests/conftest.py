from cookiecutter.main import cookiecutter
import os
import pytest
import random
import shutil
import string

@pytest.fixture
def generate_project():
    # Before each test (setup)
    print("\n[Setup] Generate a new project")
    project_slug = ''.join(random.choices(string.ascii_letters, k=10))
    extra_context = {
        "project_slug": project_slug
    }
    cookiecutter('.', no_input=True, output_dir=".pytest_cache", extra_context=extra_context)
    
    project_relative_path = f".pytest_cache/{project_slug}/"
    project_abs_path = os.path.abspath(project_relative_path)
    
    resource = {"project_path": project_abs_path}

    yield resource

    # After each test (teardown)
    print("[Teardown] Delete the generated project")
    
    try:
        shutil.rmtree(project_abs_path)
        print(f"Project '{project_slug}' and its contents deleted successfully.")
    except FileNotFoundError:
        print("The project does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    resource.clear()
    
import sys
import subprocess

def initialize_version_control() -> bool:
    print("Initializing version control...", end="")
    try:
        subprocess.run(["mv", ".env.template", ".env"], capture_output=True, check=True, text=True,)
        subprocess.run(["git", "init"], capture_output=True, check=True, text=True)
        subprocess.run(["git", "add", "."], capture_output=True, check=True, text=True)
        subprocess.run(["git", "commit", "-m", "chore: initialized project from langchain-application-template"], capture_output=True, check=True, text=True)
        print("done.")
        return True
    except subprocess.CalledProcessError as e:
        print("\nCommand failed with error:")
        print(e.stderr)
        return False
    
    
def initialize_environment() -> bool:
    print("Initializing virtual environment...", end="")
    try:
        subprocess.run(["uv", "sync"], capture_output=True, check=True, text=True)
        print("done.")
        return True
    except subprocess.CalledProcessError as e:
        print("\nCommand failed with error:")
        print(e.stderr)
        return False

if __name__ == "__main__":
    if not initialize_environment():
        print("\nERROR: environment was not initialized.")
        sys.exit(1)
    if not initialize_version_control():
        print("\nERROR: version control was not initialized.")
        sys.exit(1)
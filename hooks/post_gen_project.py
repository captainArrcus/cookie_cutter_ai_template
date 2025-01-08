import os
import subprocess

def run_command(command, error_message):
    """
    Helper function to run shell commands and handle errors.
    """
    try:
        subprocess.run(command, check=True, shell=True)
    except subprocess.CalledProcessError:
        print(f"ERROR: {error_message}")

def main():
    project_name = "{{ cookiecutter.project_name }}"
    repo_name = "{{ cookiecutter.repo_name }}"
    description = "{{ cookiecutter.description }}"
    create_github_repo = "{{ cookiecutter.create_github_repo }}".lower()

    # Initialize a local Git repo
    print("Initializing local Git repository...")
    run_command("git init", "Failed to initialize Git repository.")
    run_command("git add .", "Failed to stage files.")
    run_command(f"git commit -m 'Initial commit for {project_name}'", "Failed to make initial commit.")

    # Create GitHub repository if requested
    if create_github_repo == 'y':
        print(f"Creating GitHub repository '{repo_name}'...")
        run_command(
            f"gh repo create {repo_name} --private --description '{description}' --source . --push",
            "Failed to create GitHub repository or push to remote."
        )
        print(f"GitHub repository '{repo_name}' created successfully!")

if __name__ == "__main__":
    main()
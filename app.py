import subprocess
import sys
import os
import argparse
import json
import platform

# Define supported languages and their installation commands
supported_languages = {
    "python": "sudo apt-get install python3",
    "node": "sudo apt-get install nodejs",
    # Add more languages and their respective installation commands
}

def run_command(command):
    """
    Run a system command and handle errors.
    """
    try:
        subprocess.run(command, check=True)
        print(f"Command '{' '.join(command)}' executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while executing {' '.join(command)}: {e}")

def install_language(language):
    """
    Install or update a programming language using the system's package manager.
    """
    if language in supported_languages:
        print(f"Installing {language}...")
        run_command(supported_languages[language].split())
    else:
        print(f"{language} is not supported yet.")

def configure_git(username, email):
    """
    Configure global settings for Git.
    """
    run_command(["git", "config", "--global", "user.name", username])
    run_command(["git", "config", "--global", "user.email", email])

def create_project(language, project_name):
    """
    Create a new project directory with a basic structure.
    """
    os.makedirs(project_name, exist_ok=True)
    # Add more logic to create language-specific files and directories.
    print(f"{language} project {project_name} created.")

def check_system():
    """
    Check the current operating system and package manager.
    """
    os_info = platform.system().lower()
    if 'linux' in os_info:
        return 'apt'
    elif 'darwin' in os_info:
        return 'brew'
    elif 'windows' in os_info:
        return 'choco'
    else:
        return None

def main():
    parser = argparse.ArgumentParser(description="DevEnvCLI: Automate development environment setup")
    parser.add_argument("command", choices=["install", "configure", "create"], help="Command to execute")
    parser.add_argument("--language", help="Specify the programming language")
    parser.add_argument("--username", help="Git username")
    parser.add_argument("--email", help="Git email")
    parser.add_argument("--project", help="Project name")

    args = parser.parse_args()

    # Check the system's package manager
    package_manager = check_system()
    if not package_manager:
        print("Unsupported operating system.")
        sys.exit(1)

    if args.command == "install":
        install_language(args.language)
    elif args.command == "configure":
        configure_git(args.username, args.email)
    elif args.command == "create":
        create_project(args.language, args.project)
    else:
        print("Invalid command. Use 'install', 'configure', or 'create'.")

if __name__ == "__main__":
    main()

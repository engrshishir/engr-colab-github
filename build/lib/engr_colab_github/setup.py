import os
import subprocess
import sys
from github import Github
from pathlib import Path
from dotenv import load_dotenv, set_key, dotenv_values
import sys

load_dotenv()

env_vars = dotenv_values(
    Path(__file__).parent.parent / ".env"
)  
env_file_path = Path(__file__).parent.parent / ".env"
# Retrieve values from the .env file
active_repo = env_vars.get("ACTIVE_REPO")
user_name = env_vars.get("GITHUB_USER_NAME")

def get_token():
    token = env_vars.get("GITHUB_TOKEN")

    if token:
        print("✅ Found saved GitHub token in .env file.")
    else:
        # If no token in the .env file, ask the user for it
        has_token = input("Do you already have a GitHub personal access token? (yes/no): ").strip().lower()

        if has_token == "no":
            print("🔗 Create a GitHub personal access token here:")
            print("➡️ https://github.com/settings/personal-access-tokens")
            print("⚠️ Ensure you enable 'Repository' and 'Account' permissions!")

        token = input("🔑 Enter your GitHub personal access token: ").strip()
        set_key(env_file_path, "ACTIVE_REPO", token)
        
        print(f"✅ GitHub token saved in .env file at {env_file_path}")

    return token

def get_git_user_details():

    load_dotenv()

    user_name = env_vars.get("GITHUB_USER_NAME")
    user_email = env_vars.get("GITHUB_USER_EMAIL")
    
    if user_name and user_email:
        print(f"✅ Found saved GitHub username: {user_name} and email: {user_email} in .env file.")
    else:
        # If no username or email, prompt the user for input
        print("⚠️ Git username and email not set. Please enter them below.")
        user_name = input("👤 Enter your GitHub username: ").strip()
        user_email = input("📧 Enter your GitHub email: ").strip()

        # Save the username and email in the .env file for future use
        set_key(env_file_path, "GITHUB_USER_NAME", user_name)
        set_key(env_file_path, "GITHUB_USER_EMAIL", user_email)
        print(f"✅ GitHub username and email saved in .env file at {env_file_path}")

    return user_name, user_email

def setup():
    """Set up the GitHub configuration, including authentication token, username, and email."""
    # Ensure the token is available
    token = get_token()

    try:
        g = Github(token)
        g.get_user().login  # Validate token
        print("✅ GitHub authentication successful!")
    except Exception:
        print("❌ Invalid GitHub token! Please check and try again.")
        sys.exit(1)

    # Ensure the username and email are available and set them if not
    user_name, user_email = get_git_user_details()

    # Now set the Git configuration globally
    try:
        subprocess.run(["git", "config", "--global", "user.name", user_name], check=True)
        subprocess.run(["git", "config", "--global", "user.email", user_email], check=True)
        print(f"✅ Git configured with username: {user_name}, email: {user_email}")
    except subprocess.CalledProcessError:
        print("❌ Failed to configure Git. Ensure Git is installed and try again.")
        sys.exit(1)

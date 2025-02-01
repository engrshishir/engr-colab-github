import subprocess
from datetime import datetime
from pathlib import Path
import os
from dotenv import load_dotenv, set_key, dotenv_values
import sys

# Load environment variables from .env file
load_dotenv()

env_vars = dotenv_values(
    Path(__file__).parent.parent / ".env"
)  
# Retrieve values from the .env file
active_repo = env_vars.get("ACTIVE_REPO")
user_name = env_vars.get("GITHUB_USER_NAME")


def get_active_repo():
    return active_repo

def git_add():
    """Adds a file or folder to the staging area based on the active repository from .env."""
    active_repo = get_active_repo()

    if not active_repo:
        print("⚠️ No active repository. Please set or switch to a repository.")
        return

    path = input("➕ Enter file/folder to add: ").strip()

    # Check if the specified path exists in the repo directory
    if not Path(path).exists():
        print(f"⚠️ Path '{path}' does not exist.")
        return

    try:
        # Run the git add command
        subprocess.run(["git", "add", path], check=True)
        print(f"✅ '{path}' added to the staging area in repository '{active_repo}'.")
    except subprocess.CalledProcessError:
        print(f"❌ Failed to add '{path}' to the staging area.")

def git_commit():
    """Commits staged changes with a message."""
    message = input("📝 Enter commit message: ").strip()
    description = input("📜 Enter commit description (optional): ").strip()
    commit_message = f"{message}\n\n{description}" if description else message

    try:
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        print(f"✅ Changes committed: '{message}'")
    except subprocess.CalledProcessError:
        print("❌ Commit failed! Ensure changes are staged.")

def git_status():
    """Displays Git status."""
    try:
        subprocess.run(["git", "status"], check=True)
    except subprocess.CalledProcessError:
        print("❌ Failed to get Git status!")

def git_log():
    """Displays Git log."""
    try:
        subprocess.run(["git", "log"], check=True)
    except subprocess.CalledProcessError:
        print("❌ Failed to get Git log!")

def merge_branch():
    """Merges a specified Git branch."""
    branch_name = input("🔀 Enter branch to merge: ").strip()

    try:
        subprocess.run(["git", "merge", branch_name], check=True)
        print(f"✅ Branch '{branch_name}' merged successfully.")
    except subprocess.CalledProcessError:
        print(f"❌ Merge failed for branch '{branch_name}'.")

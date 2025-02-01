import subprocess
from datetime import datetime
from pathlib import Path
import os
from dotenv import load_dotenv, set_key, dotenv_values
import sys

env_vars = dotenv_values(
    Path(__file__).parent.parent / ".env"
)  
env_file_path = Path(__file__).parent.parent / ".env"
# Retrieve values from the .env file
active_repo = env_vars.get("ACTIVE_REPO")
user_name = env_vars.get("GITHUB_USER_NAME")


def git_add():
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

def git_push():
    if not active_repo:
        print("⚠️ No active repository. Please set or switch to a repository.")
        return

    # Check if there are any uncommitted changes first
    status_result = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
    
    # if status_result.stdout:
    #     print("⚠️ There are uncommitted changes. Commit them first.")
    #     return
    
    # Check if the local branch is ahead of the remote branch
    try:
        # Check for unpushed commits
        log_result = subprocess.run(["git", "log", "origin/master..HEAD", "--oneline"], capture_output=True, text=True)
        
        # if log_result.stdout.strip() == "":
        #     print("✅ No new commits to push.")
        #     return
        
        version = input("🚀 Enter version (e.g., v1): ").strip()
        commit_message = f"Version {version}: Pushed on {datetime.now().strftime('%d %b, %Y')}"

        try:
            # Stage all changes
            subprocess.run(["git", "add", "."], check=True)

            # Commit the changes
            subprocess.run(["git", "commit", "-m", commit_message], check=True)

            # Push changes to the remote repository
            subprocess.run(["git", "push", "origin", "main"], check=True)

            print(f"✅ Version {version} pushed successfully to {active_repo}!")
        except subprocess.CalledProcessError as e:
            print(f"❌ Push failed! Error: {e}")

    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to check for unpushed commits! Error: {e}")


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

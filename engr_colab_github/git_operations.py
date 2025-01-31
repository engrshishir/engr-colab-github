import subprocess
from datetime import datetime
from pathlib import Path
import os
from dotenv import load_dotenv

# Load environment variables from .env file
dotenv_path = os.path.join(os.getcwd(), ".env")
load_dotenv(dotenv_path)

# Retrieve values from the .env file
active_repo = os.getenv("ACTIVE_REPO")  # Repository name
user_name = os.getenv("GITHUB_USER_NAME")  # GitHub username

# Check if running in Colab and set up Git if necessary
try:
    subprocess.run(["git", "--version"], check=True)
except subprocess.CalledProcessError:
    print("⚠️ Git is not installed. Installing Git...")
    subprocess.run(["apt-get", "install", "git"], check=True)

def git_add():
    """Adds a file or folder to the staging area."""
    path = input("➕ Enter file/folder to add: ").strip()

    if not Path(path).exists():
        print(f"⚠️ Path '{path}' does not exist.")
        return

    try:
        subprocess.run(["git", "add", path], check=True)
        print(f"✅ '{path}' added to the staging area.")
    except subprocess.CalledProcessError:
        print(f"❌ Failed to add '{path}'.")


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
    """Pushes committed changes to GitHub."""
    global active_repo

    if not active_repo:
        print("⚠️ No active repository. Please set or switch to a repository.")
        return

    version = input("🚀 Enter version (e.g., v1): ").strip()
    commit_message = f"Version {version}: Pushed on {datetime.now().strftime('%d %b, %Y')}"

    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        remote_url = f"https://github.com/{user_name}/{active_repo}.git"
        subprocess.run(["git", "push", remote_url], check=True)
        print(f"✅ Version {version} pushed successfully to {active_repo}!")
    except subprocess.CalledProcessError as e:
        print(f"❌ Push failed! Error: {e}")


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

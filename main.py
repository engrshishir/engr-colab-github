import sys
from engr_colab_github.setup import setup
from engr_colab_github.repo_manager import create_repo, clone_repo, switch_repo
from engr_colab_github.git_operations import git_add, git_commit, git_push, force_push, git_status, git_log, merge_branch
from engr_colab_github.utils import author, delete_path
import os

def get_active_repo():
    """Get the active repository name from the .env file or environment."""
    try:
        from dotenv import load_dotenv
        load_dotenv()
        active_repo = os.getenv("ACTIVE_REPO")
        return active_repo if active_repo else "No active repo"
    except Exception as e:
        return "No active repo"

def main():
    setup()
    
    # Fetch the active repository
    active_repo = get_active_repo()

    # Define the active repository icon
    active_repo_icon = "📂"  # Folder/Repository Icon

    # Define icons for each action
    action_icons = {
        "1": "📝",  # Create Repository
        "2": "🔄",  # Clone Repository
        "3": "🔀",  # Switch Repository
        "4": "➕",  # Git Add
        "5": "✏️",  # Git Commit
        "6": "⬆️",  # Git Push
        "7": "⚡",  # Force Push
        "8": "📜",  # Git Status
        "9": "📊",  # Git Log
        "10": "🔨",  # Merge Branch
        "11": "🗑️",  # Delete File/Folder
        "12": "🔗",  # Open Author LinkedIn
        "13": "❌",  # Exit
    }

    functions = {
        "1": ("Create Repository", create_repo),
        "2": ("Clone Repository", clone_repo),
        "3": ("Switch Repository", switch_repo),
        "4": ("Git Add", git_add),
        "5": ("Git Commit", git_commit),
        "6": ("Git Push", git_push),
        "7": ("Force Push", force_push),
        "8": ("Git Status", git_status),
        "9": ("Git Log", git_log),
        "10": ("Merge Branch", merge_branch),
        "11": ("Delete File/Folder", delete_path),
        "12": ("Open Author LinkedIn", author),
        "13": ("Exit", sys.exit),
    }

    while True:
        # Print the active repository and the available actions in a table
        print("\n" + "="*50)
        print(f"{active_repo_icon} Active Repository: {active_repo}")
        print("="*50)

        print(f"{'Action':<5} | {'Description':<20} | {'Icon'}")
        print("-" * 60)

        for key, (desc, _) in functions.items():
            print(f"{key:<5} | {desc:<20} | {action_icons[key]}")
        
        print("="*50)

        choice = input("Enter your choice: ").strip()

        if choice in functions:
            action = functions[choice][1]  # Get the function
            action()  # Execute the function
        else:
            print("⚠️ Invalid choice! Please try again.")

if __name__ == "__main__":
    main()

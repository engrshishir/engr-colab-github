import sys
from engr_colab_github.setup import setup
from engr_colab_github.repo_manager import create_repo, clone_repo, switch_repo
from engr_colab_github.git_operations import git_add, git_commit, git_push, git_status, git_log, merge_branch
from engr_colab_github.utils import author, delete_path

#  
def main():
    setup()
    functions = {
        "1": ("Create Repository", create_repo),
        "2": ("Clone Repository", clone_repo),
        "3": ("Switch Repository", switch_repo),
        "4": ("Git Add", git_add),
        "5": ("Git Commit", git_commit),
        "6": ("Git Push", git_push),
        "7": ("Git Status", git_status),
        "8": ("Git Log", git_log),
        "9": ("Merge Branch", merge_branch),
        "10": ("Delete File/Folder", delete_path),
        "11": ("Open Author LinkedIn", author),
        "12": ("Exit", sys.exit),
    }

    while True:
        print("\nAvailable Actions:")
        for key, (desc, _) in functions.items():
            print(f"{key}. {desc}")

        choice = input("Enter your choice: ").strip()

        if choice in functions:
            action = functions[choice][1]  # Get the function
            action()  # Execute the function
        else:
            print("⚠️ Invalid choice! Please try again.")

if __name__ == "__main__":
    main()

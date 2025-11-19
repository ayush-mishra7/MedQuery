import os

# ---------------------------------------------
# Define folder structure
# ------------------------------------------------

folders = [
    "medquery",
    "medquery/app"
]

# ------------------------------------------
# Define empty files to be created
# -------------------------------------------

files = [
    "medquery/requirements.txt",
    "medquery/Dockerfile",
    "medquery/README.md",
    "medquery/app/main.py",
    "medquery/app/utils.py",
    "medquery/app/models.py"
]

# ------------------------------------------
# Create folders + empty files
# -----------------------------------------------

def create_project():
    print("Creating MedQuery project structure...\n")

    # Create folders
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
        print(f"Created folder: {folder}")

    # Create empty files
    for file_path in files:
        with open(file_path, "w") as f:
            pass
        print(f"Created empty file: {file_path}")

    print("\nAll folders and empty files created successfully!")


if __name__ == "__main__":
    create_project()
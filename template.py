import os

# Folders required for the project
folders = [
    "src",
    "src/agents",
    "src/pipelines",
    "src/utils",
    "src/api",
    "src/configs",
    "src/configs/prompts",
    "src/tests",
    "data",
    "docs"
]

files = [
    "src/__init__.py",
    "src/agents/__init__.py",
    "src/pipelines/__init__.py",
    "src/utils/__init__.py",
    "src/api/__init__.py",
    "src/configs/__init__.py",
    "src/tests/__init__.py",
    "src/utils/logger.py",
    "src/utils/config_manager.py",
    "src/configs/settings.yaml",
    "src/configs/prompts/base_prompts.txt",
    "main.py",
    "requirements.txt",
    "README.md",
    ".gitignore"
]

def create_structure():
    print("\nCreating project folder structure...\n")
    
    # Create folders
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
        print(f"[+] Folder created: {folder}")

    # Create files
    for file in files:
        with open(file, "w") as f:
            f.write("")  # create an empty file
        print(f"[+] File created: {file}")

    print("\nProject structure successfully created!\n")

if __name__ == "__main__":
    create_structure()

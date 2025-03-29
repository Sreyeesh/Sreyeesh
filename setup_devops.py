import os

# Define the folder structure (directories and files only)
folders = {
    "devops-scripts": [
        "ci-cd",
        "docker"
    ],
    "projects": [
        "docker-project"
    ],
    "docs": [
        "architecture",
        "workflows"
    ]
}

# Function to create the folder structure and empty files
def create_structure(base_path, folders):
    for root, subfolders in folders.items():
        root_path = os.path.join(base_path, root)
        os.makedirs(root_path, exist_ok=True)  # Create root folder
        for subfolder in subfolders:
            subfolder_path = os.path.join(root_path, subfolder)
            os.makedirs(subfolder_path, exist_ok=True)  # Create subfolder
            # Create an empty file in each subfolder
            open(os.path.join(subfolder_path, '.empty'), 'w').close()
            print(f"Created folder: {subfolder_path}")

    # Create an empty README.md file in the root of your project directory
    readme_path = os.path.join(base_path, "README.md")
    open(readme_path, 'w').close()  # Create an empty README file
    print(f"Created README.md at: {readme_path}")

# Set the base directory to your existing project directory
base_directory = "/home/sgarimella/dev/projects/Sreyeesh"

# Create the directory structure and empty files
create_structure(base_directory, folders)

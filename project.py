import os

# Main Project Folder
project_name = "retail-demand-forecasting-system"

# Folder Structure
folders = [
    ".github/workflows",

    "artifacts/models",
    "artifacts/scaler",
    "artifacts/reports",

    "config",

    "data/raw",
    "data/processed",
    "data/external",

    "notebook",

    "src/components",
    "src/pipeline",
    "src/utils",
    "src/entity",

    "frontend",

    "api",

    "templates",
    "static"
]

# Files Structure
files = [
    ".github/workflows/ci.yml",

    "config/config.yaml",

    "notebook/eda.ipynb",
    "notebook/feature_engineering.ipynb",
    "notebook/model_training.ipynb",

    "src/components/data_ingestion.py",
    "src/components/data_validation.py",
    "src/components/data_transformation.py",
    "src/components/feature_engineering.py",
    "src/components/model_trainer.py",
    "src/components/model_evaluation.py",
    "src/components/forecasting.py",

    "src/pipeline/training_pipeline.py",
    "src/pipeline/prediction_pipeline.py",

    "src/utils/logger.py",
    "src/utils/exception.py",
    "src/utils/helpers.py",

    "src/entity/config_entity.py",

    "frontend/streamlit_app.py",

    "api/app.py",

    "Dockerfile",
    "docker-compose.yml",

    "requirements.txt",
    "setup.py",
    "README.md",
    ".gitignore"
]

# Create Folders
for folder in folders:
    folder_path = os.path.join(project_name, folder)
    os.makedirs(folder_path, exist_ok=True)
    print(f"Created Folder: {folder_path}")

# Create Files
for file in files:
    file_path = os.path.join(project_name, file)

    # Create parent directory if not exists
    parent_dir = os.path.dirname(file_path)

    if parent_dir != "":
        os.makedirs(parent_dir, exist_ok=True)

    # Create file
    with open(file_path, "w") as f:
        pass

    print(f"Created File: {file_path}")

print("\n Complete Industry-Standard Project Structure Created Successfully!")
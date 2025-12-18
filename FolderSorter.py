import json
import os
from pathlib import Path
import shutil

# Load categories from JSON file
with open("categories.json", "r") as f:
    categories = json.load(f)

def organize_files(file_path):
    if not os.path.exists(file_path):
        print("The specified path does not exist.")
        return "Others"
    ext=Path(file_path).suffix.lower()
    for category,extensions in categories.items():
        if ext in extensions:
            return category
    return "Others"

def clean_folder(folder_path):
    folder = Path(folder_path)
    if not folder.exists():
        print("The specified folder does not exist.")
        return
    
    for item in folder.iterdir():
        if item.is_file():
            category=organize_files(item)
            target_dir=folder/category
            target_dir.mkdir(exist_ok=True)
        try:
            shutil.move(str(item), str(target_dir/item.name))
            print(f"Moved: {item.name} to {category}/")
        except Exception as e:
            print(f"Error moving {item.name}: {e}")
def main():
    target=input("Enter the path of the folder to clean: default=~/Downloads ").strip() or str(Path.home() / "Downloads")
    clean_folder(target)
    print("\nCleanup completed!")

main()
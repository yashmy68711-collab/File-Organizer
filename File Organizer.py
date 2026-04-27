import os
import shutil

print("File Organizer")

path = input("Enter folder path: ")

if not os.path.exists(path):
    print("Invalid path!")
    exit()

files = os.listdir(path)

file_types = {
    "Images": (".jpg", ".png", ".jpeg"),
    "Documents": (".pdf", ".docx", ".txt"),
    "Videos": (".mp4", ".mkv"),
    "Archives": (".zip", ".rar")
}

for file in files:
    file_path = os.path.join(path, file)
     if os.path.isdir(file_path) or file.startswith("."):
        continue  
    try:
        moved = False
        for folder, extensions in file_types.items():
            if file.lower().endswith(extensions):
                folder_path = os.path.join(path, folder)

                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                shutil.move(file_path, os.path.join(folder_path, file))
                print(f"Moved: {file} → {folder}")
                moved = True
                break

        if not moved:
            other_folder = os.path.join(path, "Others")
      
            if not os.path.exists(other_folder):
                os.makedirs(other_folder)

            shutil.move(file_path, os.path.join(other_folder, file))
            print(f"Moved: {file} → others")

    except Exception as e:
        print(f"Error moving {file}: {e}")

print("Files organized successfully!")):

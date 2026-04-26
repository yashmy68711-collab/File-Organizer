import os
import shutil

print("File Organizer")

path = input("Enter folder path: ")

if not os.path.exists(path):
    print("Invalid path!")
    exit()

files = os.listdir(path)

for file in files:
    file_path = os.path.join(path, file)
    if os.path.isdir(file_path):
        continue
    try:
        if file.endswith((".jpg", ".png", ".jpeg")):
            folder = "Images"

        elif file.endswith((".pdf", ".docx", ".txt")):
            folder = "Documents"

        elif file.endswith((".mp4", ".mkv")):
            folder = "Videos"

        elif file.endswith((".zip", ".rar")):
            folder = "Archives"

        else:
            folder = "Others"

        folder_path = os.path.join(path, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        # Move file
        shutil.move(file_path, os.path.join(folder_path, file))

        print(f"Moved: {file} → {folder}")

    except Exception as e:
        print(f"Error moving {file}: {e}")

print("Files organized successfully!")
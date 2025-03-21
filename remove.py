import os
import glob

def remove_box_files(directory):
    # Use glob to find all .box files in the directory and subdirectories
    box_files = glob.glob(os.path.join(directory, '**', '*.box'), recursive=True)
    
    if not box_files:
        print("No .box files found.")
        return
    
    for file in box_files:
        try:
            os.remove(file)  # Delete the file
            print(f"Deleted: {file}")
        except Exception as e:
            print(f"Failed to delete {file}: {e}")

# Specify the directory you want to scan
directory_to_scan = r'./'

# Call the function to remove .box files
remove_box_files(directory_to_scan)
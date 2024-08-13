import os

def replace_language_code_in_filenames(directory, target, replacement, include_subdirs=False):
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if target in filename:
                new_filename = filename.replace(target, replacement)
                os.rename(os.path.join(root, filename), os.path.join(root, new_filename))
                print(f"The file name has been successfully modified: {filename} -> {new_filename}")
            else:
                print(f"The {filename} file does not contain '{target}' in its name.")
        
        if not include_subdirs:
            break 

def main():
    target = input("What do you want to replace in the filenames? ")
    replacement = input(f"What do you want to replace '{target}' with? ")
    include_subdirs = input("Do you want to do this with the subfolders? (Yes/No): ")

    current_directory = os.getcwd()

    if include_subdirs.lower() == "yes":
        replace_language_code_in_filenames(current_directory, target, replacement, include_subdirs=True)
    elif include_subdirs.lower() == "no":
        replace_language_code_in_filenames(current_directory, target, replacement, include_subdirs=False)
    else:
        print("Please respond with 'Yes' or 'No'.")

if __name__ == "__main__":
    main()

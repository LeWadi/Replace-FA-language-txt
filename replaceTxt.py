import os

def replace_language_code_in_filenames():
    current_directory = os.getcwd() 
    for filename in os.listdir(current_directory):
        if "to_replace" in filename:
            new_filename = filename.replace("to_replace", "whatever_you_want_to_put")
            os.rename(filename, new_filename)
            print(f"The filename has been successfully changed: {filename} -> {new_filename}")
        else:
            print(f"The file {filename} does not contain 'to_replace' in its name.")

def main():
    confirm = input("Do you want to replace 'to_replace' with 'fr' in the filenames of this folder? (Yes/No): ")
    if confirm.lower() == "yes":
        replace_language_code_in_filenames()
    elif confirm.lower() == "no":
        print("The program has been stopped.")
    else:
        print("Please respond with 'Yes' or 'No'.")

if __name__ == "__main__":
    main()

import os
def filter_files(folder_path):
    filtered_files = []

    if not os.path.isdir(folder_path):
        print("Invalid folder path.")
        return []

    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path) and (file_name.startswith("short") or file_name.startswith("long")):
            filtered_files.append(file_name)

    return filtered_files

def remove_newlines(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read().replace('\n', ' ')

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

if __name__ == "__main__":
    folder_path = "./Simplified Chinese"  # Change this to your file path
    files=filter_files(folder_path)
    print(len(files))

    for f in files:
        if "ref" not in f: continue
        print(f)

        remove_newlines(os.path.join(folder_path,f))
        print("Newlines removed and content updated in the file.")


import pathlib

path_folder = pathlib.Path.home() / "my_folder"/"my_file.txt"
path_folder.mkdir(exist_ok=True)
print(path_folder.exists())

file_path = path_folder
print(file_path.exists())
print(file_path)


print(path_folder.parent)
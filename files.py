import pathlib

path = pathlib.Path("c:/reload/hello.txt")
path1 = pathlib.Path("c:/user/desktop")
path2 = pathlib.Path.cwd() / "felix" / "numbers" / "green.csv"
path2.mkdir(exist_ok=True)

new_file_path = path2 / "p rivate txt"
new_file_path.touch()

print(path.anchor)
print(path1.name)
print(path1.suffix)
print(path2.exists())
print(list(path2.parents))

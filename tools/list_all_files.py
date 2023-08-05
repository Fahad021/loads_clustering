from explorer import get_folders, get_files, get_subroots


files = []
root = "RESIDENTIAL/"
for subroot in get_subroots(root):
    for folder in get_folders(root + subroot):
        files.extend(iter(get_files(root + subroot + folder)))
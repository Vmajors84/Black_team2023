import os
import json

current_working_directory: str = os.getcwd()
directory_entries = os.scandir(current_working_directory)
file_dictionary: dict = {}

for entry in directory_entries:
    if entry.is_file():
        entry_dict: dict = {}
        entry_dict['name'] = entry.name
        entry_dict['path'] = entry.path
        size_in_bytes = entry.stat().st_size
        size_in_kilobytes = size_in_bytes / 1000
        entry_dict['size'] = "{} KB".format(size_in_kilobytes)
        file_dictionary[entry.name] = entry_dict
print("Files in current working directory:\n {}".format(file_dictionary))
print("\n\nFiles in current working directory formatted to json: ")
print(json.dumps(file_dictionary, sort_keys=True, indent=2))

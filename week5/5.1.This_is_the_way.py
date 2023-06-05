import os
"""
     Gets the folder path from the user, when a file starts with the word "deep" returns it.
    :param user_path: the folder path that is given from the user
    :return: all files that start with the word "deep" into a list
    """


def files_startswith_deep(path):
     return [file for file in os.listdir(path) if file.startswith("deep")]


if __name__ == '__main__':
    path_dir = input("Enter a path file: ")
    deep_file = files_startswith_deep(path_dir)
    for file in deep_file:
        print(file)

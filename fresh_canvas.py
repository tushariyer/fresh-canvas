#!/usr/bin/env python

import os
from directories import paths as path_list
from directories import dont_init_as_py
from canvas_utilities import get_all_subdirectories as get_dirs
from canvas_utilities import create_sample_test
from canvas_utilities import create
from canvas_utilities import save_base_gitignore


def new(name):
    print(f'Creating directories for {name}')
    os.mkdir(name)
    save_base_gitignore(name)
    project_root_dir = os.getcwd()
    for path in path_list:
        os.makedirs(path)

    created_directories = get_dirs(project_root_dir)

    create("main")

    print('Initializing Python directories')
    for directory in created_directories:
        if any(x not in directory for x in dont_init_as_py):
            os.chdir(directory)
            open("__init__.py", "w")

            if directory.endswith("Test"):
                print('Creating sample Python test')
                create_sample_test()
            elif directory.endswith("API"):
                create("controller")
            elif directory.endswith("Read"):
                create("read_data")
            elif directory.endswith("Write"):
                create("write_data")

            os.chdir(project_root_dir)

    print('Running Sample Test')
    os.system('python3 -m unittest Test')


if __name__ == '__main__':
    project_name = input("Enter Project Name:\n")
    if len(project_name) > 0:
        new(project_name)
    else:
        print(f'Project name cannot be empty')

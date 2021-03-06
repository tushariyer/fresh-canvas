#!/usr/bin/env python

import os

from Data.BaseCanvasData import directories
from Core.Utilities import canvas_utilities as cutils


def new(name, is_github):
    # Kickoff
    print(f'Creating directories for {name}')
    os.mkdir(name)
    cutils.save_base_gitignore(name)
    project_root_dir = os.getcwd()
    path_list = directories.paths
    created_sample_test = False

    # Check if the project should have basic GitHub Actions created for it
    if is_github == "n":
        path_list = directories.remove_github_path()

    # Create all the base paths
    for path in path_list:
        os.makedirs(path)

    created_directories = cutils.get_all_subdirectories(project_root_dir)
    cutils.create("main")

    print('Initializing Python directories')
    for directory in created_directories:
        # Add basic GitHub Actions
        if directory.endswith("workflows"):
            print('Adding Base GitHub Actions')

        # Don't add __init__.py files anywhere we don't need them
        if any(x not in directory for x in directories.dont_init_as_py):
            os.chdir(directory)
            open("__init__.py", "w")

            # Add a sample unit Test so the users have a starting point
            if directory.endswith("Test"):
                print('Creating sample Python Test')
                cutils.create_sample_test()
                created_sample_test = True
            elif directory.endswith("API"):
                cutils.create("controller")  # Basic API Controller file
            elif directory.endswith("Read"):
                cutils.create("read_data")
            elif directory.endswith("Write"):
                cutils.create("write_data")

            # Go back to the root. Theoretically if we were able to
            # create a Test sample then we should be able to run
            # tests and assert that python stuff is good to go
            os.chdir(project_root_dir)

    if created_sample_test:
        print('Running Sample Test')
        os.system('python3 -m unittest Test')


if __name__ == '__main__':
    # User Prompts
    project_name = input("Enter Project Name:\n")
    is_github_project = input("Is this a GitHub hosted solution? (y/n)\n")

    if len(project_name) > 0:
        new(project_name, is_github_project)
    else:
        print(f'Project name cannot be empty')

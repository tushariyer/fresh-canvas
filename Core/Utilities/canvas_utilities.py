import os


def get_all_subdirectories(root_dir):
    return [x[0] for x in os.walk(root_dir)]


def create_sample_test():
    open('test_controller.py', 'w')
    open('test_read_data.py', 'w')
    open('test_write_data.py', 'w')
    sample_test_file = "import unittest\n\n\nclass TestSum(unittest.TestCase):\n\n\tdef " \
                       "test_sum(self):\n\t\tself.assertEqual(sum([1, 2, 3]), 6, \"Should be " \
                       "6\")\n\n\nif __name__ == '__main__':\n\tunittest.main()\n"
    with open('test_sample_sum.py', 'w') as f:
        f.write(sample_test_file)


def create(file):
    open(f'{file}.py', 'w')


def read_gitignore():
    with open('Data/BaseCanvasData/base.gitignore') as f:
        file = f.read()
        f.close()
        return file


def save_base_gitignore(dest_dir):
    print("Creating GitIgnore")
    gitignore_file = read_gitignore()

    os.chdir(dest_dir)
    f = open('../.gitignore', 'w')
    f.write(gitignore_file)
    f.close()

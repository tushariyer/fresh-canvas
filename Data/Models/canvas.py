import Data.BaseCanvasData.directories as base_dir

class Canvas:
    def __init__(self, name):
        self.name = name
        self.cicd_details = None
        self.project_details = {}
        self.python_directories = base_dir.base_paths
        self.non_python_directories = []

    def create_cicd_template(self, code_hosting_method):
        details = {
            "Code Hosting Method": code_hosting_method
        }
        if code_hosting_method == "Github":
            self.non_python_directories.append(base_dir.github_path)
            details["CICD Directory"] = ".github"
        else:
            self.non_python_directories.append(base_dir.cicd_path)
            details["CICD Directory"] = base_dir.cicd_path

        self.cicd_details = details

    def collect_python_directories(self, is_api=True, has_database=True):
        if is_api:
            self.python_directories.append(base_dir.api_path)

        if has_database:
            self.python_directories.append(base_dir.database_paths)

        return self.python_directories

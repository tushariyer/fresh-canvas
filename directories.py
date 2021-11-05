import os

separator = os.sep

api_path = str("API" + separator + "Blueprints")
test_path = "Test"
cicd_path = "CICD"
data_models_path = str("Data" + separator + "Models")
data_read_path = str("Data" + separator + "Read")
data_write_path = str("Data" + separator + "Write")
core_util_path = str("Core" + separator + "Utilities")
core_int_path = str("Core" + separator + "Integration")
core_auth_path = str("Core" + separator + "Auth")
core_app_path = str("Core" + separator + "App")
github_path = str(".github" + separator + "workflows")

paths = [
    api_path,
    test_path,
    cicd_path,
    core_app_path,
    core_util_path,
    core_int_path,
    core_auth_path,
    data_models_path,
    data_read_path,
    data_write_path,
    github_path
]

dont_init_as_py = [
    "CICD",
    ".github",
    "workflows"
]


def remove_github_path():
    return paths[:-1]

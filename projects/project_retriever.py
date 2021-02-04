import json


def get_projects():
    """
    Loads the json package to retrieve projects and information.
    :return: json
    """
    projects = {}

    with open("projects/package.json") as json_file:
        projects = json.load(json_file)

    return projects

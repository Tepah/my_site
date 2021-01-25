import flask

import projects.project_retriever as project_retriever

blueprint = flask.Blueprint('projects', __name__, template_folder='templates')


@blueprint.route('/project/<project_name>')
# @response(template_file='projects/info.html')
def project_details(project_name: str):
    """ Starts the layout for the projects in the website. """
    return "Package details for {}".format(project_name)

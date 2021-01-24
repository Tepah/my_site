import flask

import projects.project_retriever as project_retriever
from infrastructure.view_modifiers import response

blueprint = flask.Blueprint('projects', __name__, template_folder='templates')


@blueprint.route('/project/<project_name>')
# @response(template_file='projects/info.html')
def project_details(project_name: str):
    return "Package details for {}".format(project_name)

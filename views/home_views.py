import flask

import projects.project_retriever as project_retriever
from infrastructure.view_modifiers import response

blueprint = flask.Blueprint('home', __name__, template_folder='templates')


@blueprint.route('/')
@response(template_file='home/index.html')
def index():
    test_projects = project_retriever.get_projects()
    return {'projects': test_projects}


@blueprint.route('/about')
@response(template_file='home/about.html')
def about():
    return {}

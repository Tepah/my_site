import flask

import projects.project_retriever as project_retriever

blueprint = flask.Blueprint('home', __name__, template_folder='templates')


@blueprint.route('/')
def index():
    test_projects = project_retriever.get_projects()
    return flask.render_template('home/index.html', projects=test_projects)


@blueprint.route('/about')
def about():
    return flask.render_template('home/about.html')

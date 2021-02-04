import flask

import projects.project_retriever as project_retriever

# SETUP
blueprint = flask.Blueprint('home', __name__, template_folder='templates')


@blueprint.route('/')
def index():
    """
    Creates a list of projects from the project json that defines how many projects are on the index page.
    Then shows the index page with those projects.
    :return: flask render of index.html
    """
    test_projects = list(project_retriever.get_projects().values())
    return flask.render_template('home/index.html', projects=test_projects)


@blueprint.route('/about')
def about():
    """
    Shows the about page
    :return: flask render of about.html
    """
    return flask.render_template('home/about.html')

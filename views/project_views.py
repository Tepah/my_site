import flask

import projects.project_retriever as project_retriever

blueprint = flask.Blueprint('projects', __name__, template_folder='templates')


@blueprint.route('/project/<project_name>')
def project_details(project_name: str):
    """
    Starts the layout for the projects in the website.
    :param project_name: str
    :return: Flask template website. Either info or error
    """

    all_projects = project_retriever.get_projects()

    if project_name in all_projects.keys():
        return flask.render_template('projects/info.html', project=all_projects[project_name])
    else:
        return flask.render_template('projects/error.html', project=project_name)

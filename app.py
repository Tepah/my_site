import flask

from projects.project_views import get_projects

app = flask.Flask(__name__)


@app.route('/')
def index():
    test_projects = get_projects()
    return flask.render_template('home/index.html', projects=test_projects)


@app.route('/about')
def about():
    return flask.render_template('home/about.html')


if __name__ == '__main__':
    app.run()

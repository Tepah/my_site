import flask

app = flask.Flask(__name__)


def get_projects():
    return [
        {'name': 'Space Pew', 'type': 'Game'},
        {'name': 'Stat tracker', 'type': 'Data logger'},
        {'name': 'Pete-bot', 'type': 'Discord Bot'}
    ]


@app.route('/')
def index():
    test_projects = get_projects()
    return flask.render_template('index.html', projects=test_projects)


@app.route('/about')
def about():
    return flask.render_template('about.html')


if __name__ == '__main__':
    app.run()

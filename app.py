import flask

# SETUP
app = flask.Flask(__name__)


def main():
    """
    Registers blueprints and runs the website
    :return: None
    """
    register_blueprints()
    app.run(debug=True)


def register_blueprints():
    """
    manages blueprints and views to open those specific pages
    :return: None
    """
    from views import home_views
    from views import project_views

    app.register_blueprint(home_views.blueprint)
    app.register_blueprint(project_views.blueprint)


if __name__ == '__main__':
    main()
else:
    register_blueprints()

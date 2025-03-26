from flask import Flask
from schema import schema
from strawberry.flask.views import GraphQLView

app = Flask(__name__)
app.add_url_rule(
    "/graphql", view_func=GraphQLView.as_view("graphql", schema=schema)
)


if __name__ == "__main__":
    app.run(debug=True)
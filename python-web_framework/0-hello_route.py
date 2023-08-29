# importing from flask
from flask import Flask  # Flask being imported

# this is needed so flask knows where to look up resources
app = Flask(__name__)


# this is a decorator used to show flask what URL it'll trigger
@app.route("/", strict_slashes=False)
def hello():
    return "<p>Hello HBNB!</p>"

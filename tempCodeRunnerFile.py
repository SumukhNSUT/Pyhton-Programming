from demo import Flask, request

app = Flask(__name__)

# Route for the homepage


@app.route('/')
def index():
    return 'Welcome to the homepage!'

# Route for handling GET requests


@app.route('/get', methods=['GET'])
def handle_get():
    return 'GET request received.'

# Route for handling POST requests


@app.route('/post', methods=['POST'])
def handle_post():
    return 'POST request received.'


if __name__ == '__main__':
    app.run(debug=True)

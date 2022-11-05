# Import Flask to allow us to create our app
from flask import Flask, render_template
# Create a new instance of the Flask class called "app"
app = Flask(__name__)


# The "@" decorator associates this route with the function immediately following
@app.route('/')
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response


@app.route('/dojo')
def dojo():
    return "dojo"


# for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
@app.route('/say/<flask>')
def say(flask):
    print(flask)
    return "Hi " + flask + "!"

# for a route '/users/____/____', two parameters in the url get passed as username and id


@app.route('/repeat/<id>/<username>')
def printName(id, username):
    print(id)
    print(username)
    return username * int(id)


def not_found(e):
    # defining function
    return render_template("404.html")


if __name__ == "__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.

from flask import Flask

app = Flask(__name__)

@app.route("/")
def mainPage():
    return "navigate to any sub-url to access this website!!!"

@app.route("/<subUrl>")
def subPage(subUrl):
    return f"You are in {subUrl} Page"

if __name__ == '__main__':
    app.run(debug=True)
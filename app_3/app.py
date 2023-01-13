from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def mainPage():
    return "navigate to any sub-url to access this website!!!"

@app.route("/<subUrl>")
def subPage(subUrl):
    return render_template("index.html",input=subUrl)

if __name__ == '__main__':
    app.run(debug=True)
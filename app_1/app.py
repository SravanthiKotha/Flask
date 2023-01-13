from flask import Flask

app = Flask(__name__)

users = ['sravanthi','Murali',"Harshit"]

@app.route("/<user>")
def myHomePage(user):
    if(user in users):
     return f"Welcome to Home Page {user}"
    else:
        return f"User not found!!!!"


@app.route("/about-us")
def about_us():
    return "About Page"

if(__name__ == "__main__"):
    app.run(debug=True)
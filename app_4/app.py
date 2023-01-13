from flask import Flask,request

app = Flask(__name__)



@app.route("/",methods=['POST','GET'])
def mainPage_Post():
    if(request.method == 'POST'):
        return "This is the POST request"
    return "This is the GET request"

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def base_page():
    return render_template("index.html")



@app.route("/thankyou", methods=['POST','GET'])
def register():
    if(request.method=='POST'):
        return render_template("thanku.html",email=request.form.get("email"))

    return "Please try to register!!!"
if(__name__ == "__main__"):
    app.run(debug=True,host='0.0.0.0')
from crypt import methods
from flask import Flask, jsonify, redirect, render_template ,request, url_for, crypt
app =Flask(__name__)

studentDB = [
    { "rollno": '11',
     "name": "Mary Denis",
     "section": 'A' 
     },
    {
        "rollno": '12',
        "name": "Phil cousol",
        "section": 'B'
    }
]

@app.route('/', methods=['GET'])
def welcome():
    return 'Welcome to the webservice'

@app.route("/student/getstudents", methods=['GET'])
def getstudents():
    return jsonify({"stud":studentDB})

@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method =="POST":
        user = request.form["nm"]
        return redirect(url_for("user", usr=user))        
    else:        
        return render_template("login.html")

@app.route('/<usr>')
def user(usr):
    return f"<h1>{usr}</h1>"
    

if __name__ == '__main__':
    app.run(debug =True)
    
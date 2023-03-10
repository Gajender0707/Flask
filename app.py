from flask import Flask

app=Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to my Home Page of the flask. I will use this for my ML model"

@app.route("/Team")
def invitation():
    return "Hey My cuties, You are most welcome in my github"

if __name__=="__main__":
    app.run(debug=True)
from flask import Flask,redirect,url_for

app=Flask(__name__)

@app.route("/")
def welcome():
    return redirect("/out")

@app.route("/out")
def out():
    return "this is indecating to out from the concept"

@app.route("/success/<int:score>")
def success(score):
    return f"You got the {score} which is extracted from the url "

@app.route("/result/<int:score>")
def result(score):
    if score>33:
        return f"Congratulation ! You are pass and get the {score} Marks..."
    if score<33:
        return f"Sorry! You are Fail and you get the {score} Marks...."





if __name__=="__main__":
    app.run(debug=True)
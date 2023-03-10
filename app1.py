## Building the Url daynamaclly
from flask import Flask,redirect,url_for

app=Flask(__name__)

@app.route("/")
def urlfunc():
    return "This is my trial url which I am trying to just check it out "

@app.route("/pass/<int:score>")  #this is way in which app.route take the input in the url
def success(score):
    return "The person is passed and the marks is "+str(score)

@app.route("/fail/<int:score>")
def fail(score):
    return "The Student is failed becuase of he get on the "+str(score)+ " Marks. "

@app.route("/result/<int:score>")
def result(score):
    if score>33:
        return "The Person Has been Passed and get the "+str(score)+" Marks"
    else:
        return "The Student is failed due to he has the marks "+str(score)+" Which are not sufficient for passed"


if __name__=="__main__":
    app.run(debug=True)
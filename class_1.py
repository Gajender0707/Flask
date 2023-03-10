from flask import Flask

app=Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello Friends and You should welcome me......."

@app.route("/hindi")
def Hindi():
    return "Kaise ho dosto?????"




if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8080,debug=True)
# if __name__=="__main__":
#     app.run(debug=True)
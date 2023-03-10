##integrating html with flask
##http verb like post and get

from flask import Flask,url_for,redirect,render_template,request
app=Flask(__name__)

@app.route("/")
def Home():
    return render_template("index.html")


@app.route("/pass/<total_marks>")
def Pass(total_marks):
    return render_template("result.html",result=total_marks)



@app.route("/fail/<total_marks>")
def Fail(total_marks):
    return render_template("result.html",result=total_marks)


@app.route("/submit",methods=["POST","GET"])
def submit():
    if request.method=="POST":
        english=float(request.form["English_Marks"])
        maths=float(request.form["Maths_Marks"])
        Physics=float(request.form["Physics_Marks"])
        chem=float(request.form["Chemistry_Marks"])
        total_marks=english+maths+Physics+chem
        if total_marks>250:
            return f"You are Pass and got {total_marks} Marks.."

            #return redirect(url_for("/pass",total_marks))
        else:
            return f"You are fail becuase you got only {total_marks} score"
            #return redirect(url_for("/fail",total_marks))


if __name__=="__main__":
    app.run(debug=True)
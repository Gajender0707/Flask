##integrating html with flask
##http verb like post and get

from flask import Flask,url_for,redirect,render_template,request
app=Flask(__name__)

@app.route("/")
def Home():
    return render_template("index.html")


@app.route("/pass/<int:total_marks>")
def Pass(total_marks):
    return f"this is pass route and pass marks is {total_marks} "



@app.route("/fail/<int:total_marks>")
def Fail(total_marks):
    return f"this is fail route and failing marks is {total_marks} "


@app.route("/submit",methods=["POST","GET"])
def submit():
    if request.method=="POST":
        english=float(request.form["English_Marks"])
        maths=float(request.form["Maths_Marks"])
        Physics=float(request.form["Physics_Marks"])
        chem=float(request.form["Chemistry_Marks"])
        total_marks=english+maths+Physics+chem
        # if total_marks>250:
        #     return render_template("pass.html",T_marks=total_marks)
        # else:
        #     return render_template("fail.html",T_marks=total_marks)
        res=""
    if total_marks>250:
        res="pass"
    else:
        res="fail"
    return(redirect(url_for(res,total_marks=total_marks)))



if __name__=="__main__":
    app.run(debug=True)
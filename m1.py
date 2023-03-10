from flask import Flask,redirect,render_template,url_for,request

app=Flask(__name__)

@app.route("/")
def Home():
    return render_template("index.html")

@app.route("/admin/<detail>")
def admin(detail):
    return render_template("admin_detail.html",n=detail)

@app.route("/gajender/<name>")
def gajender(name):
    return f"This is Main Boss of the this code and  detail and boss name is {name}"

@app.route("/login",methods=["POST","GET"])
def login():
    if request.method=="POST":
        name=request.form["Name"]
        password=request.form["Password"]

        if name=="admin":
            detail={"name of admin":name,"Passowrd of admin":password}
            return redirect(url_for("admin",detail=detail))
        
        elif name=="Gajender":
            return redirect(url_for("gajender",name=name))
        
        else:
            return f"This is ordinary account detail.... Name:{name} and Password: {password}"



        # return f"This is name: {name} and this is password: {password}"

if __name__=="__main__":
    app.run(debug=True)
from flask import Flask, url_for,redirect

app=Flask(__name__)

@app.route("/admin")
def hello_admin():
    return f"Hello admin. this is the url for the admin"

@app.route("/guest/<guest_name>")
def hello_guest(guest_name):
    return f"Hello guest. this is guest page and your name is {guest_name}"

@app.route("/checking/<guest_name>")
def checking(name):
    if name=="admin":
        return redirect(url_for("/admin"))
    else:
        return redirect(url_for("/guest",name))
    




if __name__=="__main__":
    app.run(debug=True)
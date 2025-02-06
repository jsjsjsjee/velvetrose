from flask import Flask,render_template,request
app=Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/rooms')
def rooms():
    return render_template("rooms.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact',methods=['POST','GET'])
def contact():
    if request.method == "POST":
        return "<h1><center>Thank You For Your Submission!</center></h1>"
    return render_template("contact.html")

if __name__=="__main":
    app.run(debug=True)

from flask import *
import db,hashlib
app Flask(__name__)

@app.route("/")
def index():
return render_template("index.html")

#User Registration
@app.route("/create",methods=["POST", "GET"])
def create():
if request.method == "POST":
username = request.form["username"]
password = request.form["password"]
   
if  db.get_user_by_name(name) is None:# ゆーざー名が被ってなければ
db.add_user(username,password)
session["username"]=username
return render_template("index.html",username =session["username"])
    return render_template("create.html")

# Login
@app.route("/login",methods=["POST", "GET"])
def login():
    if request.method == "POST"
    username =request.form["username"]
    password = request.form["password"]
    hashed_pass = hashlib.sha256(password.encode('utf-8')).hexdigest()
    user = db.get_user_by_name(username)
true_pass = user[2]
if hashed_pass ==true pass:
session["username"] = username
    return render_template("login.html")

# Tweet
@app.route("/tweet",methods=["POST","GET"])
def tweet():
    if request.methods == "POST":
        text = request.form["text"]
        db.add.tweet(0,text)
tweets =db.gat_all_tweets()
        return render_template("timeline.html",tweets = tweets)
app.secret_key='fefefe'

if __name__ == "__main__":
app.run(debug=True)

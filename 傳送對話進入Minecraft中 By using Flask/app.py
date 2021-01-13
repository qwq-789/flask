from flask import Flask,render_template,request
from mcpi.minecraft import Minecraft


app = Flask(__name__)

mc = Minecraft.create()
name = "error"

@app.route("/", methods=['GET','POST'])
def home():
    if request.method == 'POST':
        igetpost = "<"+name+"> "
        igetpost += request.values.get("txt")
        mc.postToChat(igetpost)
        return igetpost
    return render_template("index.html")

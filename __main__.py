from flask import Flask,request,render_template,redirect,session
from oauth import Oauth

app=Flask(__name__)

@app.route("/join",methods=["get"])
async def join():
  return redirect(Oauth.discord_login_url)

@app.route("/logged",methods=["get"])
async def logged():
  return "Logged in"

@app.route("/",methods=["get"])
async def index():
  return "Site Under Development"

if(__name__==__main__):
  app.run(debug=True)

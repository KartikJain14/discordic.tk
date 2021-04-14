from flask import Flask,request,render_template,redirect,session
from oauth import Oauth

app=Flask(__name__)

@app.route("/join",methods=["get"])
async def join():
  return redirect(Oauth.discord_login_url)

@app.route("/logged",methods=["get"])
async def logged():
  code = requests.args.get("code")
  access_token = Oauth.get_access_token(code)
  user_json = Oauth.get_user_json(access_token)
  username = user_json.get("username")
  return username

@app.route("/",methods=["get"])
async def index():
  return "Site Under Development"

if(__name__==__main__):
  app.run(debug=True)

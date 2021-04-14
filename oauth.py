class Oauth(object):
  client_id = "831801290534551583"
  client_secret = "1c8a881dbc827cfbeb5ee38de81662cdd2a09cd91e855b0065962c2ec4f94555"
  scope = "identify%20guilds.join"
  redirect_uri = "https://discordic.tk/logged"
  discord_login_url = f"https://discord.com/api/oauth2/authorize?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code&scope={scope}"

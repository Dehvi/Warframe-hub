"""
This program takes data from API, parses it and shows it on the flask site.

"""
from flask import Flask, render_template
from getWarframeStatus import *

app = Flask(__name__)
app.config['SECRET_KEY'] = "SuperSecretKey123!"

# get the API data
earth = getCycle("earth")
cetus = getCycle("cetus")
vallis = getCycle("vallis")
cambion = getCycle("cambion")
fissures = getFissures()
sortie = getSortie()
sortie_boss_info = getMoreSortieInfo()

# Home page
@app.route("/")
def hub():
    return render_template("index.html", cambion=cambion,
            earth=earth, cetus=cetus, vallis=vallis,
            fissures=fissures, sortie=sortie,
            sortie_boss_info=sortie_boss_info)

if __name__ == "__main__":
    app.run()

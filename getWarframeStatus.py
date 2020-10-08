"""
This program gets the data from warframestat api
and parses the data for the
Warframe API: https://docs.warframestat.us/

API LINK: https://api.warframestat.us/pc
"""
from parseCambionCycle import parseCambionJson
import requests


# Gets the sortie boss info data
def getMoreSortieInfo():
    url = "https://api.warframestat.us/pc/sortie"
    r = requests.get(url)
    sortie_data = r.json()

    boss = sortie_data["boss"]
    eta = sortie_data["eta"]

    data = {
        "boss": boss,
        "eta": eta,
    }
    return data

# Gets the sortie data and parses the useful parts from it
def getSortie():
    url = "https://api.warframestat.us/pc/sortie"
    r = requests.get(url)
    sortie_data = r.json()

    sortie_d = []
    for sortie in sortie_data["variants"]:
        # Information of missions
        mission_type = sortie["missionType"]
        modifier = sortie["modifier"]
        modifier_desc = sortie["modifierDescription"]
        node = sortie["node"]

        data = {
                "mission_type": mission_type,
                "modifier": modifier,
                "node": node,
                }
        sortie_d.append(data)
    return sortie_d

# Gets the fissures data and parses it
def getFissures():
    url = "https://api.warframestat.us/pc/fissures"
    r = requests.get(url)
    fissure_data = r.json()

    fissure_l = []

    for data in fissure_data:
        node = data["node"]
        missionType = data["missionType"]
        tier = data["tier"]
        eta = data["eta"]
        enemy = data["enemy"]
        da = {
                "node": node,
                "missionType": missionType,
                "tier": tier,
                "eta": eta,
                "enemy": enemy,
             }
        fissure_l.append(da)

    return fissure_l

# Gets the time cycle data and takes the planet name as input [earth,cetus,cambion,vallis]
def getCycle(place="cambion"):
    url = f"https://api.warframestat.us/pc/{place}Cycle"
    r = requests.get(url)

    # check if place == "cambion" then parse it differently, else continue normally
    if place == "cambion":
        return parseCambionJson(r.json()) # cambion returns differently formatted json file than
    else:
        return r.json()

import json, requests


def GetPostData():
    with open('FormData.json') as f:
        x = json.load(f)

    return x

session = requests.session()
res = session.get("https://odyssey.tarrantcounty.com/PublicAccess/default.aspx")
res = session.post("https://odyssey.tarrantcounty.com/PublicAccess/Search.aspx?ID=900", data=GetPostData())

print(res.text)
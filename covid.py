import requests

a = requests.get("https://api.covid19india.org/data.json")
text = a.text
dict = eval(text)
state=dict["statewise"]

for i in state:
 print(i["state"])
 print("Confirmed: ",i["confirmed"])
 print("Active:    ",i["active"])
 print("Recovered: ",i["recovered"])
 print("Deaths:    ",i["deaths"])
 print("")
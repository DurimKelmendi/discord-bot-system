import http.client
import json

conn = http.client.HTTPSConnection("yahoo-finance15.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "bdafce06f6mshe7dfa1ad7a260b3p1f23b0jsn817950867139",
    'X-RapidAPI-Host': "yahoo-finance15.p.rapidapi.com"
    }

conn.request("GET", "/api/yahoo/qu/quote/AAPL/financial-data", headers=headers)

res = conn.getresponse()
data = res.read()

aapl = json.dumps(data.decode("utf-8"), indent=2)
#print()
import http.client
import json

conn = http.client.HTTPSConnection("yahoo-finance15.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "PRIVATE_KEY",
    'X-RapidAPI-Host': "PRIVATE_HOST"
    }

conn.request("GET", "/api/yahoo/qu/quote/AAPL/financial-data", headers=headers)

res = conn.getresponse()
data = res.read()

aapl = json.dumps(data.decode("utf-8"), indent=2)
#print()

"""
Want to make an HTTP call? Use requests.
See the docs here: http://docs.python-requests.org/en/master/
"""

import requests

def getFoods():
    resp = requests.get("http://localhost:5000/api/foods")
    print(resp.json())

def postFood(newFood):
    resp = requests.post("http://localhost:5000/api/foods", json=newFood)
    print("HTTP status code: {}, Response text: {}".format(resp.status_code, resp.text))

getFoods()
postFood({
    "name": input("Enter a food: ")
})
getFoods()
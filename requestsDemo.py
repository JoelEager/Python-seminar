"""
Want to make an HTTP call? Use requests.
See the docs here: http://docs.python-requests.org/en/master/

Note that these demo functions need a local instance of the flask demo server to talk to.
"""

import requests

def getFoods():
    resp = requests.get("http://localhost:5000/api/foods")
    print(resp.json())

def postFood(newFood):
    resp = requests.post("http://localhost:5000/api/foods", json=newFood)
    print("HTTP status code: {}, Response text: {}".format(resp.status_code, resp.text))

def main():
    getFoods()

    while True:
        postFood({
            "name": input("Enter a food: ")
        })
        getFoods()

if __name__ == "__main__":
    main()
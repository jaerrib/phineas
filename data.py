from random import choice

import requests


class Selector:

    def __init__(self):
        self.activity = ""
        self.participants = "1"
        self.price = "0.0"
        self.accessibility = "0.0"

    @staticmethod
    def get_rand_type():
        activity_types = [
            "education",
            "recreational",
            "social",
            "diy",
            "charity",
            "cooking",
            "relaxation",
            "music",
            "busywork",
        ]
        return choice(activity_types)

    @staticmethod
    def get_rand_activity():
        response = requests.get("http://www.boredapi.com/api/activity/")
        response.raise_for_status()
        data = response.json()
        return data["activity"]

    def get_suggestion(self, activity_type, participants, price, accessibility):

        parameters = {
            "type": activity_type,
            "participants": participants,
            "price": price,
            "minaccessibility": "0",
            "maxaccessibility": accessibility,
        }

        if activity_type == "random":
            parameters["type"].set = self.get_rand_type()
        response = requests.get(
            "http://www.boredapi.com/api/activity/", params=parameters
        )
        response.raise_for_status()
        data = response.json()
        if "error" in data:
            suggestion = "No suggestion found for the chosen parameters." "Try again."
        else:
            suggestion = data["activity"]
        return suggestion

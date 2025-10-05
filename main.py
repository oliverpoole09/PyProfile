import json
import settings.universal as univ
import gui

with open("data/account.json", "r") as f:
    accData = json.load(f)

if accData["loginToken"] == "":
    gui.main_page()
else:
    gui.account_page()
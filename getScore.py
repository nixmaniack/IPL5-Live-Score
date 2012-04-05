#!/usr/bin/env python

import requests
import json
import re

data = requests.get("http://data.iplt20.com/core/cricket/2012/ipl2012/ipl2012-01/scoring.js").content

json_data = re.sub(r'\);','',re.sub(r'onScoring\(','', data))

score = json.loads(json_data)

print score["matchInfo"]["teams"][0]["team"]["abbreviation"] + ":" + str(score["innings"][0]["scorecard"]["runs"]) + '/' + str(score["innings"][0]["scorecard"]["wkts"])
print score["matchInfo"]["teams"][1]["team"]["abbreviation"] + ":" + str(score["innings"][1]["scorecard"]["runs"]) + '/' + str(score["innings"][1]["scorecard"]["wkts"])

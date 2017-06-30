# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 19:47:29 2017

@author: Noah
"""

import requests
import json

fpl_data = requests.get('https://fantasy.premierleague.com/drf/bootstrap-static').json()
for i, player in enumerate(fpl_data['elements']):
    try:
        fpl_data['elements'][i]['history'] = requests.get('https://fantasy.premierleague.com/drf/element-summary/'
                                                             + str(player['id'])).json()
    except:
        fpl_data['elements'][i]['history'] = -1

                                                             
with open('fpl_data.json', 'w') as outfile:
    json.dump(fpl_data, outfile)
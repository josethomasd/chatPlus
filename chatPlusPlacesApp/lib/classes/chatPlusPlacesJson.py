import urllib.request
import sys
import json
import requests
from collections import defaultdict

from chatPlusPlacesApp.lib.classes import chatPlusConstants

constantsObject = chatPlusConstants.chatPlusConstants

class chatPlusPlacesJson:

    # the searchstring is stored searchString variable.
    searchString = ''
    def getJSON(self,searchString):
        url_input = searchString
        base_url=constantsObject.__BASEURL__
        details_url=constantsObject.__DETAILSURL__
        url_location=constantsObject.__BASELOCATION__
        url_radius=constantsObject.__BASERADIUS__
        url_key=constantsObject.__APIKEY__
        img_url=constantsObject.__IMAGEURL__
        url = base_url+url_input+url_location+url_radius+url_key
        urllib.request.urlretrieve(url, 'search.json')#reading place search json
        with open('search.json') as json_file:
                json_data = json.load(json_file)
                #place_id = json_data['predictions'][0]['place_id']
                placeJson = defaultdict(dict)
                dictLen = len(json_data['predictions'])
                for i in range(0,dictLen):
                    placeJson[i] = json_data['predictions'][i]['description']
        return placeJson
    def getJSONFinal(self,searchOption):
        print('WOrking')
        op = searchOption
        place_id = json_data['predictions'][op]['place_id']
        url1 = details_url+place_id+url_key
        urllib.request.urlretrieve(url1, 'details.json')#place details json
        with open('details.json') as json_file1:
                json_data1 = json.load(json_file1)
                finalJson = defaultdict(dict)
                try:
                    placeName=json_data1['result']['name']
                    finalJson['placeName'] = placeName
                except:
                    finalJson['placeName'] = 'N/A'
                try:
                    placeRating=json_data1['result']['rating']
                    finalJson['placeRating'] = placeRating
                except:
                    finalJson['placeRating'] = 'N/A'
                try:
                    placePhone=json_data1['result']['international_phone_number']
                    finalJson['placePhone'] = placePhone
                except:
                    finalJson['placePhone'] = 'N/A'

                try:
                    placeAddr=json_data1['result']['formatted_address']
                    finalJson['placeAddr'] = placeAddr
                except:
                    finalJson['placeAddr'] = 'N/A'
                try:
                    placeWeb=json_data1['result']['website']
                    finalJson['placeWeb'] = placeWeb
                except:
                    finalJson['placeWeb'] = 'N/A'
                try:
                    picture_id=json_data1['result']['photos'][0]['photo_reference']
                    placeImageURL = img_url+picture_id+url_key
                    finalJson['placeImageURL'] = placeImageURL

                except:
                    pass
        return finalJson

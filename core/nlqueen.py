# this is from preliminary testing of NatOS

import re, datetime, json, urllib2, urllib
from geotext import GeoText
import yweather

with open('core/khal.json', 'r') as f:
    khal = json.load(f)

def getWords(data):
    return re.compile(r"[\w']+").findall(data)

def jdump(element, value):
    with open('core/khal.json', 'r') as f:
        khal = json.load(f)
    khal[element] = value
    with open('core/khal.json', 'w') as f:
        json.dump(khal,f)

def get_weather(city, type):
    baseurl = "https://query.yahooapis.com/v1/public/yql?"
    yql_query = "select * from weather.forecast where woeid="+city
    yql_url = baseurl + urllib.urlencode({'q':yql_query}) + "&format=json"
    result = urllib2.urlopen(yql_url).read()
    data = json.loads(result)
    condition = data['query']['results']['channel']['item']['condition']['text']
    temperature = str(int((float(data['query']['results']['channel']['item']['forecast'][0]['high'])-32)/1.8))
    return 'The weather is ' + condition + ' reaching ' + temperature + ' degree celsius'

def intent(a):
    words = getWords(a)
    # --- update khal
    if a.lower().find('call me') != -1:
        jdump('name', a[a.lower().find('call me')+8:]) #plus 8 because len(call me) + 1
        return 'Okay, will call you ' + a[a.lower().find('call me')+8:]
    # --- "what's my name"
    if a.lower().find('my name') != -1:
        return 'I call you ' + khal['name']
    # --- find if user is asking for time
    time_text = ['time']
    for each in time_text:
        if each in words:
            now = datetime.datetime.now()
            res = 'It is ' + str(now.hour) + ' ' + str(now.minute)
            return res
    # --- weather data
    weather_text = ['weather']
    non_cap_weather = ['show', 'tell', 'what', 'is', 'the', 'weather', 'city', 'today',
                        'right', 'now']
    for each in weather_text:
        if each in words:
            potential = GeoText(' '.join([x for x in words if x not in non_cap_weather])).cities
            if potential != []:
                city = potential[0]
                client = yweather.Client()
                city = client.fetch_woeid(city)
            else:
                city = khal['city_id']
            return get_weather(city, 'simple')
    return a

def extract(a):
    res = intent(a)
    return res

#jdump('name', 'love')

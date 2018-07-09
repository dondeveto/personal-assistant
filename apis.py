import re
import urllib.request
import time
import pyttsx

location = "" 

def fetch_weather(location):
    location=location.capitalize()
    if location == "":
        exit
    else:
        try:   
            city = location.replace(" ", "-")
            url = "http://www.weather-forecast.com/locations/" + city + "/forecasts/latest"
            
            data = urllib.request.urlopen(url).read()
            data1 = data.decode("utf-8")
            m = re.search('span class="phrase">', data1)
            start = m.end()
            end = start + 300
            newString = data1[start:end]

            

            m = re.search("</span>", newString)
            end = m.start() - 2
            final = newString[0:end]
            
            engine = pyttsx.init()
            engine.say(final)
            engine.runAndWait()
            return final
            fetch_weather()
        except:
            return "The city doesn't exist"
            #time.sleep(2)
            fetch_weather()





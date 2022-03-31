# Author: Ezra Aguimatang <ezreag>
# Date: 03.31.2022

#Given the URL, this file parses raw HTML
#Prints desired surf conditions

import requests
from bs4 import BeautifulSoup
from URLgetter import * #chooseregion(), socalsurf()

chooseregion()

print("\n-----------------------------------\n")
print("\n\n\n\n\nLoading data...")
print("Do not type for accurate results...\n")
print("\n\n\n\n\n***********************************\n")

#GET request of url
url = urlobj.urllist[0] #url string
r = requests.get(url)

#creates: soup object = BeautifulSoup(raw HTML, HTML parser used)
#print(soup.prettify())
soup = BeautifulSoup(r.content, 'html.parser')

#print the location
locationstr = str(soup.find('h1', attrs={'class':'fcst-loc-name-label'}))
locationstr = locationstr[locationstr.find(">")+1:-5]
print("CURRENT Conditions For: ", locationstr,"\n")

print("***********************************\n")

def getcurrtemp():
    #prints current date's average temperature
    tempstr = str(soup.find('div', attrs={'class':'wx-icon-temp'}))
    if "°" in tempstr:
        startpos = tempstr.find(">") + 1
        endpos = tempstr.find("</") - 1
        print("Avg Temperature: ", tempstr[startpos:endpos], "\n")
    else:
        print("No temp forcast for today :(")

def getcurrwind():
    #prints current date's wind direction and avg wind speed
    windstr = str(soup.find('div', attrs={'class':'wx-icons-wind-desc'}))
    if "mph" in windstr:
        startpos = windstr.find(">") + 1
        endpos = windstr.find("<i") - 1
        print("Wind Direction:  ", windstr[startpos:endpos])

        windstr = windstr[endpos:len(windstr)]
        startpos = windstr.find("ht") + 8
        endpos = windstr.find("mph") + 3
        print("Avg Wind Speed:  ", windstr[startpos:endpos], "\n")
    else:
        print("No wind forcast for today :(")

def getbuoydata():
    #prints buoy number and data
    buoystr = str(soup.find('div', attrs={'class':'wx-icon-buoy-data'}))
    if "@" in buoystr:
        buoynamepos = buoystr.find("Buoy ")
        buoystr = buoystr[buoynamepos:len(buoystr)]
        endstr = buoystr.find("<")
        print("Buoy Name: ", buoystr[0:endstr])

        startpos = buoystr.find("<div>") + 5
        endpos = buoystr.find("sec") + 3
        print("Buoy Data: ", buoystr[startpos:endpos], "\n")
    else:
        print("No buoy data for today :(")

def gettidedata():
    #prints tide data
    tidestr = str(soup.find('div', attrs={'class':'wx-icon-tide-data'}))
    if ("LOW" or "HIGH") in tidestr:
        tidelist = tidestr.rsplit("\n")
        lowstr = tidelist[1]
        highstr = tidelist[2]
        print("LOW TIDE:  ", lowstr[lowstr.find(":")-2:-6])
        print("HIGH TIDE: ", highstr[highstr.find(":")-2:-6], "\n")
    else:
        print("No tide data for today :(")
    
def getwatertemp():
    #prints water temp data
    watertempstr = str(soup.find('div', attrs={'class':'wx-icon-water-data'}))
    if "°" in watertempstr:
        watertemplist = watertempstr.rsplit("\n")
        tempstr = watertemplist[1]
        suitstr = watertemplist[2]
        print("Avg Water Temp:   ", watertemplist[1][tempstr.find(">")+1:-6])
        print("Recommended Suit: ", watertemplist[2][suitstr.find(">")+1:-6], "\n")
    else:
        print("No water temp data for today :(")

def getwavecond():
    #prints wave height
    wavestr = str(soup.find('div', attrs={'class':'graph-data-wave-height'}))
    if "ft" in wavestr:
        waveheighpos = wavestr.find("ght") + 5
        waveheighstr = wavestr[waveheighpos:-6]
        print("Wave Height:    ", waveheighstr)
    else:
        print("No wave height data for today :(")

    #prints wave condition
    wavecondstr = str(soup.find('div', attrs={'class':'graph-data-wave-cond'}))
    wavecondstr = wavecondstr[wavecondstr.find(">")+1:-6]
    if wavecondstr == "CHOPPY" or wavecondstr == "FAIR" or wavecondstr == "CLEAN":
        print("Wave Condition: ", wavecondstr, "\n")
    else:
        print("No wave condition data for today :(")


getcurrtemp() 
getcurrwind() 
getbuoydata() 
gettidedata() 
getwatertemp() 
getwavecond() 

print("***********************************\n")
print("Thanks for using PumpinSwellNotifs :)\n")
print("***********************************\n")

""""""""""""

#first draft of getcurrtemp
''''
def getcurrtemp():
    degreessymb = "°"
    for i in range(0, len(tempstr)):
        if tempstr[i] == degreessymb:
            print("Avg Temperature Today: ",tempstr[i-2:i+1])
        elif i == len(tempstr):
            print("No temp forcast for today :(")
'''
#first draft of getcurrwind
'''
f = ">"
windstr = str(soup.find('div', attrs={'class':'wx-icons-wind-desc'}))
for i in range(0, len(windstr)):
    if windstr[i] == f:
        print("Wind Direction Today:  ", windstr[i+1:i+4])
        newwindstr = windstr[i+5:len(windstr)]
        mphpos = newwindstr.find("mph")
        firstmph = newwindstr[mphpos-2]
        if firstmph == "1" or firstmph == "2"\
            or firstmph == "3" or firstmph == "4"\
                or firstmph == "5" or firstmph == "6"\
                    or firstmph == "7" or firstmph == "8"\
                        or firstmph == "9":
            print("Avg Wind Speed Today:  ", newwindstr[mphpos-2:mphpos+3])
        else:
            print("Avg Wind Speed Today:  ", newwindstr[mphpos-1:mphpos+3])
        break
    elif i == len(windstr):
        print("No wind forcast for today :(")
'''
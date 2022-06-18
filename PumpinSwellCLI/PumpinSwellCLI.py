# Author: Ezra Aguimatang <ezreag>
# Date: 04.03.2022

#Creates a Command Line Interface (CLI) using argparse

import os
import requests
from bs4 import BeautifulSoup
import argparse
from ParseHTML import *

class URLgetter:
    def __init__(self):
        self.url = [None]
        self.southerncalifornia = \
        ["https://www.swellinfo.com/surf-forecast/santa-barbara-california",
        "https://www.swellinfo.com/surf-forecast/ventura-california",
        "https://www.swellinfo.com/surf-forecast/los-angeles-california-north",
        "https://www.swellinfo.com/surf-forecast/los-angeles-california-south",
        "https://www.swellinfo.com/surf-forecast/orange-county-california-north",
        "https://www.swellinfo.com/surf-forecast/orange-county-california-south",
        "https://www.swellinfo.com/surf-forecast/san-diego-california-north",
        "https://www.swellinfo.com/surf-forecast/san-diego-california-south"]
        self.northerncalifornia = \
        ["https://www.swellinfo.com/surf-forecast/crescent-city-california",
        "https://www.swellinfo.com/surf-forecast/eureka-california",
        "https://www.swellinfo.com/surf-forecast/fort-bragg-california",
        "https://www.swellinfo.com/surf-forecast/sea-ranch-california",
        "https://www.swellinfo.com/surf-forecast/sonoma-county-california",
        "https://www.swellinfo.com/surf-forecast/marin-county-california",
        "https://www.swellinfo.com/surf-forecast/ocean-beach-california",
        "https://www.swellinfo.com/surf-forecast/half-moon-bay-california",
        "https://www.swellinfo.com/surf-forecast/pescadero-california",
        "https://www.swellinfo.com/surf-forecast/davenport-california",
        "https://www.swellinfo.com/surf-forecast/santa-cruz-california",
        "https://www.swellinfo.com/surf-forecast/moss-landing-california",
        "https://www.swellinfo.com/surf-forecast/monterey-california",
        "https://www.swellinfo.com/surf-forecast/big-sur-california",
        "https://www.swellinfo.com/surf-forecast/san-simeon-california",
        "https://www.swellinfo.com/surf-forecast/morro-bay-california",
        "https://www.swellinfo.com/surf-forecast/pismo-beach-california"]
        self.hawaii = \
        ["https://www.swellinfo.com/surf-forecast/north-shore-oahu-hawaii",
        "https://www.swellinfo.com/surf-forecast/south-shore-oahu-hawaii",
        "https://www.swellinfo.com/surf-forecast/sandy-beach-oahu-hawaii",
        "https://www.swellinfo.com/surf-forecast/ewa-beach-oahu-hawaii",
        "https://www.swellinfo.com/surf-forecast/east-oahu-hawaii",
        "https://www.swellinfo.com/surf-forecast/west-oahu-hawaii",
        "https://www.swellinfo.com/surf-forecast/hookipa-maui",
        "https://www.swellinfo.com/surf-forecast/waiehu-maui",
        "https://www.swellinfo.com/surf-forecast/honolua-maui",
        "https://www.swellinfo.com/surf-forecast/lahaina-maui",
        "https://www.swellinfo.com/surf-forecast/kehei-maui",
        "https://www.swellinfo.com/surf-forecast/makena-maui",
        "https://www.swellinfo.com/surf-forecast/hana-maui",
        "https://www.swellinfo.com/surf-forecast/northeast-hawaii",
        "https://www.swellinfo.com/surf-forecast/northwest-hawaii",
        "https://www.swellinfo.com/surf-forecast/west-hawaii",
        "https://www.swellinfo.com/surf-forecast/southeast-hawaii"]
        self.bajamexico = \
        ["https://www.swellinfo.com/surf-forecast/ensenada-mexico",
        "https://www.swellinfo.com/surf-forecast/san-quintin-mexico",
        "https://www.swellinfo.com/surf-forecast/seven-sisters-mexico",
        "https://www.swellinfo.com/surf-forecast/punta-abreojos-mexico",
        "https://www.swellinfo.com/surf-forecast/scorpion-bay-mexico",
        "https://www.swellinfo.com/surf-forecast/cabo-mexico"]

    def parseURL(self,url):
        #GET request of url
        r = requests.get(url)
        #creates: soup object = BeautifulSoup(raw HTML, HTML parser used)
        soup = BeautifulSoup(r.content, 'html.parser')

        #print the location
        locationstr = str(soup.find('h1', attrs={'class':'fcst-loc-name-label'}))
        locationstr = locationstr[locationstr.find(">")+1:-5]
        
        clear()

        print("************************************************\n")
        print("\033[1mCURRENT\033[0m Conditions For: ", "\033[1;33m", locationstr, "\033[0m""\n")
        print("************************************************\n")

        getswelldata = parsingInfo(soup)
        getswelldata.getcurrtemp() 
        getswelldata.getcurrwind() 
        getswelldata.getbuoydata() 
        getswelldata.gettidedata() 
        getswelldata.getwatertemp() 
        getswelldata.getwavecond() 

        print("\033[5m************************************************")
        print("*                                              *")
        print("*    \033[0mThanks for using PumpinSwellNotifs :)\033[5m     *")
        print("*                                              *")
        print("************************************************\n\033[0m")

    def chooselocation(self, region, location): #add a parameter that intakes input
        #request user input to choose a region 
        if region == 1 and location in range(1,9):
            clear()
            loadingmessage()
            self.socalsurf(location)
        elif region == 2 and location in range(1,18):
            clear()
            loadingmessage()
            self.norcalsurf(location)
        elif region == 3 and location in range(1,18):
            clear()
            loadingmessage()
            self.hawaiisurf(location)
        elif region == 4 and location in range(1,7):
            clear()
            loadingmessage()
            self.bajamexicosurf(location)
        else:
            clear()
            print("\033[91m\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("!                                              !")
            print("!        \033[0mERROR: INVALID REGION OR LOCATION\033[91m     !")
            print("!                   \033[0mTRY AGAIN\033[91m                  !")
            print("!                                              !")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\033[0m")
            exit()

    def socalsurf(self, location):
        if location in range(1,9):
            self.url[0] = self.southerncalifornia[location - 1]
            self.parseURL(self.url[0])

    def norcalsurf(self, location):
        if location in range(1,18):
            self.url[0] = self.northerncalifornia[location - 1]
            self.parseURL(self.url[0])

    def hawaiisurf(self, location):
        if location in range(1,18):
            self.url[0] = self.hawaii[location - 1]
            self.parseURL(self.url[0])

    def bajamexicosurf(self, location):
        if location in range(1,7):
            self.url[0] = self.bajamexico[location - 1]
            self.parseURL(self.url[0])

def clear():
     os.system('cls' if os.name=='nt' else 'clear')
     return("   ")

def loadingmessage():
    print("\033[92m\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n------------------------------------------------\n\033[0m")
    print("\n\n\n\n\n               Loading data\033[5m...\033[0m")
    print("      Do not type for accurate results\033[5m...\033[0m\n")
    print("\033[92m\n\n\n\n\n------------------------------------------------\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\033[0m")
    
def RegionList():
    clear()
    print("\n\n\n         Regions with Available Data:\n\n")
    print("------------------------------------------------\n\n")
    print("                  1: Socal")
    print("                  2: Norcal")
    print("                  3: Hawaii")
    print("                  4: Baja Mexico\n\n")
    print("------------------------------------------------\n\n\n")
    exit()

def LocationList(location):
    if location == 1:
        clear()
        print("\n\n\n      SoCal Counties with Available Data:\n\n")
        print("------------------------------------------------\n\n")
        print("          1: Santa Barbara, CA")
        print("          2: Ventura, CA")
        print("          3: Northern Los Angeles, CA")
        print("          4: Southern Los Angeles, CA")
        print("          5: Northern Orange County, CA")
        print("          6: Southern Orange County, CA")
        print("          7: Northern San Diego, CA")
        print("          8: Southern San Diego, CA\n\n")
        print("------------------------------------------------\n\n\n")
        exit()
    elif location == 2:
        clear()
        print("\n\n\n     NorCal Counties with Available Data:\n\n")
        print("------------------------------------------------\n\n")
        print("          1: Crescent City, CA")
        print("          2: Eureka, CA")
        print("          3: Fort Bragg, CA")
        print("          4: Sea Ranch, CA")
        print("          5: Sonoma County, CA")
        print("          6: Marin County, CA")
        print("          7: Ocean Beach, CA")
        print("          8: Half Moon Bay, CA")
        print("          9: Pescadero, CA")
        print("          10: Davenport, CA")
        print("          11: Santa Cruz, CA")
        print("          12: Moss Landing, CA")
        print("          13: Monterey, CA")
        print("          14: Big Sur, CA")
        print("          15: San Simeon, CA")
        print("          16: Morro Bay, CA")
        print("          17: Pismo Beach, CA\n\n")
        print("------------------------------------------------\n\n\n")
        exit()
    elif location == 3:
        clear()
        print("\n\n\n     Hawaiian Islands with Available Data:\n\n")
        print("------------------------------------------------\n\n")
        print("          1: North Shore Oahu, HI")
        print("          2: Honolulu, HI")
        print("          3: Sandy Beach Oahu, HI")
        print("          4: Ewa Beach Oahu, HI")
        print("          5: East (Hauula) Oahu, HI")
        print("          6: West Shore Oahu, HI")
        print("          7: Hookipa Maui, HI")
        print("          8: Waiehu Maui, HI")
        print("          9: Honolua Maui, HI")
        print("          10: Lahaina Maui, HI")
        print("          11: Kihei Maui, HI")
        print("          12: Makena Maui, HI")
        print("          13: Hana Maui, HI")
        print("          14: Northeast Hawaii, HI")
        print("          15: Northwest Hawaii, HI")
        print("          16: West Hawaii, HI")
        print("          17: Southeast Hawaii, HI\n\n")
        print("------------------------------------------------\n\n\n")
        exit()
    elif location == 4:
        clear()
        print("\n\n\n      Baja Mexico Breaks with Available Data:\n\n")
        print("------------------------------------------------\n\n")
        print("          1: Ensenada, MX")
        print("          2: San Quintin, MX")
        print("          3: Seven Sisters, MX")
        print("          4: Punta Abreojos, MX")
        print("          5: Scorpion Bay, MX")
        print("          6: Cabo, MX\n\n")
        print("------------------------------------------------\n\n\n")
        exit()
    else:
        clear()
        print("\033[91m\n\n\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("!                                              !")
        print("!          ERROR: INVALID LOCATION NUM         !")
        print("!                   TRY AGAIN                  !")
        print("!                                              !")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\n\n\033[0m")
        exit()


def main():
    clear()
    print("\n")
    parser = argparse.ArgumentParser(
        prog = "PumpinSwell",
        usage = "%(prog)s [-h] [-RegionList SHOW] [-LocationList RegionNum] [-SwellInfo RegionNum LocationNum]",
        description = "INTRO: A program called PumpinSwell \
            that accesses current surf and weather forcasts of your \
            favorite locations",
        epilog = "Thanks for using PumpinSwell :)")

    parser.add_argument("-RegionList",
        metavar = "SHOW",
        type = str,
        help = "Type 'python3 CLI.py -RegionList SHOW' to see the list of Regions")

    parser.add_argument("-LocationList",
        metavar = "RegionNum",
        nargs = 1,
        type = int,
        help = "With your corresponding RegionNum (1-3) in mind, type 'python3 CLI.py -LocationList RegionNum' to see the list of Locations")

    parser.add_argument("-SwellInfo",
        metavar = ("RegionNum", "LocationNum"),
        nargs = 2,
        type = int,
        help = "Enter the number for corresponding Region and Location")
    
    args = parser.parse_args()

    if args.RegionList != None:
        RegionList()
    elif args.LocationList != None:
        RegionNumList = []
        for i in args.LocationList:
            RegionNumList.append(i)
        LocationList(RegionNumList[0])
    elif args.SwellInfo != None:
        SwellInfoList = []
        for i in args.SwellInfo:
            SwellInfoList.append(i)
        urlgetter = URLgetter()
        urlgetter.chooselocation(SwellInfoList[0], SwellInfoList[1])
    else:
        clear()
        parser.print_help()
        exit()

if __name__ == "__main__":
    #calling the main function
    main()
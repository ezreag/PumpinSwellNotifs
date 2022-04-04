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
        print("CURRENT Conditions For: ", locationstr,"\n")
        print("************************************************\n")

        getswelldata = parsingInfo(soup)
        getswelldata.getcurrtemp() 
        getswelldata.getcurrwind() 
        getswelldata.getbuoydata() 
        getswelldata.gettidedata() 
        getswelldata.getwatertemp() 
        getswelldata.getwavecond() 

        print("************************************************")
        print("*                                              *")
        print("*    Thanks for using PumpinSwellNotifs :)     *")
        print("*                                              *")
        print("************************************************\n")

    def chooselocation(self, region, location): #add a parameter that intakes input
        #request user input to choose a region 
        if region == 1 and location in range(1,9):
            clear()
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n------------------------------------------------\n")
            print("\n\n\n\n\nLoading data...")
            print("Do not type for accurate results...\n")
            print("\n\n\n\n\n------------------------------------------------\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            self.socalsurf(location)
        elif region == 2 and location in range(1,18):
            clear()
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n------------------------------------------------\n")
            print("\n\n\n\n\nLoading data...")
            print("Do not type for accurate results...\n")
            print("\n\n\n\n\n------------------------------------------------\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            self.norcalsurf(location)
        elif region == 3 and location in range(1,18):
            clear()
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n------------------------------------------------\n")
            print("\n\n\n\n\nLoading data...")
            print("Do not type for accurate results...\n")
            print("\n\n\n\n\n------------------------------------------------\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            self.hawaiisurf(location)
        else:
            print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("!                                              !")
            print("!        ERROR: INVALID REGION OR LOCATION     !")
            print("!                   TRY AGAIN                  !")
            print("!                                              !")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
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

def clear():
     os.system('cls' if os.name=='nt' else 'clear')
     return("   ")

def RegionList():
    clear()
    print("\n         Regions with Available Data:\n")
    print("------------------------------------------------\n")
    print("                  1: Socal")
    print("                  2: Norcal")
    print("                  3: Hawaii\n")
    print("------------------------------------------------\n")
    exit()

def LocationList(location):
    if location == 1:
        clear()
        print("\n\n\n\n\n      SoCal Counties with Available Data:\n")
        print("------------------------------------------------\n")
        print("          1: Santa Barbara, CA")
        print("          2: Ventura, CA")
        print("          3: Northern Los Angeles, CA")
        print("          4: Southern Los Angeles, CA")
        print("          5: Northern Orange County, CA")
        print("          6: Southern Orange County, CA")
        print("          7: Northern San Diego, CA")
        print("          8: Southern San Diego, CA\n")
        print("------------------------------------------------\n")
        exit()
    elif location == 2:
        clear()
        print("\n\n\n\n\n     NorCal Counties with Available Data:\n")
        print("------------------------------------------------\n")
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
        print("          17: Pismo Beach, CA\n")
        print("------------------------------------------------\n")
        exit()
    elif location == 3:
        clear()
        print("\n\n\n\n\n     Hawaiian Islands with Available Data:\n")
        print("------------------------------------------------\n")
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
        print("          17: Southeast Hawaii, HI\n")
        print("------------------------------------------------\n")
        exit()

def main():
    parser = argparse.ArgumentParser(
        prog = "PumpinSwell",
        usage = "%(prog)s [-h] [-RegionList] [-LocationList] [-RegionNum] [-LocationNum]",
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
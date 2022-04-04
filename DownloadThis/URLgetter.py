# Author: Ezra Aguimatang <ezreag>
# Date: 03.31.2022

#gets the URL for the location desired by the user

#Main Page Choose Region in US
#https://www.swellinfo.com/surf-forecast

class URLobj:
    def __init__(self):
        self.urllist = []

urlobj = URLobj()

def socalsurf():
    southerncalifornia = \
    ["https://www.swellinfo.com/surf-forecast/santa-barbara-california",
    "https://www.swellinfo.com/surf-forecast/ventura-california",
    "https://www.swellinfo.com/surf-forecast/los-angeles-california-north",
    "https://www.swellinfo.com/surf-forecast/los-angeles-california-south",
    "https://www.swellinfo.com/surf-forecast/orange-county-california-north",
    "https://www.swellinfo.com/surf-forecast/orange-county-california-south",
    "https://www.swellinfo.com/surf-forecast/san-diego-california-north",
    "https://www.swellinfo.com/surf-forecast/san-diego-california-south"]

    print("\n\n\n\n\n             Choose a SoCal County:\n")
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

    print("Type the number that corresponds to the correct county and press ENTER:", end = " ")
    num = int(input())

    if num not in range(1,9):
        print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("!                                              !")
        print("!             ERROR: INVALID COUNTY            !")
        print("!                   TRY AGAIN                  !")
        print("!                                              !")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
        socalsurf()
    elif num in range(1,9):
        url = southerncalifornia[num - 1]
        urlobj.urllist.append(url)

def norcalsurf():
    northerncalifornia = \
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

    print("\n\n\n\n\n             Choose a NorCal County:\n")
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

    print("Type the number that corresponds to the correct county and press ENTER:", end = " ")
    num = int(input())

    if num not in range(1,18):
        print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("!                                              !")
        print("!             ERROR: INVALID COUNTY            !")
        print("!                   TRY AGAIN                  !")
        print("!                                              !")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
        norcalsurf()
    elif num in range(1,18):
        url = northerncalifornia[num - 1]
        urlobj.urllist.append(url)

def hawaiisurf():
    hawaii = \
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

    print("\n\n\n\n\n       Choose a Hawaiian Island Location:\n")
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

    print("Type the number that corresponds to the correct county and press ENTER:", end = " ")
    num = int(input())

    if num not in range(1,18):
        print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("!                                              !")
        print("!             ERROR: INVALID COUNTY            !")
        print("!                   TRY AGAIN                  !")
        print("!                                              !")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
        hawaiisurf()
    elif num in range(1,18):
        url = hawaii[num - 1]
        urlobj.urllist.append(url)

def chooseregion(): #add a parameter that intakes input
    #request user input to choose a region   
    print("\n\n\n\n\n\n               Choose a region:\n")
    print("------------------------------------------------\n")
    print("                  1: Socal")
    print("                  2: Norcal")
    print("                  3: Hawaii\n")
    print("------------------------------------------------\n")
    print("Type the number that corresponds to the correct region and press ENTER:", end = " ")
    region = int(input())
    print("\n")

    if region == 1:
        socalsurf()
    elif region == 2:
        norcalsurf()
    elif region == 3:
        hawaiisurf()
    else:
        print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("!                                              !")
        print("!             ERROR: INVALID REGION            !")
        print("!                   TRY AGAIN                  !")
        print("!                                              !")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
        chooseregion(region)
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

    if num == 1:
        url = southerncalifornia[0]
    elif num == 2:
        url = southerncalifornia[1]
    elif num == 3:
        url = southerncalifornia[2]
    elif num == 4:
        url = southerncalifornia[3]
    elif num == 5:
        url = southerncalifornia[4]
    elif num == 6:
        url = southerncalifornia[5]
    elif num == 7:
        url = southerncalifornia[6]
    elif num == 8:
        url = southerncalifornia[7]
    if num == 1 or num == 2 or num == 3 or num == 4 or num == 5 or num == 6 or num == 7 or num == 8:
        urlobj.urllist.append(url)
    else:
        print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("!                                              !")
        print("!             ERROR: INVALID COUNTY            !")
        print("!                   TRY AGAIN                  !")
        print("!                                              !")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
        socalsurf()

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
    print("          !: Davenport, CA")
    print("          @: Santa Cruz, CA")
    print("          #: Moss Landing, CA")
    print("          $: Monterey, CA")
    print("          %: Big Sur, CA")
    print("          ^: San Simeon, CA")
    print("          &: Morro Bay, CA")
    print("          *: Pismo Beach, CA\n")

    print("------------------------------------------------\n")

    print("Type the number that corresponds to the correct county and press ENTER:", end = " ")
    num = str(input())

    if num == "1":
        url = northerncalifornia[0]
    elif num == "2":
        url = northerncalifornia[1]
    elif num == "3":
        url = northerncalifornia[2]
    elif num == "4":
        url = northerncalifornia[3]
    elif num == "5":
        url = northerncalifornia[4]
    elif num == "6":
        url = northerncalifornia[5]
    elif num == "7":
        url = northerncalifornia[6]
    elif num == "8":
        url = northerncalifornia[7]
    elif num == "9":
        url = northerncalifornia[8]
    elif num == "!":
        url = northerncalifornia[9]
    elif num == "@":
        url = northerncalifornia[10]
    elif num == "#":
        url = northerncalifornia[11]
    elif num == "$":
        url = northerncalifornia[12]
    elif num == "%":
        url = northerncalifornia[13]
    elif num == "^":
        url = northerncalifornia[14]
    elif num == "&":
        url = northerncalifornia[15]
    elif num == "*":
        url = northerncalifornia[16]
    if num == "1" or num == "2" or num == "3" or num == "4" or num == "5" or num == "6" or num == "7" or num == "8" or num == "9" or\
        num == "!" or num == "@" or num == "#" or num == "$" or num == "%" or num == "^" or num == "&" or num == "*":
        urlobj.urllist.append(url)
    else:
        print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("!                                              !")
        print("!             ERROR: INVALID COUNTY            !")
        print("!                   TRY AGAIN                  !")
        print("!                                              !")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
        norcalsurf()

def chooseregion():
    #request user input to choose a region   
    print("\n\n\n\n\n\n         Choose a region of California:\n")
    print("------------------------------------------------\n")
    print("                  1: Socal")
    print("                  2: Norcal\n")
    print("------------------------------------------------\n")
    print("Type the number that corresponds to the correct region and press ENTER:", end = " ")
    
    region = int(input())
    print("\n")
    if region == 1:
        socalsurf()
    elif region == 2:
        norcalsurf()
    else:
        print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("!                                              !")
        print("!             ERROR: INVALID REGION            !")
        print("!                   TRY AGAIN                  !")
        print("!                                              !")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
        chooseregion()
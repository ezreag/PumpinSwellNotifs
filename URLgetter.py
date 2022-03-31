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

    print("-----------------------------------\n")
    print("SoCal Counties:\n")

    print("1: Santa Barbara, CA")
    print("2: Ventura, CA")
    print("3: Northern Los Angeles, CA")
    print("4: Southern Los Angeles, CA")
    print("5: Northern Orange County, CA")
    print("6: Southern Orange County, CA")
    print("7: Northern San Diego, CA")
    print("8: Southern San Diego, CA\n")

    print("-----------------------------------\n")

    print("Type the number that corresponds to the correct county and press ENTER:", end = " ")
    num = int(input())

    if num == 1:
        url = southerncalifornia[0]
        urlobj.urllist.append(url)
    elif num == 2:
        url = southerncalifornia[1]
        urlobj.urllist.append(url)
    elif num == 3:
        url = southerncalifornia[2]
        urlobj.urllist.append(url)
    elif num == 4:
        url = southerncalifornia[3]
        urlobj.urllist.append(url)
    elif num == 5:
        url = southerncalifornia[4]
        urlobj.urllist.append(url)
    elif num == 6:
        url = southerncalifornia[5]
        urlobj.urllist.append(url)
    elif num == 7:
        url = southerncalifornia[6]
        urlobj.urllist.append(url)
    elif num == 8:
        url = southerncalifornia[7]
        urlobj.urllist.append(url)
    else:
        print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
        print("ERROR: INVALID COUNTY")
        print("TRY AGAIN")
        print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
        socalsurf()

def chooseregion():
    #request user input to choose a region   
    print("\nChoose a region of California:\n")
    print("-----------------------------------\n")
    print("1: Socal")
    print("2: Norcal\n")
    print("-----------------------------------\n")
    print("Type the number that corresponds to the correct region and press ENTER:", end = " ")
    
    region = int(input())
    if region == 1:
        socalsurf()
    elif region == 2:
        print("meh not done yet")
    else:
        print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
        print("ERROR: INVALID REGION")
        print("TRY AGAIN")
        print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
        chooseregion()
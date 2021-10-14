import urllib.parse
import requests
import colorama
from colorama import Fore, Style, Back
main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "2QwbAL478H3EPnGIPwGVrnrCpnbUiFNk"    # own key used
while True:
    name = input(Fore.MAGENTA + Back.BLACK + "Hi! What's your name? : ")
    print (Fore.BLUE + "Hi " + name +"!")
    orig = input (Fore.GREEN + name + "! Where are you from? :")
    if orig == "quit" or orig == "q":
        break
    dest = input(Fore.YELLOW + name + "! Where will you go? :")
    if dest == "quit" or dest == "q":
        break
    url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})
    print (Fore.WHITE + "URL ", (url))
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]
    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.")
        print(Fore.RED + "=============================================")
        print(Fore.LIGHTGREEN_EX +"Directions from " + (orig) + " to " + (dest))
        print("Trip Duration: " + (json_data["route"]["formattedTime"]))
        print("Distance: " + str("{:.2f}".format(json_data["route"]["distance"] * 1.6 ))+ " Km")
        print("Fuel Used: " + str("{:.3f}".format(json_data["route"]["fuelUsed"]*3.78))+ "L")
        print(Fore.RED + "=============================================")
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((Fore.LIGHTYELLOW_EX + "-" + each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
        print(Fore.RED + "=============================================\n")
    elif json_status == 402:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Invalid user inputs for one or bothlocations.")
        print("**********************************************\n")
    elif json_status == 611:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Missing an entry for one or bothlocations.")
        print("**********************************************\n")
    else:
        print("************************************************************************")
        print("For Staus Code: " + str(json_status) + "; Refer to:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("************************************************************************\n")
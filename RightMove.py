from bs4 import BeautifulSoup
import requests
import time

tempurl = "https://www.rightmove.co.uk/property-for-sale/find.html?locationIdentifier=REGION%5E1460&" \
      f"&index=24&" \
      "maxBedrooms=3&" \
      "minBedrooms=2&" \
      "maxPrice=325000&" \
      "radius=10.0&" \
      "propertyTypes=detached%2Csemi-detached%2Cterraced&primaryDisplayPropertyType=houses" \
      "&includeSSTC=false&mustHave=&dontShow=&furnishTypes=&keywords="


default_input = input("Default? y/n : ")
global pagereq
if default_input == "y":
      default = "https://www.rightmove.co.uk/property-for-sale/find.html?locationIdentifier=REGION%5E1460&&index=24&maxBedrooms=3&minBedrooms=2&maxPrice=450000&radius=5&propertyTypes=detached%2Csemi-detached%2Cterraced&primaryDisplayPropertyType=houses&includeSSTC=false&mustHave=&dontShow=&furnishTypes=&keywords="
      print("LinkLog : " + default)
      time.sleep(1)
      pagereq = requests.get(default)
      print(pagereq)

elif default_input == "n":
      minBedrooms = int(input('Minimum Bedrooms : '))
      maxBedrooms = int(input("Maximum Bedrooms : "))
      maxPrice = int(input("Maximuim Price : "))

      radius_reqr = [0 - 5 - 10 - 15 - 20 - 30 - 40]

      radius = int(input("Radius (Options : [0 - 5 - 10 - 15 - 20 - 30 - 40]) : "))

      url = "https://www.rightmove.co.uk/property-for-sale/find.html?locationIdentifier=REGION%5E1460&" \
            f"&index=24&" \
            f"maxBedrooms={maxBedrooms}&" \
            f"minBedrooms={minBedrooms}&" \
            f"maxPrice={maxPrice}&" \
            f"radius={radius}&" \
            "propertyTypes=detached%2Csemi-detached%2Cterraced&primaryDisplayPropertyType=houses" \
            "&includeSSTC=false&mustHave=&dontShow=&furnishTypes=&keywords="

      print("LinkLog : " + url)
      time.sleep(1)
      pagereq = requests.get(url)
      print(pagereq)

soup = BeautifulSoup(pagereq.content, "html.parser")

lists1 = soup.find_all("div", class_="propertyCard-wrapper")

for list in lists1:
      addresses = [address['content'] for address in list.findAll('meta', {'itemprop': 'streetAddress'})]
      property_type_demo = str(list.find("h2", class_="propertyCard-title"))
      property_type = property_type_demo.replace("end of terrace", "end-of-terrace")
      property_type = property_type.split(" ")[-14: -10]
      price = [price.text.strip() for price in list.findAll('div', {'class': 'propertyCard-priceValue'})]
      dates = [date.text.split(' ')[-1] for date in
               list.findAll('span', {'class': 'propertyCard-branchSummary-addedOrReduced'})]
      image = [image['src'] for image in list.findAll('img', {'itemprop': 'image'})]
      link = 1
      info = str([property_type, addresses, price, dates])
      print(info)
      with open("log.txt", "a") as pf:
            pf.write(info)

import requests
from bs4 import BeautifulSoup

class RightmoveScraper:
    results = []

    def fetch(self, url):
        print('HTTP GET request to URL: %s' % url, end='')
        response = requests.get(url)
        print(' | Status code: %s' % response.status_code)

        return response

    def parse(self, html):
        content = BeautifulSoup(html, 'lxml')

        titles = [title.text.strip() for title in content.findAll('h2', {'class': 'propertyCard-title'})]
        addresses = [address['content'] for address in content.findAll('meta', {'itemprop': 'streetAddress'})]
        descriptions = [description.text for description in
                        content.findAll('span', {'data-test': 'property-description'})]
        prices = [price.text.strip() for price in content.findAll('div', {'class': 'propertyCard-priceValue'})]
        dates = [date.text.split(' ')[-1] for date in
                 content.findAll('span', {'class': 'propertyCard-branchSummary-addedOrReduced'})]
        sellers = [seller.text.split('by')[-1].strip() for seller in
                   content.findAll('span', {'class': 'propertyCard-branchSummary-branchName'})]
        images = [image['src'] for image in content.findAll('img', {'itemprop': 'image'})]

        for index in range(0, len(titles)):
            self.results.append({
                'title': titles[index],
                'address': addresses[index],
                'description': descriptions[index],
                'price': prices[index],
                'date': dates[index],
                'seller': sellers[index],
                'image': images[index],
            })
            print(self.results)

default_input = input("Default? y/n : ")
if default_input == "y":
    default = "https://www.rightmove.co.uk/property-for-sale/find.html?locationIdentifier=REGION%5E1460&&index=24&maxBedrooms=3&minBedrooms=2&maxPrice=450000&radius=5&propertyTypes=detached%2Csemi-detached%2Cterraced&primaryDisplayPropertyType=houses&includeSSTC=false&mustHave=&dontShow=&furnishTypes=&keywords="
    def run(self):
        for page in range(0, 5):
            index = page * 24
            default = url1 + str(index) + url2
            response = self.fetch()
            self.parse(response.text)
        print(self.results)

    if __name__ == '__main__':
        scraper = RightmoveScraper()
        RightmoveScraper.run = run

elif default_input == "n":
    minBedrooms = int(input('Minimum Bedrooms : '))
    maxBedrooms = int(input("Maximum Bedrooms : "))
    maxPrice = int(input("Maximuim Price : "))
    radius_reqr = [0 - 5 - 10 - 15 - 20 - 30 - 40]
    radius = int(input("Radius (Options : [0 - 5 - 10 - 15 - 20 - 30 - 40]) : "))

    url1 = "https://www.rightmove.co.uk/property-for-sale/find.html?locationIdentifier=REGION%5E1460&" \
            f"&index="
    url2 = \
            f"&maxBedrooms={maxBedrooms}&" \
            f"minBedrooms={minBedrooms}&" \
            f"maxPrice={maxPrice}&" \
            f"radius={radius}&" \
            "propertyTypes=detached%2Csemi-detached%2Cterraced&primaryDisplayPropertyType=houses" \
            "&includeSSTC=false&mustHave=&dontShow=&furnishTypes=&keywords="

def run(self):
    for page in range(0, 5):
        index = page * 24
        url = (url1 + str(index) + url2)
        response = self.fetch(url)
        self.parse(response.text)


if __name__ == '__main__':
    scraper = RightmoveScraper()
    RightmoveScraper.run = run


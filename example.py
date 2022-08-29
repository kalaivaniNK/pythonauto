
import requests
from bs4 import BeautifulSoup

class suman:
    url = "https://www.flipkart.com/search?q=laptop&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
    data=requests.get(url)

    soup = BeautifulSoup(data.content,'lxml')
    #
    # def website(self):
    #     return self.soup.prettify()



    def product_name(self):
        product_name=self.soup.find('div',class_='_4rR01T')
        return product_name.text

    def product_price(self):
        product_price = self.soup.find('div', class_='_30jeq3 _1_WHN1')
        return product_price.text

    def product_ratings(self):
        product_rating1 = self.soup.find('div', class_='_3LWZlK')
        return product_rating1.text


    # def content(self):
    #     product_detail1=self.soup.find('div',class_='fMghEO')
    #     return product_detail1.text

    def scrap_everything(self):
        product_name=[]
        product_price=[]
        product_ratings=[]
        for data in self.soup.findAll('div',class_='_3pLy-c row'):
            names = data.find('div',class_='_4rR01T')
            prices = data.find('div', class_='_30jeq3 _1_WHN1')
            ratings=data.find('div', class_='_3LWZlK')
            product_name.append(names.text)
            product_price.append(prices.text)
            product_ratings.append(ratings.text)
            product_ratings.append(ratings.text)
        print(product_name)
        print('########################')
        print(product_price)
        print('########################')
        print(product_ratings)

    # def scrap_eveything(self):
    #     product_name = []
    #     product_ratings = []
    #     product_price = []
    #
    #     for data in self.soup.findAll('div', class_='_3pLy-c row'):
    #         names = data.find('div', class_='_4rR01T')
    #         ratings = data.find('div', class_='_3LWZlK')
    #         price = data.find('div', class_='_30jeq3 _1_WHN1')
    #         product_name.append(names.text)
    #         product_ratings.append(ratings)
    #         product_price.append(price.text)
    #
    #     print(product_name)
    #     print("##############################")
    #     print(product_ratings)
    #     print("##############################")
    #     print(product_price)

# print(suman().website())
print(suman().product_name())
print(suman().product_price())
print(suman().product_ratings())
# print(suman().content())
# suman().scrap_eveything()
suman().scrap_everything()
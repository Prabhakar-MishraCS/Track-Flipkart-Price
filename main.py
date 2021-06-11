

import requests
from bs4 import BeautifulSoup

from lxml import etree
import webbrowser
import pywhatkit
import time
from datetime import datetime


url = "https://www.flipkart.com/audio-technica-at2035-large-diaphragm-studio-condenser-microphone/p/itmfdj8898ecskab?pid=MICFDGZU6TXVHBC5&lid=LSTMICFDGZU6TXVHBC5WI9EEH&marketplace=FLIPKART&q=microphone&store=ypu%2Falc%2F3d4&srno=s_3_86&otracker=AS_QueryStore_OrganicAutoSuggest_2_3_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_2_3_na_na_ps&fm=SEARCH&iid=4d86bde8-fb8e-4eb3-86a0-7ebb6972c649.MICFDGZU6TXVHBC5.SEARCH&ppt=sp&ppn=sp&ssid=kul71lkmao0000001623249557175&qH=7a05af9edb26eec3"
headers = {"UserAgent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}

page = requests.get(url,headers=headers)
print(page.status_code)

soup = BeautifulSoup(page.content,'html.parser')
#print(soup.prettify())

#***************************************************************

dom = etree.HTML(str(soup))
curr_day = datetime.today()
while True:
    price = dom.xpath('///*[@id="container"]/div/div[3]/div[1]/div[2]/div[3]/div/div[3]/div[1]/div/div[1]')[0].text
    # print(price)
    s = price.replace(',', '')
    price_updated = int(s[1:6])
    print(price_updated)

    if price_updated > 10000:

        webbrowser.open(
            'https://www.flipkart.com/audio-technica-at2035-large-diaphragm-studio-condenser-microphone/p/itmfdj8898ecskab?pid=MICFDGZU6TXVHBC5&lid=LSTMICFDGZU6TXVHBC5WI9EEH&marketplace=FLIPKART&q=microphone&store=ypu%2Falc%2F3d4&srno=s_3_86&otracker=AS_QueryStore_OrganicAutoSuggest_2_3_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_2_3_na_na_ps&fm=SEARCH&iid=4d86bde8-fb8e-4eb3-86a0-7ebb6972c649.MICFDGZU6TXVHBC5.SEARCH&ppt=sp&ppn=sp&ssid=kul71lkmao0000001623249557175&qH=7a05af9edb26eec3',
            new=1)

        hour = curr_day.strftime("%H")
        min1 = curr_day.strftime("%M")
        min_updated = int(min1) + 2
        pywhatkit.sendwhatmsg ('+916363693577', "Within the budget!, Khareed lo Mic",int(hour),min_updated)


        exit()
    else:
        print('Budget se baahar hai -_- \n')

    time.sleep(60)


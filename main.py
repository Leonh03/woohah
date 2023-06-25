import requests
from bs4 import BeautifulSoup
import time
from discord_webhook import DiscordWebhook
from datetime import datetime

def log(msg):
    print('[{}] {}'.format(datetime.now(), msg))

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'DNT': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://rollingloudrotterdam.nl/tickets/', headers=headers)
soup = BeautifulSoup(response.text,'html.parser')
price = soup.find_all('span')[55].text
log('current price - {}'.format(price))
webhook = DiscordWebhook(url='https://discordapp.com/api/webhooks/1122574317528555560/dXn1dkeC5_DUlDA1ax2w1sdOWo_uCG4TJN1dbZIEZIDM1W7skJPykv-dHAJtKDW1heHX', content='current price: {}'.format(price))
webhook.execute()
while True:
    response = requests.get('https://rollingloudrotterdam.nl/tickets/', headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    price2 = soup.find_all('span')[55].text
    if price != price2:
        webhook = DiscordWebhook(url='https://discordapp.com/api/webhooks/1122574317528555560/dXn1dkeC5_DUlDA1ax2w1sdOWo_uCG4TJN1dbZIEZIDM1W7skJPykv-dHAJtKDW1heHX',content='price change {} => {}'.format(price, price2))
        webhook.execute()

        log('price changed ! - {}'.format(price2))
        price = price2
        time.sleep(100)


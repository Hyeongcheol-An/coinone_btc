import json
import urllib.request
import codecs
import threading
from urllib.request import Request, urlopen
from time import sleep
import datetime


def coinone():

	urlTicker = urllib.request.urlopen('https://api.coinone.co.kr/trades')
	readTicker = urlTicker.read().decode('utf8')
	jsonTicker = json.loads(readTicker)
	FindTIME = jsonTicker['timestamp']
	TIME = int(FindTIME)
	for h in jsonTicker['completeOrders']:
		FindBTC = h['price']
	BTC = int(FindBTC)
	s = datetime.datetime.now()
	print(s, "BTC", BTC, "원")
	threading.Timer(1, coinone).start()
	urlTicker = urllib.request.urlopen('https://api.coinone.co.kr/orderbook')


if __name__ == "__main__":

	coinone()

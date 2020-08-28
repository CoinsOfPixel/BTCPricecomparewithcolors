import colorama
from colorama import Fore, Style, Back
import tkinter
import json
from urllib.request import urlopen
import threading

last_btc_price_list = []

def comparador():
	#O Try/Exception de agora resolve aquele bug feio que aparecia no início quando não havia
	#nada para mostrar e o programa dava o erro de fora de index. 
	try:

	        urlBTCUSD = 'https://www.bitstamp.net/api/ticker/'
 
	        json_obj_BTCUSD = urlopen(urlBTCUSD)

	        btc = json.load(json_obj_BTCUSD)

	        btcUSDPrice = float(btc['last'])

	        last_btc_price_list.append(btcUSDPrice)
    
            #Não compara até ter três posições e depois mostra o penúltimo.
	        btc_last_price = last_btc_price_list[-2]


	        print("√")

	        print("» Actual BTC price: " + str(btcUSDPrice))

	        print("« Last BTC price: " + str(btc_last_price))

	        print("\n")

	        if btcUSDPrice > btc_last_price:
		        print(Fore.GREEN + "█ BIGGER ▲")
		        print(Style.RESET_ALL)
    
	        if btcUSDPrice < btc_last_price:
		        print(Fore.RED + "█ SMALLER ▼")
		        print(Style.RESET_ALL)

	        if btcUSDPrice == btc_last_price:
		        print(Fore.YELLOW + "█ SAME ●")
		        print(Style.RESET_ALL)

	        print("\n")
            #Apenas um debug para mostrar que a lista está funcionando e se enchendo com os dados
	        #print(last_btc_price_list)

	        #print("\n")
	except IndexError:
		print("\n")
		print("Aguarde, estamos coletando dados para começar...")
		print("\n")


def contador():
	threading.Timer(5, contador).start()
	comparador()

contador()


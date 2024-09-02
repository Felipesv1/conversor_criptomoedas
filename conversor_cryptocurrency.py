import requests
from utils.url_API import URL_API
def brl_to_btc(brl_amount):
  
    response = requests.get(URL_API)
    data = response.json()
    btc_price_in_brl = data['bitcoin']['brl']
    btc_amount = brl_amount / btc_price_in_brl
    return btc_amount

def btc_to_brl(btc_amount):
    response = requests.get(URL_API)
    data = response.json()
    btc_price_in_brl = data['bitcoin']['brl']
    brl_amount = btc_amount * btc_price_in_brl
    return brl_amount


control = 1;
while True:
    if control == 3:
        break;
    print("CONVERSOR DE CRIPTOMOEDA")
    print("1-Converter Bitcoins em Reais")
    print("2-Converter Reais em Bitcoins")
    print("3-Sair")
    print("--------------------------------------------", end='\n')
    control = int(input("Escolha uma opção:"))
    if control == 1:
        print(".", end='\n')
        print(".", end='\n')
        btc_value = float(input("Digite o valor em Bitcoins: "))
        print(".", end='\n')
        brl_value = btc_to_brl(btc_value)
        print(f"{btc_value} BTC é equivalente a {brl_value:.2f} BRL")
        print("--------------------------------------------", end='\n')
    elif control == 2:
        print(".", end='\n')
        print(".", end='\n')
        brl_value = float(input("Digite o valor em Reais: "))
        print(".", end='\n')
        btc_value = brl_to_btc(brl_value)
        print(f"{brl_value} BRL é equivalente a {btc_value:.8f} BTC")
        print("--------------------------------------------", end='\n')
        
        
print("--------------------------------------------", end='\n')
print("Fim da conversão")

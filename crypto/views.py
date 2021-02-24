from urllib import request
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def home(request):
    import requests
    import json

    price_request= requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,ADA,DOT,BCH,LTC,XLM,BNB,USTD,XMR&tsyms=USD")
    price= json.loads(price_request.content)
    api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api= json.loads(api_request.content)
    return render(request, 'home.html', {'api': api, 'price': price} )

def prices(request):
    if request.method == 'POST':
        import requests
        import json
        price = request.POST['price']
        price = price.upper()
        crypto_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=" + price + "&tsyms=USD")
        crypto = json.loads(crypto_request.content)
        return render(request, 'prices.html', {'price': price, 'crypto': crypto})
    else:

        return render(request, 'home.html', {})


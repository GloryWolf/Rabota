usd = 57
euro = 60
grv = 2.07
cny = 8.8
btc = 556484.28

money = int(input("Vvedite summu, kot vi hotite obmenjatb: "))
currency = int(input("Ykagite kod valuty (dollar - 400, evro - 401, grv - 402, cny - 403, btc - 404): "))

if currency == 400:
    cache = round(money / usd, 2)
    print("Valuta: dollar USA")
elif currency == 401:
    cache = round(money / euro, 2)
    print("Valuta: evro")
elif currency == 402:
    cache = round(money / grv, 2)
    print("Valuta: grv")
elif currency == 403:
    cache = round(money / cny, 2)
    print("Valuta: cny")
elif currency == 404:
    cache = round(money / btc, 2)
    print("Valuta: btc")
else:
    cache = 0
    print("Unknown valute")

print("K polycheniy:", cache)

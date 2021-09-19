from pycoingecko import CoinGeckoAPI
from src.reformat import reformat


cg = CoinGeckoAPI()


print("Type number and program will print you top N cryptocurrencies by now:")
n = int(input())
line = cg.get_coins()[:n]
result = []
for j in range(n):
    m = str(line[j])
    result.append(reformat(m))

print(result)

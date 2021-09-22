from pycoingecko import CoinGeckoAPI
import sys
sys.path.append("src")
import reformat as p


cg = CoinGeckoAPI()


print("Type number and program will print you top N cryptocurrencies by now:")
n = int(input())
line = cg.get_coins()[:n]
result = []
for j in range(n):
    m = str(line[j])
    result.append(p.reformat(m))

print(result)

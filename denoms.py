import csv
import json
import math
from unicodedata import decimal
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()

# filename = './csv/rektdrop_2.csv'

denoms = {}

p = open('./prices.json')
prices = json.load(p)

with open('./frontier.assetlist.json') as assetlist:
    data = json.load(assetlist)

    for asset in data['assets']:


        decimals = -1

        for denom_unit in asset['denom_units']:
            if denom_unit['denom'] == asset['display']:
                decimals = denom_unit['exponent']

        if decimals == -1:
            raise Exception('No Decimals found') 


        price = 0

        if 'coingecko_id' in asset.keys() and asset['coingecko_id'] in prices.keys():
            price = prices[asset['coingecko_id']]['usd']

        

        denoms[asset['base']] = [asset['symbol'], decimals, price]
        

print(json.dumps(denoms))

# balances = {}

# with open(filename, 'r') as csvfile:
#     datareader = csv.reader(csvfile)
#     next(datareader, None)
#     for row in datareader:
#         tokens = row[2].split(",")
#         for token in tokens:
#             tokenname = ""
#             amount = 0
#             if "uosmo" in token:
#                 tokenname = "uosmo"
#                 amount = int(token.replace(tokenname, ""))
#             elif "uion" in token:
#                 tokenname = "uion"
#                 amount = int(token.replace(tokenname, ""))
#             elif "ibc" in token:
#                 spl = token.split("ibc")
#                 amount = int(spl[0])
#                 tokenname = "ibc" + spl[1]
#             else:
#                 raise Exception(token)


#             balances.setdefault(tokenname, 0)
#             balances[tokenname] += amount


# redenominated_balances = {}

# for base, amount in balances.items():
#     metadata = denom_mapping[base]

#     redenominated_balances[metadata[0]] = amount / math.pow(10, metadata[1])

#     # print(metadata[2])


# print(json.dumps(balances))



# # for name, amount in redenominated_balances.items():
# #     print(amount)
import csv
import json
import math
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()

# filename = './csv/rektdrop_2.csv'

coingecko_ids = []

with open('./frontier.assetlist.json') as assetlist:
    data = json.load(assetlist)

    for asset in data['assets']:
        
        decimals = -1


        if 'coingecko_id' in asset.keys():
            coingecko_ids += [asset['coingecko_id']]

# print(json.dumps(denom_mapping))

# print(','.join(coingecko_ids))


price = cg.get_price(ids=','.join(coingecko_ids), vs_currencies='usd')

print(json.dumps(price))

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
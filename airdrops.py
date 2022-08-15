from audioop import add
import csv
import json
import math

filename = './csv/rektdrop_2.csv'

p = open('./prices.json')
prices = json.load(p)

balances = {}

with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    next(datareader, None)
    for row in datareader:
        address = row[0]

        tokens = row[2].split(",")
        for token in tokens:
            tokenname = ""
            amount = 0
            if "uosmo" in token:
                tokenname = "uosmo"
                amount = int(token.replace(tokenname, ""))
            elif "uion" in token:
                tokenname = "uion"
                amount = int(token.replace(tokenname, ""))
            elif "ibc" in token:
                spl = token.split("ibc")
                amount = int(spl[0])
                tokenname = "ibc" + spl[1]
            else:
                raise Exception(token)


            balances.setdefault(tokenname, {})
            balances[tokenname].setdefault(address, 0)
            balances[tokenname][address] += amount


denoms = data = json.load(open('./denoms.json'))


for outputtoken in balances:

    sum = 0
    output = []

    for addr in balances[outputtoken]:
        amount = balances[outputtoken][addr]
        output += [{"address": addr, "amount": amount }]
        sum += amount


    sorted(output, key=lambda k: k['amount'], reverse=True)


    # print(json.dumps(sorted(output, key=lambda k: k['amount'])))


    with open('airdrops/'+ denoms[outputtoken][0] +'.json', 'w') as f:
        json.dump(sorted(output, key=lambda k: k['amount'], reverse=True), f, indent=4)


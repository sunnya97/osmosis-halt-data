import csv
import json
import math

denoms = json.load(open('./denoms.json'))

total_needed =0

for denom in denoms:
    try:
        file = open('./airdrops/' + denoms[denom][0] + '.json')

        entries = json.load(file)
        total = 0

        filtered_balances = []

        for entry in entries:
            total += 1
            # print(float(entry['amount']) * denoms[denom][2] )
            if float(entry['amount']) / math.pow(10, denoms[denom][1]) * denoms[denom][2] > 0.5:
                filtered_balances += [entry]

        # print(denoms[denom][0])
        # print(num_real)
        # print(total)
        # print(float(num_real)/float(total))

        print (str(denoms[denom][0]) + ' - ' + str(float(len(filtered_balances))/float(total)) + '%')

        if len(filtered_balances) > 0:
            with open('filtered/'+ denoms[denom][0] +'_filtered.json', 'w') as f:
                json.dump(filtered_balances, f, indent=4)

    except FileNotFoundError:
        pass



print (total_needed)
# balances = {}

# with open(filename, 'r') as csvfile:
#     datareader = csv.reader(csvfile)
#     next(datareader, None)
#     for row in datareader:
#         address = row[0]

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


#             balances.setdefault(tokenname, {})
#             balances[tokenname].setdefault(address, 0)
#             balances[tokenname][address] += amount


# denoms = data = json.load(open('./denoms.json'))


# for outputtoken in balances:

#     sum = 0
#     output = []

#     for addr in balances[outputtoken]:
#         amount = balances[outputtoken][addr]
#         output += [{"address": addr, "amount": amount }]
#         sum += amount


#     sorted(output, key=lambda k: k['amount'], reverse=True)


#     # print(json.dumps(sorted(output, key=lambda k: k['amount'])))


#     with open('airdrops/'+ denoms[outputtoken][0] +'.json', 'w') as f:
#         json.dump(sorted(output, key=lambda k: k['amount'], reverse=True), f, indent=4)


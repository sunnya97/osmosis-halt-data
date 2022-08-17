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
        unincluded_balances = []

        for entry in entries:
            total += 1
            # print(float(entry['amount']) * denoms[denom][2] )
            if float(entry['amount']) / math.pow(10, denoms[denom][1]) * denoms[denom][2] > 0.5:
                filtered_balances += [entry]
            else:
                unincluded_balances += [entry]

        # print (str(denoms[denom][0]) + ' - ' + str(float(len(filtered_balances))/float(total)) + '%')
        print (str(denoms[denom][0]) + ' - ' + denom + ' - ' + str(len(filtered_balances)))
        

        # if len(filtered_balances) > 0:
        #     with open('filtered/'+ denoms[denom][0] +'_filtered.json', 'w') as f:
        #         json.dump(filtered_balances, f, indent=4)

        # if len(unincluded_balances) > 0:
        #     with open('unincluded/'+ denoms[denom][0] +'.json', 'w') as f:
        #         json.dump(unincluded_balances, f, indent=4)

    except FileNotFoundError:
        pass



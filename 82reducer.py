# Logan Krohn
# Crypto 24H Performance Reducer 

import sys

thisKey = ""
thisValue = ""

for line in sys.stdin:
  datalist = line.strip(' \t\n\r%').split('\t')
  if (len(datalist) == 2) : 
    crypto, amount = datalist

    if float(amount) <= 0:   # finding the negative percentages
      thisKey = crypto
      thisValue = amount
      # output the previous key-summaryvalue result
      print(thisKey,'\t',thisValue)

      # start over for each new key
      thisKey = ""
      thisValue = ""
  
 

# output the final key-summaryvalue result outside the loop
print(thisKey,'\t',thisValue)
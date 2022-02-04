# Logan Krohn
# Crypto 24H Performance Mapper 

import sys 

# iterate through each line provided via standard input
for line in sys.stdin:
  datalist = line.strip().split(",")
  if (len(datalist) == 10) : 
    Ranking,cryptoName,Price,Changes24H ,Changes7D ,Changes30D ,Changes1Y,MarketCap,Volume24H,AvailableSupply = datalist

    # print intermediate key-value pairs to standard output
    print(cryptoName,"\t",Changes24H)
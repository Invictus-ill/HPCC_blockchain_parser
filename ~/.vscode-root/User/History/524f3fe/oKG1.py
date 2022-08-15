import os
import sys as sys
import pandas as pd
from HPCC_bitcoin_parser.blockchain import Blockchain



rows=[]
# Instantiate the Blockchain by giving the path to the directory
# containing the .blk files created by bitcoind

df=pd.DataFrame( columns=['tx_hash', 'in_index', 'in_hash', 'out_index', 'out_addr', 'out_val', 'timestamp'])
counter = 0
blockchain = Blockchain(os.path.expanduser('~/.bitcoin/blocks'))
for i, block in enumerate(blockchain.get_unordered_blocks()):
    print(i)
    for tx in block.transactions:
        counter +=1
        if(counter == 10000):
            df = df.append(df, pd.Series(data, index = df.columns))
            rows=[]
            counter=0
        # print("\nHash " + tx.hash)
        # print("-----------------------------------")
        # print("\nInputs")
        for no, input in enumerate(tx.inputs):
            #print("tx=%s outputno=%d type=%s value=%s" % (tx.hash, no, output.type, output.value))
            # print("Hash : " + str(input.transaction_hash) + "\nIndex : " +str(input.transaction_index))
            # print("\nOutput")
            for no_out, output in enumerate(tx.outputs):
                #print("tx=%s outputno=%d type=%s value=%s" % (tx.hash, no, output.type, output.value))
                # print("No : "+ str(no_out)+"\nAddy : " + str(output.addresses[0].address)+"\nValue : "+str(output.value))

                rows.append([tx.hash,input.transaction_index, input.transaction_hash, no_out, output.addresses[0].address, output.value, block.header.timestamp])
                # print(rows)
        
    if(i == int(sys.argv[1])):
        break

# df=pd.DataFrame(rows, columns=['tx_hash', 'in_index', 'in_hash', 'out_index', 'out_addr', 'out_val', 'timestamp'])
df.to_csv('test.csv', index=False)
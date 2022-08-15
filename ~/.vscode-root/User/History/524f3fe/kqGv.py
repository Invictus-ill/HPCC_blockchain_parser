import os
from HPCC_bitcoin_parser.blockchain import Blockchain

# Instantiate the Blockchain by giving the path to the directory
# containing the .blk files created by bitcoind
blockchain = Blockchain(os.path.expanduser('~/.bitcoin/blocks'))
for block in blockchain.get_unordered_blocks():
    for tx in block.transactions:
        # for no, output in enumerate(tx.outputs):
        #     print("tx=%s outputno=%d type=%s value=%s" % (tx.hash, no, output.type, output.value))
        print(tx.inputs, tx.outputs)
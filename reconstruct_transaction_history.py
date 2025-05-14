# Scans all blocks in the block archive JSON files in the current directory, https://github.com/NicolasFlamel1/MimbleWimble-Coin-Block-Archive?tab=readme-ov-file#mainnet-blocks, to reconstruct a wallet's transaction history. All applicable UTXOs and when they were spent are logged to a file, and a brief overview of the wallet's transaction history is shown in the console. This code lacks any error checking. A wallet's rewind hash can be obtained by running the command `mwc-wallet rewind_hash` with the MWC CLI wallet, https://github.com/mwcproject/mwc-wallet.
# Install required dependencies with: pip install secp256k1_zkp_mw


# Imports
from secp256k1_zkp_mw import *
from hashlib import blake2b
import time
from datetime import datetime
import os
import re
import json


# Constants

# Rewind hash
REWIND_HASH = bytes.fromhex('0000000000000000000000000000000000000000000000000000000000000000')

# Network type
NETWORK_TYPE = 'mainnet'


# Functions

# Format number
def formatNumber(number):

    # Return formatted number
    return '{:.9f}'.format(number / 1E9).rstrip('0').rstrip('.')


# Main function

# Create context
context = secp256k1_context_create(SECP256K1_CONTEXT_VERIFY | SECP256K1_CONTEXT_SIGN)

# Get blocks files
blocksFiles = [file for file in os.listdir() if re.search(r'^' + NETWORK_TYPE + r' blocks \d+\-\d+\.json$', file)]

# Sort blocks files in numeric order
blocksFiles.sort(key = lambda file:int(re.search(r'^' + NETWORK_TYPE + r' blocks (\d+)\-\d+\.json$', file).group(1)))

# Get first height from the first blocks file
firstHeight = int(re.search(r'^' + NETWORK_TYPE + r' blocks (\d+)\-\d+\.json$', blocksFiles[0]).group(1))

# Get the tip height from the last blocks file
tipHeight = int(re.search(r'^' + NETWORK_TYPE + r' blocks \d+\-(\d+)\.json$', blocksFiles[-1]).group(1))

# Set file name
fileName = 'transaction history ' + str(datetime.now()).split('.')[0] + '.txt'

# Display start message
print('Scanning blocks %d to %d and writing the transaction history to \'%s\' for the wallet with the rewind hash %s.' % (firstHeight, tipHeight, fileName, REWIND_HASH.hex()))

# Initialize current outputs
currentOutputs = {}

# Open file
with open(fileName, 'w') as file:

    # Initialize last percent time
    lastPercentTime = time.time()

    # Initialize mined amount
    minedAmount = 0

    # Initialized mined start block
    minedStartBlock = 0

    # Go through all blocks files
    for blocksFile in blocksFiles:

        # Open current blocks file
        with open(blocksFile, 'r') as currentBlocksFile:

            # Get blocks from the current blocks file
            blocks = json.load(currentBlocksFile)

            # Go through all blocks in the blocks file
            for block in blocks:

                # Initialize spent amount
                spentAmount = 0

                # Initialize received amount
                receivedAmount = 0

                # Go through all inputs in the block
                for input in block['inputs']:

                    # Check if input is a current outputs
                    if input in currentOutputs:

                        # Add input's amount to spent amount
                        spentAmount += currentOutputs[input]

                        # Write spent output message to file
                        file.write('Spent output %s containing %s MWC in block %d at %s\n' % (input, formatNumber(currentOutputs[input]), block['header']['height'], block['header']['timestamp']))

                        # Remove input from current outputs
                        del currentOutputs[input]

                # Go through all outputs in the block
                for output in block['outputs']:

                    # Get commit and proof from the output
                    commit = bytes.fromhex(output['commit'])
                    proof = bytes.fromhex(output['proof'])

                    # Get rewind nonce for the commit
                    rewindNonce = blake2b(REWIND_HASH, digest_size = 32, key = commit).digest()

                    # Check if the output belongs to the wallet
                    internalCommit = secp256k1_pedersen_commitment_parse(context, commit)
                    outputData = secp256k1_bulletproof_rangeproof_rewind(context, proof, 0, internalCommit, secp256k1_generator_const_h, rewindNonce, None)

                    if outputData is not None:

                        # Get amount from the output data
                        amount = outputData[0]

                        # Check if output is a coinbase reward
                        if output['output_type'] == 'Coinbase':

                            # Add output's amount to mined amount
                            minedAmount += amount

                        # Otherwise
                        else:

                            # Add output's amount to received amount
                            receivedAmount += amount

                        # Write received output message to file
                        file.write('Received %s output %s containing %s MWC in block %d at %s\n' % ('coinbase' if output['output_type'] == 'Coinbase' else 'transaction', output['commit'], formatNumber(amount), block['header']['height'], block['header']['timestamp']))

                        # Add output to current outputs
                        currentOutputs[output['commit']] = amount

                # Check if amount was spent or received
                if spentAmount != 0 or receivedAmount != 0:

                    # Check if mined amount exists
                    if minedAmount != 0:

                        # Show mined amount message
                        print('You mined %s MWC from block %d to block %d.' % (formatNumber(minedAmount), minedStartBlock, block['header']['height']))

                        # Reset mined amount
                        minedAmount = 0

                        # Reset mined start block
                        minedStartBlock = block['header']['height'] + 1

                    # Initialize balance
                    balance = 0

                    # Go through all current outputs
                    for output in currentOutputs:

                        # Add output's amount to balance
                        balance += currentOutputs[output]

                    # Check if more was spent than received
                    if spentAmount > receivedAmount:

                         # Show spent and received amount message
                        print('You spent %s MWC and received %s MWC in block %d at %s. You probably sent someone %s MWC including fees. Current balance is %s MWC.' % (formatNumber(spentAmount), formatNumber(receivedAmount), block['header']['height'], block['header']['timestamp'], formatNumber(spentAmount - receivedAmount), formatNumber(balance)))

                    # Otherwise
                    else:

                        # Show spent and received amount message
                        print('You spent %s MWC and received %s MWC in block %d at %s. Current balance is %s MWC.' % (formatNumber(spentAmount), formatNumber(receivedAmount), block['header']['height'], block['header']['timestamp'], formatNumber(balance)))

                # Get current time
                currentTime = time.time()

                # Check if a minute has passed since the last percent time
                if currentTime - lastPercentTime >= 60:

                    # Show percent complete message
                    print('%s%% complete.' % ('{:.9f}'.format(block['header']['height'] / tipHeight * 100).rstrip('0').rstrip('.')))

                    # Update last percent time
                    lastPercentTime = currentTime

    # Check if mined amount exists
    if minedAmount != 0:

        # Show mined amount message
        print('You mined %s MWC from block %d to block %d.' % (formatNumber(minedAmount), minedStartBlock, tipHeight))

# Show done scanning message
print('Done scanning.')

# Initialize balance
balance = 0

# Go through all current outputs
for output in currentOutputs:

    # Add output's amount to balance
    balance += currentOutputs[output]

# Show final balance message
print('Final balance is %s MWC.' % (formatNumber(balance)))

# Destroy the context
secp256k1_context_destroy(context)

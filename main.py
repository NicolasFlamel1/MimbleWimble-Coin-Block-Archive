# Imports
import requests
import sys
import os
import json
import subprocess


# Main function

# Check if no network type isn't provided
if len(sys.argv) < 2:

	# Display error
	print("No network type provided");
	
	# Exit
	sys.exit(os.EX_USAGE);

# Check if network type is invalid
if sys.argv[1] != "mainnet" and sys.argv[1] != "floonet":

	# Display error
	print("Invalid network type");
	
	# Exit
	sys.exit(os.EX_USAGE);

# Get network type
networkType = sys.argv[1];

# Check if no full archive node address isn't provided
if len(sys.argv) < 3:

	# Display error
	print("No full archive node address provided");
	
	# Exit
	sys.exit(os.EX_USAGE);

# Check if full archive node address is invalid
if (not sys.argv[2].startswith("http://") and not sys.argv[2].startswith("https://")) or (sys.argv[2].startswith("http://") and len(sys.argv[2]) == len("http://")) or (sys.argv[2].startswith("https://") and len(sys.argv[2]) == len("https://")):

	# Display error
	print("Invalid full archive node address");
	
	# Exit
	sys.exit(os.EX_USAGE);

# Get full archive node address
fullArchiveNodeAddress = sys.argv[2];

# Check if start height isn't provided
if len(sys.argv) < 4:

	# Display error
	print("No start height provided");
	
	# Exit
	sys.exit(os.EX_USAGE);

# Check if start height is invalid
if not sys.argv[3].isdigit() or len(sys.argv[3]) == 0 or (sys.argv[3] != "0" and sys.argv[3].startswith("0")):

	# Display error
	print("Invalid start height");
	
	# Exit
	sys.exit(os.EX_USAGE);

# Get start height
startHeight = int(sys.argv[3]);

# Check if number of blocks isn't provided
if len(sys.argv) < 5:

	# Display error
	print("No number of blocks provided");
	
	# Exit
	sys.exit(os.EX_USAGE);

# Check if number of blocks is invalid
if not sys.argv[4].isdigit() or len(sys.argv[4]) == 0 or sys.argv[4].startswith("0"):

	# Display error
	print("Invalid number of blocks");
	
	# Exit
	sys.exit(os.EX_USAGE);

# Get number of blocks
numberOfBlocks = int(sys.argv[4]);

# Get output file name
outputFileName = "./" + networkType + " blocks " + str(startHeight) + "-" + str(startHeight + numberOfBlocks - 1) + ".json";

# Open output file
with open(outputFileName, "w", encoding="utf-8") as outputFile:

	# Write start of array to output file
	outputFile.write("[");
	
	# Go through all requested blocks
	for i in range(numberOfBlocks):
	
		# Check if not at the first request block
		if i != 0:
		
			# Write next in array to output file
			outputFile.write(",");

		# Request block information from the full archive node
		response = requests.post(fullArchiveNodeAddress + "/v2/foreign", json = {
			"jsonrpc": "2.0",
			"id": 1,
			"method": "get_block",
			"params": [
				startHeight + i,
				None,
				None
			]
		});
		
		# Get block
		block = response.json()["result"]["Ok"];
		
		# Write block to output file
		json.dump(block, outputFile);
	
	# Write end of array to output file
	outputFile.write("]");

# Get compressed file name
compressedFileName = "./" + networkType + "_blocks_" + str(startHeight) + "-" + str(startHeight + numberOfBlocks - 1) + ".zip";

# Compress output file
subprocess.run(["7z", "a", compressedFileName, outputFileName, "-mx9"]);

# Add release to git repo
subprocess.run(["gh", "release", "create", networkType.title() + "_Blocks_" + str(startHeight) + "-" + str(startHeight + numberOfBlocks - 1), compressedFileName, "-t", networkType.title() + " Blocks " + str(startHeight) + "-" + str(startHeight + numberOfBlocks - 1), "-n", networkType.title() + " blocks " + str(startHeight) + "-" + str(startHeight + numberOfBlocks - 1)]);

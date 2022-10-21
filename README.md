# MimbleWimble Coin Block Archive

### Description
Archive of all MimbleWimble Coin mainnet and floonet blocks. Each [release](https://github.com/NicolasFlamel1/MimbleWimble-Coin-Block-Archive/releases) includes a zip file that contains a JSON file consisting of an array of 100000 blocks. Each block is stored in the same format that's returned by a node's foreign API when performing a `get_block` JSON-RPC call to it.

### Running
If you want to create the files yourself, you can run the following command while passing in a network type, a full archive node's address, a start height, and the number of blocks desired as command line arguments to the program. This example uses the network type `mainnet`, the full archive node address `http://localhost:3413`, the start height `1524200`, and the number of blocks `50` which will create the JSON file `mainnet blocks 1524200-1524249.json`.
```
python3 main.py mainnet http://localhost:3413 1524200 50
```

# MimbleWimble Coin Block Archive

### Description
Archive of MimbleWimble Coin mainnet and floonet blocks. Each [release](https://github.com/NicolasFlamel1/MimbleWimble-Coin-Block-Archive/releases) includes a zip file that contains a JSON file consisting of an array of 100000 blocks. Each block is stored in the same format that's returned by a node's foreign API when performing a `get_block` JSON-RPC call to it.

### Running
If you want to create the files yourself, you can run the following command while passing in a network type, a full archive node's address, a start height, and the number of blocks desired as command line arguments to the program. This example uses the network type `mainnet`, the full archive node address `http://localhost:3413`, the start height `1524200`, and the number of blocks `50` which will create the JSON file `mainnet blocks 1524200-1524249.json`.
```
python3 main.py mainnet http://localhost:3413 1524200 50
```

### Mainnet Blocks
* [Mainnet blocks 0-99999](https://github.com/NicolasFlamel1/MimbleWimble-Coin-Block-Archive/releases/download/Mainnet_Blocks_0-99999/mainnet_blocks_0-99999.zip)
* [Mainnet blocks 100000-199999](https://github.com/NicolasFlamel1/MimbleWimble-Coin-Block-Archive/releases/download/Mainnet_Blocks_100000-199999/mainnet_blocks_100000-199999.zip)
* [Mainnet blocks 200000-299999](https://github.com/NicolasFlamel1/MimbleWimble-Coin-Block-Archive/releases/download/Mainnet_Blocks_200000-299999/mainnet_blocks_200000-299999.zip)
* [Mainnet blocks 300000-399999](https://github.com/NicolasFlamel1/MimbleWimble-Coin-Block-Archive/releases/download/Mainnet_Blocks_300000-399999/mainnet_blocks_300000-399999.zip)
* [Mainnet blocks 400000-499999](https://github.com/NicolasFlamel1/MimbleWimble-Coin-Block-Archive/releases/download/Mainnet_Blocks_400000-499999/mainnet_blocks_400000-499999.zip)
* [Mainnet blocks 500000-599999](https://github.com/NicolasFlamel1/MimbleWimble-Coin-Block-Archive/releases/download/Mainnet_Blocks_500000-599999/mainnet_blocks_500000-599999.zip)
* [Mainnet blocks 600000-699999](https://github.com/NicolasFlamel1/MimbleWimble-Coin-Block-Archive/releases/download/Mainnet_Blocks_600000-699999/mainnet_blocks_600000-699999.zip)
* [Mainnet blocks 700000-799999](https://github.com/NicolasFlamel1/MimbleWimble-Coin-Block-Archive/releases/download/Mainnet_Blocks_700000-799999/mainnet_blocks_700000-799999.zip)
* [Mainnet blocks 800000-899999](https://github.com/NicolasFlamel1/MimbleWimble-Coin-Block-Archive/releases/download/Mainnet_Blocks_800000-899999/mainnet_blocks_800000-899999.zip)
* [Mainnet blocks 900000-999999](https://github.com/NicolasFlamel1/MimbleWimble-Coin-Block-Archive/releases/download/Mainnet_Blocks_900000-999999/mainnet_blocks_900000-999999.zip)
* [Mainnet blocks 1000000-1099999](https://github.com/NicolasFlamel1/MimbleWimble-Coin-Block-Archive/releases/download/Mainnet_Blocks_1000000-1099999/mainnet_blocks_1000000-1099999.zip)
* [Mainnet blocks 1100000-1199999](https://github.com/NicolasFlamel1/MimbleWimble-Coin-Block-Archive/releases/download/Mainnet_Blocks_1100000-1199999/mainnet_blocks_1100000-1199999.zip)
* [Mainnet blocks 1200000-1299999](https://github.com/NicolasFlamel1/MimbleWimble-Coin-Block-Archive/releases/download/Mainnet_Blocks_1200000-1299999/mainnet_blocks_1200000-1299999.zip)
* [Mainnet blocks 1300000-1399999](https://github.com/NicolasFlamel1/MimbleWimble-Coin-Block-Archive/releases/download/Mainnet_Blocks_1300000-1399999/mainnet_blocks_1300000-1399999.zip)
* [Mainnet blocks 1400000-1499999](https://github.com/NicolasFlamel1/MimbleWimble-Coin-Block-Archive/releases/download/Mainnet_Blocks_1400000-1499999/mainnet_blocks_1400000-1499999.zip)
* [Mainnet blocks 1500000-1599999](https://github.com/NicolasFlamel1/MimbleWimble-Coin-Block-Archive/releases/download/Mainnet_Blocks_1500000-1599999/mainnet_blocks_1500000-1599999.zip)
* [Mainnet blocks 1600000-1699999](https://github.com/NicolasFlamel1/MimbleWimble-Coin-Block-Archive/releases/download/Mainnet_Blocks_1600000-1699999/mainnet_blocks_1600000-1699999.zip)
* [Mainnet blocks 1700000-1799999](https://github.com/NicolasFlamel1/MimbleWimble-Coin-Block-Archive/releases/download/Mainnet_Blocks_1700000-1799999/mainnet_blocks_1700000-1799999.zip)
* [Mainnet blocks 1800000-1899999](https://github.com/NicolasFlamel1/MimbleWimble-Coin-Block-Archive/releases/download/Mainnet_Blocks_1800000-1899999/mainnet_blocks_1800000-1899999.zip)
* [Mainnet blocks 1900000-1999999](https://github.com/NicolasFlamel1/MimbleWimble-Coin-Block-Archive/releases/download/Mainnet_Blocks_1900000-1999999/mainnet_blocks_1900000-1999999.zip)
* [Mainnet blocks 2000000-2099999](https://github.com/NicolasFlamel1/MimbleWimble-Coin-Block-Archive/releases/download/Mainnet_Blocks_2000000-2099999/mainnet_blocks_2000000-2099999.zip)
* [Mainnet blocks 2100000-2199999](https://github.com/NicolasFlamel1/MimbleWimble-Coin-Block-Archive/releases/download/Mainnet_Blocks_2100000-2199999/mainnet_blocks_2100000-2199999.zip)
* [Mainnet blocks 2200000-2299999](https://github.com/NicolasFlamel1/MimbleWimble-Coin-Block-Archive/releases/download/Mainnet_Blocks_2200000-2299999/mainnet_blocks_2200000-2299999.zip)
* [Mainnet blocks 2300000-2399999](https://github.com/NicolasFlamel1/MimbleWimble-Coin-Block-Archive/releases/download/Mainnet_Blocks_2300000-2399999/mainnet_blocks_2300000-2399999.zip)
* [Mainnet blocks 2400000-2499999](https://github.com/NicolasFlamel1/MimbleWimble-Coin-Block-Archive/releases/download/Mainnet_Blocks_2400000-2499999/mainnet_blocks_2400000-2499999.zip)
* [Mainnet blocks 2500000-2599999](https://github.com/NicolasFlamel1/MimbleWimble-Coin-Block-Archive/releases/download/Mainnet_Blocks_2500000-2599999/mainnet_blocks_2500000-2599999.zip)
* [Mainnet blocks 2600000-2699999](https://github.com/NicolasFlamel1/MimbleWimble-Coin-Block-Archive/releases/download/Mainnet_Blocks_2600000-2699999/mainnet_blocks_2600000-2699999.zip)
* [Mainnet blocks 2700000-2799999](https://github.com/NicolasFlamel1/MimbleWimble-Coin-Block-Archive/releases/download/Mainnet_Blocks_2700000-2799999/mainnet_blocks_2700000-2799999.zip)
* [Mainnet blocks 2800000-2899999](https://github.com/NicolasFlamel1/MimbleWimble-Coin-Block-Archive/releases/download/Mainnet_Blocks_2800000-2899999/mainnet_blocks_2800000-2899999.zip)

### Floonet Blocks
* [Floonet blocks 0-99999](https://github.com/NicolasFlamel1/MimbleWimble-Coin-Block-Archive/releases/download/Floonet_Blocks_0-99999/floonet_blocks_0-99999.zip)
* [Floonet blocks 100000-199999](https://github.com/NicolasFlamel1/MimbleWimble-Coin-Block-Archive/releases/download/Floonet_Blocks_100000-199999/floonet_blocks_100000-199999.zip)
* [Floonet blocks 200000-299999](https://github.com/NicolasFlamel1/MimbleWimble-Coin-Block-Archive/releases/download/Floonet_Blocks_200000-299999/floonet_blocks_200000-299999.zip)
* [Floonet blocks 300000-399999](https://github.com/NicolasFlamel1/MimbleWimble-Coin-Block-Archive/releases/download/Floonet_Blocks_300000-399999/floonet_blocks_300000-399999.zip)
* [Floonet blocks 400000-499999](https://github.com/NicolasFlamel1/MimbleWimble-Coin-Block-Archive/releases/download/Floonet_Blocks_400000-499999/floonet_blocks_400000-499999.zip)
* [Floonet blocks 500000-599999](https://github.com/NicolasFlamel1/MimbleWimble-Coin-Block-Archive/releases/download/Floonet_Blocks_500000-599999/floonet_blocks_500000-599999.zip)
* [Floonet blocks 600000-699999](https://github.com/NicolasFlamel1/MimbleWimble-Coin-Block-Archive/releases/download/Floonet_Blocks_600000-699999/floonet_blocks_600000-699999.zip)
* [Floonet blocks 700000-799999](https://github.com/NicolasFlamel1/MimbleWimble-Coin-Block-Archive/releases/download/Floonet_Blocks_700000-799999/floonet_blocks_700000-799999.zip)
* [Floonet blocks 800000-899999](https://github.com/NicolasFlamel1/MimbleWimble-Coin-Block-Archive/releases/download/Floonet_Blocks_800000-899999/floonet_blocks_800000-899999.zip)
* [Floonet blocks 900000-999999](https://github.com/NicolasFlamel1/MimbleWimble-Coin-Block-Archive/releases/download/Floonet_Blocks_900000-999999/floonet_blocks_900000-999999.zip)
* [Floonet blocks 1000000-1099999](https://github.com/NicolasFlamel1/MimbleWimble-Coin-Block-Archive/releases/download/Floonet_Blocks_1000000-1099999/floonet_blocks_1000000-1099999.zip)
* [Floonet blocks 1100000-1199999](https://github.com/NicolasFlamel1/MimbleWimble-Coin-Block-Archive/releases/download/Floonet_Blocks_1100000-1199999/floonet_blocks_1100000-1199999.zip)
* [Floonet blocks 1200000-1299999](https://github.com/NicolasFlamel1/MimbleWimble-Coin-Block-Archive/releases/download/Floonet_Blocks_1200000-1299999/floonet_blocks_1200000-1299999.zip)
* [Floonet blocks 1300000-1399999](https://github.com/NicolasFlamel1/MimbleWimble-Coin-Block-Archive/releases/download/Floonet_Blocks_1300000-1399999/floonet_blocks_1300000-1399999.zip)
* [Floonet blocks 1400000-1499999](https://github.com/NicolasFlamel1/MimbleWimble-Coin-Block-Archive/releases/download/Floonet_Blocks_1400000-1499999/floonet_blocks_1400000-1499999.zip)

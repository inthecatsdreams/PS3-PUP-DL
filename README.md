# PS3-PUP-DL

A cli tool to download PS3 firmwares (uses midnightchannel as its source)

## Requirements
- Python 3
- Python request
- Beautiful soup


## Example usage
--download will always defaults to false
--fwtype will use DEX by default
**If you want to just browse the archive:**
`python3 madl.py --fwtype DEX --no-download`

**If you want download all firmwares for a specific type (DEX, CEX, REBUG)**
`python3 madl.py --fwtype REBUG --download`

# searchTPB

A minimalist script that searches The Pirate Bay [through the clearnet or tor].

The script asks the user for a search query and returns the corresponding list of torrents from The Pirate Bay for the given query. The user then selects a torrent, whose magnet link will be copied to the clipboard.

### Dependencies
- python3
- selenium (python)
- dmenu
- tor (needed if The Pirate Bay is inaccesible for you)

### Installation
Copy 'getPageSource.py' and 'searchTPB' to your PATH and make them executable.

### Usage
`searchTPB [-t]` The `-t` flag enables access to The Pirate Bay through tor.

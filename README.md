# searchTPB

A minimalist script that searches ThePirateBay.

The script asks the user for a search query and returns the corresponding list of torrents from The Pirate Bay for the given query. The user then selects the torrent whose magnet link will be copied to the clipboard.

### Dependencies
- python
- selenium (python)
- dmenu
- tor (needed if ThePirateBay is inaccesible for you)

### Installation
Copy 'getPageSource.py' and 'searchTPB' to your PATH and make them executable.

### Usage
Normally: `searchTPB`
If TPB is inaccesible for you: `searchTPB -t`

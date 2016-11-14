# TerminalTalk
Terminal Run Chat Application

Requirements: Python 2.7

SETUP:
- Open TerminalTalk_server.py
  - For use on LAN
    - Change server_address (line 14) to server's local IP
  - For use on WAN
    - Change server_address (line 14) to server's public IP

- Open TerminalTalk.py
  - For use on LAN
    - Change server_address (line 20) to server's local IP
  - For use on WAN
    - Change server_address (line 20) to server's public IP


TO START SERVER:
- Open Terminal
- cd to TerminalTalk directory.
- Enter 'python TerminalTalk_server.py'


TO START CLIENT:
- Open Terminal
- cd to TerminalTalk directory.
- Enter 'python TerminalTalk.py [moniker]'


COMMANDS:
\\setmoniker [moniker]     # Moniker is your desired username
\\setcolor [color]         # Available colors are red, green, yellow, blue, magenta, and cyan
\\disconnect               # Must be followed by a space

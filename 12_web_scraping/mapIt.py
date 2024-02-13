#! python3
# mapIT.py - Luauches a map in the browser using an address from the command line or clipboard.
# testable input: "python mapIt.py 870 Valencia St, San Francisco, CA 94110"

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '.join(sys.argv[1:])

else:
    # Get address from clipboard.
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
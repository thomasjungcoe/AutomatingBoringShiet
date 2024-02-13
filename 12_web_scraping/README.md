WEB SCRAPING
    Web scarping is the term for using a program to download and process content from the web.
        For example, Google runs many web scraping programs to index web pages for its search engine.
        This learning will go over serveral modules that make it easy to scrape web pages in Python.
            * webbrowser - comes with python and opens a browser to a specific page
            * requests   - downloads files and web pages from the internet
            * bs4        - parses HTML, the format that web pages are written in.
            * selenium   - luanches and controls a web browser - also able to fill in forms and simulate mouse clicks in this browser

Project: MapIT.PY with the webbrowser module
    The webbrowser module’s open() function can launch a new browser to a specified URL. 
        ex.)
            import webbrowser
            webbrowser.open('https://inventwithpython.com')
                1.) Gets a street address from the command line arguments or clipboard
                2.) Opens the web browser to the Google Maps page for the address
            What can be done after:
                1.) Read the command line arguments from sys.argv.
                2.) Read the clipboard contents.
                3.) Call the webbrowser.open() function to open the web browser.

Downloading Files from the Web with the requests Module
    The "request" module lets you easily download files from the web without having to worry about complicated issues such as network errors, connection problems, and data compression.
        the request module doesn't come with Python so manual installation is required, "pip install --user requests"
    This module was written because Python's "urllib2" module is too complicated to use.
        The raise_for_status() method is a good way to ensure that a program halts if a bad download occurs.

Saving Downloaded Files to the Hard Drive
    open(), close()
    write()
    wb - write binary (you need to write binary data instead of text data in order to maintain the Unicode encoding of the text.)


Hypertext Markup Language (HTML) 
    HTML is the format that web pages are written in.
        tags
        elements
        text (inner HTML)
        
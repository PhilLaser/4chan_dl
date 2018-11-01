# 4chan_dl

This is a command line webm download script written in Python.
At the moment this application only works for 4chan threads.

The following modules are used inside the code:

 * 'requests' for getting the HTML of the website.

 * 'BeautifulSoup' to parse the HTML and extract data.

 * 'urllib' for HTTP-requests.

 * 'tqdm' for progress bars.

 * 'ffmpy' for converting the .webm into .mp4


Usage: 4chan_dl.py \<ThreadURL> <path_where_to_store_the_files>

Passing '-h' or '--help' as first argument prints the usage message.




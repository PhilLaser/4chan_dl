import requests
import os
import sys
import urllib.request
from bs4 import BeautifulSoup
from tqdm import tqdm
import ffmpy


def get_thread():
    return soup.find('span', {'class': 'subject'}).string


if __name__ == '__main__':
    if sys.argv[1] == '-h' or sys.argv[1] == '--help':
        print ("Usage: 4chan_dl.py <ThreadURL> <path_where_to_store_the_files>")
    else:
        url = sys.argv[1]  # url to parse
        file_path = sys.argv[2]  # path
        links = []
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')

        thread_title = get_thread() if get_thread() is not None else url.split("thread/", 1)[1]
        thread_title = thread_title.replace(" ", "_")
        for a in soup.find_all('a', 'fileThumb', href=True):
            links.append("https:" + a['href'])

        if not os.path.exists(thread_title):
            os.mkdir(thread_title)

        abs_path = os.path.abspath(os.path.join(os.sep, os.getcwd(), thread_title))

        for i in tqdm(range(len(links))):
            response = urllib.request.urlopen(links[i])
            fl = open(os.path.join(file_path + "/" + thread_title + "/" + "%i.webm" % i), 'wb')
            fl.write(response.read())
            fl.close()
            ff = ffmpy.FFmpeg(inputs={abs_path + "/" + "%i.webm" % i: ["-loglevel", "panic"]},
                              outputs={abs_path + "/" + "%i.mp4" % i: ["-r", "30"]}
                              )
            ff.run()
            os.remove(fl.name)

        print("Done!")

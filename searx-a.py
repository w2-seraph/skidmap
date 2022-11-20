import requests
from bs4 import BeautifulSoup
import time
import random
from urllib.parse import urlparse
import codecs
import os
import subprocess

# Uncomment line 62 & remove line 63 for proxyless

os.system("cat ak-skid.ans")
print("")
print("")
dorkfile = "dorks.txt"

proxies = {
    "http": "http://p.webshare.io:9999",
    "https": "http://p.webshare.io:9999",
}

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0",
    "Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0",
    "Mozilla/5.0 (X11; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0",
]

random_user_agent = random.choice(user_agents)

headers = {"User-Agent": random_user_agent}


with open(dorkfile) as fp:
    urls = []

    line = fp.readlines()
    totalLines = len(line)
    currentLine = 0

    for dork in line:
        for x in range(0,3):
            print ("\033[A                             \033[A")
        currentLine +=1

        print("Total urls:")
        os.system("wc -l dorks_out.txt | grep -Eo '[0-9]{1,4}'")
        subprocess.call(["python3", "same-domain-append.py"], stdout=subprocess.DEVNULL)
        time.sleep(1.5)
        print(f"\n[{currentLine}/{totalLines}][QUERY]: {dork}", end='\r')

        with open('dorks.txt', 'r') as fin:
            data = fin.read().splitlines(True)
        with open('dorks.txt', 'w') as fout:
            fout.writelines(data[1:])

        count = 1

        while count != 10:
            # URL = f"https://searx.pussthecat.org/search?q={dork}&language=en-US&time_range=None&safesearch=0&categories=general&pageno={count}"

            URL = f"https://searx.rimkus.it/search?q={dork}&language=en-US&time_range=None&safesearch=0&categories=general&pageno={count}"

            # perform get request to the url
            try:

		# reqs = requests.get(URL, headers=headers, timeout=10)
                reqs = requests.get(URL, proxies=proxies, headers=headers, timeout=10)

                content = reqs.text

            except Exception as e:
                print("[-]Connection error:", end='\r')
                print(e,  end='\r')
                print("\033[A                             \033[A")
                pass

            if len(content) < 30000:
                print(f"[-]Breaking to {count} of {len(content)} length",  end='\r')
                time.sleep(1)
                count = 10
                break
            if len(content) > 30000:
                count += 1

            soup = BeautifulSoup(content, "html.parser")

            for h in soup.findAll("article"):
                a = h.find("a")
                try:
                    if "href" in a.attrs:

                        url = a.get("href")
                        urls.append(url)

                except:
                    pass

            pageLength = len(content)
            print(f"[-]Paginating {count-1}/10 len[{pageLength}]",  end='\r')
            time.sleep(1)
        dorksout = "dorks_out.txt"

        # bad urls
        for url in urls:

            if "?" in url:
                bad_words = [
                    "youtube",
                    "207",
                    "amazon",
                    "google",
                    "gov",
                    "mil",
                    "bbs",
                    "quora",
                    "cve",
                    "stackoverflow",
                    "binance",
                    "microsoft",
                    "facebook",
                    "ebay",
                    "reddit",
                    "edu",
                    ".kr",
                    ".cn",
                    "207.241.228.197",
                    "archive",
                    "moodle",
                    "103.2",
                    ".jp"
                ]

    
                dork_file = open("dorks_out.txt", "a")

                if not any(bad_word in url for bad_word in bad_words):
                    dork_file.write(url)
                    dork_file.write("\n")
                    dork_file.close()
                urls = []


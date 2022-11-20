from urllib.parse import urlparse
import codecs
import os
import colorama
from colorama import Fore, Style

# Negotiates with (remote) server running sqlmap, disregard misleading name
# Would not tamper with

all_urls = open('dorks_out.txt').readlines()
# dorks_hour = codecs.open('/media/xs/dorks-h.txt', 'r')
# dorks_hour_int = int(dorks_hour.read()[0:4])

# dorks_hour_oth = []

# for line in dorks_hour:
# 	dorks_hour_oth.append(line)


unique_urls = []

for url in all_urls:
    url = url.strip()
    root_url = urlparse(url).hostname
    is_duplicate = any(str(root_url) in unique_url for unique_url in unique_urls)
    if not is_duplicate:
        unique_urls.append(url)

unique_urls_file = codecs.open('dorks_out.txt', 'w')

for unique_url in unique_urls:
    unique_urls_file.write(unique_url + '\n')

unique_urls_file.close()

print("")
print(len(unique_urls))
# print(Fore.GREEN)
# print(str(dorks_hour_oth[0]))
# print(Style.RESET_ALL)

# if dorks_hour_int <= 200:
# print(f"{Fore.GREEN}{print(dorks_hour_oth[0])}{Style.RESET_ALL}")
# if dorks_hour_int in range(200,998):
   #     print(f"{Fore.GREEN}{dorks_hour_int}/h{Style.RESET_ALL}")
# if dorks_hour_int >= 999:
  #      print(f"{Fore.MAGENTA}{dorks_hour_oth}{Style.RESET_ALL}")

urlRun = len(unique_urls)

if urlRun > 2000:
    print("[==>]Pushing dorks")
    os.system("sh pushdorks.sh")
    print(len(unique_urls))

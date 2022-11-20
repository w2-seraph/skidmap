from urllib.parse import urlparse
import codecs

all_urls = open('vuln.out', encoding='utf-8', errors='ignore').readlines()
print('[+]all urls count = ', len(all_urls))
unique_urls = []

for url in all_urls:
    url = url.strip()
    root_url = urlparse(url).hostname
    is_duplicate = any(str(root_url) in unique_url for unique_url in unique_urls)
    if not is_duplicate:
        unique_urls.append(url)

unique_urls_file = codecs.open('vuln.out', 'w', encoding='utf8')

for unique_url in unique_urls:
    unique_urls_file.write(unique_url + '\n')

unique_urls_file.close()

print('--------------------')
print('[+]Vulnerable unique urls count = ', len(unique_urls))
print('[+]wrote vuln.out')
print('--------------------')

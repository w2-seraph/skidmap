from urllib.parse import urlparse
import codecs

all_urls = open('linkz.txt', encoding='utf-8', errors='ignore').readlines()
print('[+]all urls count = ', len(all_urls))
unique_urls = []

for url in all_urls:
    url = url.strip()
    root_url = urlparse(url).hostname
    is_duplicate = any(str(root_url) in unique_url for unique_url in unique_urls)
    if not is_duplicate:
        unique_urls.append(url)

unique_urls_file = codecs.open('linkz.txt', 'w', encoding='utf8')

for unique_url in unique_urls:
    unique_urls_file.write(unique_url + '\n')

unique_urls_file.close()

print('--------------------')
print('[+]Linkz unique urls count = ', len(unique_urls))
print('[+]wrote linkz.txt')
print('--------------------')

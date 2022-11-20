from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import codecs
import os

## Enter base words into init_word.txt
## Keyword propegator, run this first to generate keywords.txt
## Then run dork_gen_inurl.py

os.system("echo > keywords.txt")

path = 'chromedriver' # path of your chromedriver file

# master_keyword = input('Enter something to search for: ')
# total_keywords = int(input('Enter maximum number of keywords to fetch: '))
total_keywords = 5

service = Service(executable_path=path)
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(service=service, options=chrome_options)

init_keyword = open('init_word.txt', encoding='utf-8', errors='ignore').readlines()

total_outwords = []

for initalword in init_keyword:
    
    driver.get('https://keywordshitter.com/')
    driver.execute_script("Reset()")
    text_area = driver.find_element(By.ID, 'input')
    text_area.send_keys(initalword)
    print(f"[+]Query:{initalword}".strip())
    start_job = driver.find_element(By.ID, 'sheetingText')
    start_job.click()
    keyword_div = driver.find_element(By.ID, 'numofkeywords')
    shouldLoop = True
    keywords_list = list
    while(shouldLoop):
        keyword_count_text = keyword_div.text.split(':')
        keyword_count_1 = int(keyword_count_text[0])
        keyword_count_2 = int(keyword_count_text[1])
        if(keyword_count_1 >= total_keywords or keyword_count_2 >= total_keywords):
            start_job.click()
            shouldLoop = False
            data = text_area.get_attribute('value')
            keywords_list = data.split('\n')
            keywords_list = [i for i in keywords_list if(len(i.strip())!=0)]

            for k in keywords_list:
                total_outwords.append(k)
            

for lol in total_outwords:
    unique_keyword = codecs.open('keywords.txt', 'a', encoding='utf8')
    unique_keyword.write(lol)
    unique_keyword.write("\n")
    

unique_keyword.close()
print(f"\n[+]Wrote {len(total_outwords)} initial keywords to keywords.txt")

from time import sleep
import requests
import random
import string
from colorama import Fore

scrape = input(f"{Fore.WHITE}[ {Fore.YELLOW}> {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Proxy Scrape? {Fore.WHITE}(yes or no){Fore.LIGHTBLACK_EX}: {Fore.WHITE}")

if scrape == "no":
  input()
  exit()

if scrape == "yes":
  f = open("proxies.txt", "a+")
  f.truncate(0)
  r = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=15000&ssl=yes')
  proxies = []
  for proxy in r.text.split('\n'):
      proxy = proxy.strip()
      if proxy:
          proxies.append(proxy)
  for p in proxies:
        scraped = scraped + 1 
      f.write((p)+"\n")
  f.close()
  print(f"{Fore.WHITE}[ {Fore.YELLOW}? {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Scraped {Fore.WHITE}{scraped} {Fore.LIGHTBLACK_EX}proxies.")
  exit()

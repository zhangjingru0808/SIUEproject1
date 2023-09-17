import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("URL")
args = parser.parse_args()
address = args.URL


r = requests.get(address).content
str_content = r.decode('utf-8')
fp = open("contents.txt","w", encoding='utf-8')
fp.write(str_content)
fp.close()

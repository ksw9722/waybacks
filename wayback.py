import argparse
import sys
import requests
import subprocess

parser = argparse.ArgumentParser()

parser.add_argument("-u",type=str,required=True,help="Input url")
parser.add_argument("--header",type=str,required=False)
parser.add_argument("-p",type=str,required=False,default="http://127.0.0.1:8080",help="proxy url",metavar="http://127.0.0.1:8080")


args = parser.parse_args()
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6367.60 Safari/537.36"}

http_proxy  = args.p
https_proxy = args.p



proxies = { 
              "http"  : http_proxy, 
              "https" : https_proxy
            }

if args.header!=None:
    headerName, headerValue = args.headers.split(':')
    headerName = headerName.strip()
    headerValue = headerValue.lstrip()
    headers[headerName]=headerValue

waybackCmd = f"waybackurls {args.u}"
waybacks = subprocess.check_output(waybackCmd,shell=True).decode()
result = waybacks

waybackUrls = waybacks.split('\n')

for url in waybackUrls:
    if len(url)<2:
        continue
    
    try:
        requests.get(url,headers=headers,proxies=proxies,verify=False)
        print(url)
    except Exception as e:
        pass


print(result)
f = open('result.txt','w')
f.write(result)
f.close()
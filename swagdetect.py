import concurrent.futures
import requests
from optparse import OptionParser
from httpx import get
requests.packages.urllib3.disable_warnings()
from termcolor import colored
import bs4

parser = OptionParser()
parser.add_option("-u", "--url", dest="url",help="Url to scan.", metavar="URL")
parser.add_option("-f", "--file", dest="file",help="File to scan", metavar="FILE")
parser.add_option("-v", "--verbose", dest="verbose",help="Showing the entered url", metavar="VERBOSE",action="store_true")
parser.add_option("-o", "--output", dest="output",help="Save the result to a file", metavar="OUTPUT")
(options, args) = parser.parse_args()
url=options.url
file=options.file
verbose=options.verbose
output=options.output

def check_url(path):
    try:
        response = get(path, verify=False, timeout=10)
        if response.status_code == 200:
            html = bs4.BeautifulSoup(response.text,"html.parser")
            title=str(html.title)
            if "Swagger" in title:
                print(colored("[+] Swagger UI detected at " + path,'blue'))
                if output:
                    with open(output,"a") as file:
                        file.writelines(path)
                        file.write("\n")
        else:
            print(colored("[!] HTTP error " + str(response.status_code) + " at " + path,'red'))
    except Exception as e:
        print(colored("[!] Exception: " + str(e) + " at " + path,'red'))

def check_file(line):
    with open(line) as read:
        for line in read:
            line=line.strip()
            if verbose:
                print(line)
            with open('payloads.txt') as slist:
                for line1 in slist:
                    line1=line1.strip()
                    path=line+"/"+line1
                    executor.submit(check_url, path)

executor = concurrent.futures.ThreadPoolExecutor(max_workers=10)

if url:
    if verbose:
        print(url)
    else:
        pass
    with open('payloads.txt','r') as slist:
        for line in slist:
            line=line.strip()
            path=url+"/"+line
            executor.submit(check_url, path)

if file:
    check_file(file)

executor.shutdown(wait=True)

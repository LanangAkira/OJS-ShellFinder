import asyncio
import requests



class color:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


async def getRequest(url):
    req = requests.get(url)
    status = req.status_code
    url = req.url
    if status == 200:
        print("\33[97;1mHere", f"{color.OKCYAN}{url}")
    elif status == 404:
        print("\33[91;1mxXx", f"{color.FAIL}{url}")
    else:
        print("\33[91;1mxXx", f"{color.FAIL}{url}")
    return req

print("\n\033[32;1mOJS Shell Finder By L4N4N9_4K1R4\033[0m")
print("\033[32;1mGithub : https://github.com/LanangAkira\n\033[0m")
url = input("Url: ")
if "http://" not in url:
    url = "http://" + url
filename = input("Filename: ")
no = filename.split("-")[0]
data = []
for x in range(150):
    data.append(getRequest("{}/files/journals/{}/articles/{}/submission/original/{}".format(url, x + 1, no, filename)))

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.gather(*data))


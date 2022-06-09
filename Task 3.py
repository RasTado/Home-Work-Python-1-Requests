import time
import requests
from pprint import pprint

def Stackoverflow(tagged, day):
    fromdate = time.time() - (day*86400)
    todate = time.time()
    url = 'https://api.stackexchange.com/2.3/questions'
    params = {'tagged': tagged, 'fromdate': int(fromdate), 'todate': int(todate), 'site': 'stackoverflow'}
    response = requests.get(url, params=params)
    return response.json()

if __name__ == '__main__':
    pprint(Stackoverflow('Python', 2))


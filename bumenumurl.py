#!/usr/bin/python3
import sys
import requests
import concurrent.futures,argparse

def Thread(get):
    headers = {'user-agent': 'fellipgomes/bumenumurl github'}
    try:
        if 'https' in get or 'http' in get:
            get = get.strip()
            r = requests.get(get,headers=headers,timeout=30)
            msg=f"[{r.status_code}] - {get}"
            print(msg.replace('\n',''))
        else:
            get = get.strip()
            get = f"http://{get}"
            r = requests.get(get, headers=headers,timeout=30)
            msg=f"[{r.status_code}] - {get}"
            print(msg.replace('\n',''))
    except Exception as e:
        msg=f"[?] - {get}"
        print(msg.replace('\n',''))
        print(e)

def run(source, tt):
    if tt < 10:
        tt = 10
    with open(source, 'r') as list_file:
        with concurrent.futures.ThreadPoolExecutor(max_workers=tt) as executor:
            for get in list_file:
                executor.submit(Thread, get)    
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", default=20, type=int, help="threads")
    parser.add_argument("-f", default=False, type=str, help="file")
    parser.add_argument("-v", "--verbosity", action="count", default=0)
    args = parser.parse_args()
    if args.f:
        run(args.f, args.t)
    else:
        with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
            for u in sys.stdin:
                executor.submit(Thread, u)

if __name__ == "__main__":
    main()

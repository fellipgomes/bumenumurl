#!/usr/bin/python3
import sys
import requests
import concurrent.futures,argparse

def Thread(get, sfind):
    headers = {'user-agent': 'fellipgomes/bumenumurl github'}
    get = get.strip()
    try:
        if 'https' in get or 'http' in get:
            r = requests.get(get,headers=headers,timeout=30)
            if sfind:
                desc = r.text
                for single_line in desc.splitlines():
                    if sfind in single_line:
                        print(f"[FOUND] - {get} - {single_line}")
            else:
                print(f"[{r.status_code}] - {get}")
        else:
            get = f"http://{get}"
            r = requests.get(get, headers=headers,timeout=30)
            print(f"[{r.status_code}] - {get}")
    except Exception as e:
        get = get.strip()
        print(f"[?] - {get}")

def run(source, tt, sfind):
    if tt < 10:
        tt = 10
    with open(source, 'r') as list_file:
        with concurrent.futures.ThreadPoolExecutor(max_workers=tt) as executor:
            for get in list_file:
                executor.submit(Thread, get, sfind)    
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", default=20, type=int, help="threads")
    parser.add_argument("-f", default=False, type=str, help="file")
    parser.add_argument("-s", default=False, type=str, help="Find string")
    parser.add_argument("-v", "--verbosity", action="count", default=0)
    args = parser.parse_args()
    if args.f:
        run(args.f, args.t, args.s)
    else:
        with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
            for u in sys.stdin:
                executor.submit(Thread, u, args.s)

if __name__ == "__main__":
    main()

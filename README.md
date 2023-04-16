# bumenumurl
Check urls, status code, capture urls from file or other program

Use in conjunction with waybackurls to enumerate all urls, advanced use for `Redteam` and `Bugbounty`

Requirements: `python3, pip`.

Usage example:


```
▶ cat urls.txt | bumenumurl
```
```
▶ waybackurls *nubank.com.br | bumenumurl
```
```
▶ bumenumurl -f urls.txt -t 5 | grep 200
```

Install:

```
▶ git clone https://github.com/fellipgomes/bumenumurl.git && cd bumenumurl
```
```
▶ pip3 install -r requirements.txt
```
```
▶ sudo cp bumenumurl.py /usr/local/bin/bumenumurl
```
## Credit

Fellip Melo [linkedin](https://www.linkedin.com/in/fellipmelo/).

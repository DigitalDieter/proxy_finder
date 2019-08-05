[![Build Status](https://travis-ci.org/DigitalDieter/proxy_finder.svg?branch=master)](https://travis-ci.org/DigitalDieter/proxy_finder)

# proxy finder

These python scripts download and check https, socks5, socks4 proxy server.

![](header.png)

## Installation

OS X & Linux:

```bash
python -m pip install -r requirements.txt
```

Windows:

```bash
python get_socks5.py -h
```

## Usage example
Default server = 100

For downloading proxy server execute the following command.


Download and save 50 https proxy-server ./source folder 
```bash
python get_https.py -n 50
```

Download and save 50 socks5 proxy-server ./source folder 
```bash
python get_socks5.py -n 50
```

Download and save 50 socks4 proxy-server ./source folder 
```bash
python get_socks4.py -n 50
```

For checking proxies
```bash
python check_proxy.py -n 50
```




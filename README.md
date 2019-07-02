# proxy finder

[![Build Status][travis-image]][travis-url]

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

For check proxys

```bash
python check_proxy.py -n 50
```
<<<<<<< HEAD
=======

>>>>>>> 7eab3d85159f4e8cae43de74bdad4872f8c8391b



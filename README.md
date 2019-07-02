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


## Meta

Your Name – [@YourTwitter](https://twitter.com/dbader_org) – YourEmail@example.com

Distributed under the XYZ license. See ``LICENSE`` for more information.

[https://github.com/yourname/github-link](https://github.com/dbader/)

## Contributing

1. Fork it (<https://github.com/yourname/yourproject/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

<!-- Markdown link & img dfn's -->
[npm-image]: https://img.shields.io/npm/v/datadog-metrics.svg?style=flat-square
[npm-url]: https://npmjs.org/package/datadog-metrics
[npm-downloads]: https://img.shields.io/npm/dm/datadog-metrics.svg?style=flat-square
[travis-image]: https://img.shields.io/travis/dbader/node-datadog-metrics/master.svg?style=flat-square
[travis-url]: https://travis-ci.org/dbader/node-datadog-metrics
[wiki]: https://github.com/yourname/yourproject/wiki

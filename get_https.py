import asyncio
import argparse
from proxybroker import Broker

import warnings
warnings.filterwarnings("ignore")

parser = argparse.ArgumentParser(description='Find Proxy Server')
parser.add_argument('-n', '--n_results', type=int, default=20,
                    help='number of proxy server')

args = parser.parse_args()
number = args.n_results

filename = 'source/' + str(number) + '_https_proxies.txt'

async def save(proxies, filename):
    count = 0
    with open(filename, 'w') as f:
        while True:
            proxy = await proxies.get()
            if proxy is None:
                break
            # proto = 'https' if 'HTTPS' in proxy.types else 'http'
            row = '%s:%d\n' % (proxy.host, proxy.port)
            f.write(row)
            count = count + 1
            print(count, row)


def main():
    proxies = asyncio.Queue()
    broker = Broker(proxies)
    tasks = asyncio.gather(broker.find(types=['HTTPS'], limit=number),
                           save(proxies, filename=filename))
    loop = asyncio.get_event_loop()
    loop.run_until_complete(tasks)


if __name__ == '__main__':
    main()

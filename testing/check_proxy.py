import requests
import pandas as pd
from connection_handler import connect_db


# Read csv file:
csv_path = 'source/100_https_proxies.txt'
url = "http://example.com"

proxies = pd.DataFrame(
    {'Proxy-Server': [], 'Response': [], 'Status': [], 'Proto': []})

# Read from csv
df = pd.read_csv(csv_path, names=['Proxy-Server', 'Response'])
df['Response'] = 0
df['Status'] = 'untested'
df['Proto'] = 'https'

# define useragent

for index, row in df.iterrows():
    if row['Status'] == 'untested':
        try:
            response = requests.get(
                url, proxies={'http': row['Proxy-Server'], 'https': row['Proxy-Server']},
                timeout=(1, 5))

            if response.status_code == 200:
                proxies = proxies.append(
                    {'Proxy-Server': row['Proxy-Server'], 'Status': 'alive',
                     'Response': response.elapsed.total_seconds(), 'Proto': 'https'},
                    ignore_index=True)

                print(index, row['Proxy-Server'], 'OK')
            else:
                pass

        except Exception as e:
            print(index, row['Proxy-Server'], e.__class__.__name__)
            pass
else:
    print("Test finished")


with connect_db() as conn:
    proxies.to_sql('Proxy-Server', conn, if_exists='append')

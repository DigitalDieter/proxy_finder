import requests
import pandas as pd
from fake_useragent import UserAgent

# Read csv file:
csv_path = '/path/to/file.csv'

# Create proxies df
proxies = pd.DataFrame(
    {'IP_PO': [], 'Response': [], 'Status': [], 'Proto': []})

# Read from csv
df = pd.read_csv(csv_path, names=['IP_PO', 'Response'])
df['Response'] = 0
df['Status'] = 'untested'
df['Proto'] = 'https'

url = "http://example.com"

# define useragent
ua = UserAgent()
print(ua.random)

headers = {'User-Agent': ua.random}

for index, row in df[df['Response'] == 0].iterrows():
    if row["Status"] == 'untested':
        try:
            proxy = (row["IP_PO"])

            response = requests.get(
                url, proxies={"http": proxy, "https": proxy}, timeout=(1, 5), headers=headers)
            if response.status_code == 200:

                # Response time in ms
                response_time = requests.get(url, proxies={"http": proxy, "https": proxy},
                                                 timeout=(1, 5)).elapsed.total_seconds()

                # Add test results to df
                proxies = proxies.append(
                    {'IP_PO': proxy, 'Status': 'alive', 'Response': response_time,
                     'Proto': 'https'}, ignore_index=True)

                print(index, proxy, "OK")
            else:
                pass
                #print("Failed:", response.status_code)

        except Exception as x:
            print(index, proxy, x.__class__.__name__)
else:
    print("Test finished")

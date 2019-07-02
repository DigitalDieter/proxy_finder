import requests
import pandas
import proxybroker
import os


# create file structure for training data
if os.path.exists('source/'):
    print("folder source already existing")
else:
    print("create folder source")
    os.makedirs("source")


print("package versions:")
print("requests:",requests.__version__)
print("pandas:",pandas.__version__)
print("proxybroker:",proxybroker.__version__)



import requests
import pandas
import proxybroker
import os


# create file structure for training data
if not os.path.exists('source/'):
    print("create folder source")
    os.makedirs("source")
else:
    print("folder source already existing")


print("package versions:")
print("requests:",requests.__version__)
print("pandas:",pandas.__version__)
print("proxybroker:",proxybroker.__version__)



import requests
import pandas
import proxybroker
import os


# create file structure for training data
if not os.path.exists('datasets/'):
    os.makedirs("source")


print("package versions:")
print("requests:",requests.__version__)
print("pandas:",pandas.__version__)
print("proxybroker:",proxybroker.__version__)



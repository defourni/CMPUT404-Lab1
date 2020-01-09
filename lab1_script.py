import requests

#print(requests.__version__)

#google = requests.get("http://www.google.com")
#print(google)
script = requests.get("https://raw.githubusercontent.com/defourni/CMPUT404-Lab1/master/lab1_script.py")
print(script.text)


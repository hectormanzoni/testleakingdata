import requests

print ( 'Im leaking Hypeflame data')

user = 'eyJhbGci-OiJI-UzI1-NiIs-InR5cCI6IkpX'
password = 'iaWF0Ijo-xNTE-2MjM-6MDI-yfQfmZS9ujYD'

session = requests.Session()
session.auth = (user, password)

auth = session.get('https://api.agibank.com.br/')

print(auth)
print(auth.text)

auth = session.get('https://api.hypeflame.com.br/')

print(auth)
print(auth.text)

print ('Hello there')

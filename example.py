import requests

print ("Just testing pipenv and dependabot... we'll use requests.")
print ("...")

response = requests.get('https://httpbin.org/ip')

print('Your IP is {0}.'.format(response.json()['origin']))
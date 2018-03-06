from orgmanager import orgmanager
token = ''

client = orgmanager(token)
response = client.getStats()
print(response.status_code)
print(response.json())
print(response.text)

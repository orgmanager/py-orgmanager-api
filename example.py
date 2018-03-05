from orgmanager import orgmanager
token = 'vVoj1NMjKxumRjayNlC3JpBWj6nxp6pfajM0XZrNECZ6OYbWpRAxQ07ElMkh'

client = orgmanager(token)
response = client.getStats()
print(response.status_code)
print(response.json())
print(response.text)

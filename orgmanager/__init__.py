import requests

def makeRequest(self, method, uri, formData):
	url = '{baseUrl}/api{uri}'.format(
		baseUrl = 'https://orgmanager.miguelpiedrafita.com',
		uri = str(uri)
	)

	data = formData
	headers = {
		'authorization': 'Bearer {token}'.format(
			token = self.token
		),
		'user-agent': 'php-orgmanager-api',
	}

	response = requests.request(str(method), url, data=data, headers=headers)
	return response

class orgmanager:
	def __init__(self, token):
		self.token = token

	def getRoot(self):
		return makeRequest(self, 'GET', '', {})

	def getStats(self):
		return makeRequest(self, 'GET', '/stats', {})

	def getUser(self):
		return makeRequest(self, 'GET', '/user', {})

	def getOrgs(self):
		return makeRequest(self, 'GET', '/user/orgs', {})

	def getOrg(selfid):
		return makeRequest(self, 'GET', '/org/{id}'.format(
			id = id
		), {})

	def regenerateToken(self):
		return makeRequest(self, 'GET', '/token/regenerate', {})

	def changeOrgPassword(self, id, password):
		return makeRequest(self, 'POST', '/org/{id}'.format(
			id = id
		), {
			'password': password
		})

	def joinOrg(self, id, username):
		return makeRequest(self, 'POST', '/join/{id}'.format(
			id = id
		), {
			'username': username
		})

	def updateOrg(self, id):
		return makeRequest(self, 'PUT', '/org/{id}'.format(
			id = id
		), {})

	def deleteOrg(self, id):
		return makeRequest(self, 'DELETE', '/org/{id}'.format(
			id = id
		), {})

import requests

def makeRequest(self, method, uri, formData):
	'''
	Send request
	'''
	url = '{baseUrl}/api{uri}'.format(
		baseUrl = 'https://orgmanager.miguelpiedrafita.com',
		uri = str(uri)
	)

	data = formData
	headers = {
		'authorization': 'Bearer {token}'.format(
			token = self.token
		),
		'user-agent': 'py-orgmanager-api',
	}

	response = requests.request(str(method), url, data=data, headers=headers)
	return response

class orgmanager:
	'''
	Main class
	All Methods return response of packages 'requests'
	More in help(requests.Response)
	'''
	def __init__(self, token):
		'''
		Save token in self.token
		'''
		self.token = token

	def getRoot(self):
		'''
		Get root urls
		'''
		return makeRequest(self, 'GET', '', {})

	def getStats(self):
		'''
		Get OrgManager stats
		'''
		return makeRequest(self, 'GET', '/stats', {})

	def getUser(self):
		'''
		Get user info
		'''
		return makeRequest(self, 'GET', '/user', {})

	def getOrgs(self):
		'''
		Get list of orgs
		'''
		return makeRequest(self, 'GET', '/user/orgs', {})

	def getOrg(self, id):
		'''
		Get org info
		'''
		return makeRequest(self, 'GET', '/org/{id}'.format(
			id = id
		), {})

	def regenerateToken(self):
		'''
		Get new token
		'''
		return makeRequest(self, 'GET', '/token/regenerate', {})

	def changeOrgPassword(self, id, password):
		'''
		Change org password
		'''
		return makeRequest(self, 'POST', '/org/{id}'.format(
			id = id
		), {
			'password': password
		})

	def joinOrg(self, id, username):
		'''
		Join org
		'''
		return makeRequest(self, 'POST', '/join/{id}'.format(
			id = id
		), {
			'username': username
		})

	def updateOrg(self, id):
		'''
		Update org
		'''
		return makeRequest(self, 'PUT', '/org/{id}'.format(
			id = id
		), {})

	def deleteOrg(self, id):
		'''
		Delete org
		'''
		return makeRequest(self, 'DELETE', '/org/{id}'.format(
			id = id
		), {})

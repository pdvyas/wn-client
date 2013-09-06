import requests
import json

class AuthError(Exception):
	pass

class WNException(Exception):
	pass


class WNClient(object):

	def __init__(self, url, username, password):
		self.session = requests.Session()
		self.url = url
		self.login(username, password)

	def login(self, username, password):
		r = self.session.post(self.url, data={
			'cmd': 'login',
			'usr': username,
			'pwd': password
		})

		if r.json().get('message') == "Logged In":
			return r.json()
		else:
			raise AuthError

	def insert(self, doclist):
		return self.post_request({
			"cmd": "webnotes.client.insert",
			"doclist": json.dumps(doclist)
		})
		
	def update(self, doclist):
		return self.post_request({
			"cmd": "webnotes.client.save",
			"doclist": json.dumps(doclist)
		})

	def delete(self, doctype, name):
		return self.post_request({
			"cmd": "webnotes.model.delete_doc",
			"doctype": doctype,
			"name": name
		})
		
	def submit(self, doclist):
		return self.post_request({
			"cmd": "webnotes.client.submit",
			"doclist": json.dumps(doclist)
		})


	def cancel(self, doctype, name):
		return self.post_request({
			"cmd": "webnotes.client.cancel",
			"doctype": doctype,
			"name": name
		})
		
	def get_doc(self, doctype, name=None, filters=None):
		params = {
			"cmd": "webnotes.client.get",
			"doctype": doctype,
		}
		if name:
			params["name"] = name
		if filters:
			params["filters"] = json.dumps(filters)
		ret = self.get_request(params)
		return ret

	def get_request(self, params):
		res = self.session.get(self.url, params=params)
		res = self.post_process(res)
		return res

	def post_request(self, data):
		res = self.session.post(self.url, data=data)
		res = self.post_process(res)
		return res
	
	def post_process(self, response):
		if response.json() and ("exc" in response.json()) and response.json()["exc"]:
			raise WNException(response.json()["exc"])
		return response.json()['message']

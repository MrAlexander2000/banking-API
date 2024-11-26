import requests

url = 'http://127.0.0.1:5000/api/transactions/deposit'
data = {'amount':'2000' , 'user_id':'1' , 'account_id':'1234567890'}

response = requests.post(url, json=data)

print(response.text)
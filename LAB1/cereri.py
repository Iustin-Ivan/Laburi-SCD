import requests

url = "https://scd.dfilip.xyz/lab1/task1/check"
headers = {'secret2': 'SCDisBest'}
params = {'nume': 'Ivan Iustin', 'grupa': '342C2'}
body = {'secret': 'SCDisNice'}
response = requests.post(url, headers=headers, params=params, data=body)
print(response.text)


url2 = "https://scd.dfilip.xyz/lab1/task2"
json_body = {'username': 'scd', 'password': 'admin', 'nume': 'Ivan Iustin'}
response = requests.post(url2, json=json_body)
print(response.text)

url3 = "https://scd.dfilip.xyz/lab1/task3/login"
response = requests.post(url3, json=json_body)
print(response.text)
cookies = response.cookies
#print(cookies.values()[0])


url4 = "https://scd.dfilip.xyz/lab1/task3/check"
response = requests.get(url4, json=json_body, cookies=cookies)
print(response.text)
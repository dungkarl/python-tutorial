"""
    file example requests
"""

import requests

url = "https://ubuntu.com/blog/ai-ml-model-ubuntu"

URL = "https://imgs.xkcd.com/comics/python.png"
#r = requests.get(URL)

# payload = {
#     "page":2,
#     "count":25
# }
payload = {
    "name":"dungkarl",
    "password":"testing"
}

#r = requests.get("https://httpbin.org/get", params=payload) # get metthod

#r = requests.post("https://httpbin.org/post", data=payload) # post method
r = requests.get("https://httpbin.org/basic-auth/dungkarl/testing", auth=("dungkarl", "testing"))

#print(help(r))
print("All methods: ", dir(r))
#print(r.text)
#print(r.content)
#print(r.json)
#print(r.content)
# with open('python.png', 'wb') as f:
#     f.write(r.content)

print("response status:", r.status_code)
print("raise for status: ", r.raise_for_status)
print("OK: ", r.ok)
print("Iter lines: ", r.iter_lines)
print("DOC: ", r.__doc__)
print("Links: ", r.links)
print("URL: ", r.url)
print("elapsed: ", r.elapsed)
print("attrs:", r.__attrs__)
print("cookies:", r.cookies)
print(r.text)
print(r.json())
r_dict = r.json()

#print(r_dict['form']['name'])



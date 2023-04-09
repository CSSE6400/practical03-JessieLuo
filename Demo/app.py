from requests import request

res = request(method="GET", url="http://www.google.com")

print('request_status')
print(res.text)
with open("text.txt", "w") as f:
    print("file statue")
    print(f.read())
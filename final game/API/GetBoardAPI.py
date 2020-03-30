import requests

url = "https://www.notexponential.com/aip2pgaming/api/index.php?gameId=332&type=boardString"

payload = {}
files = {}
headers = {
  'x-api-key': 'c390b1f5889a538eca88',
  'userID': '881',
  "User-Agent": "Mozilla / 5.0(X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
}

response = requests.request("GET", url, headers=headers, data = payload, files = files)

print(response.text.encode('utf8'))

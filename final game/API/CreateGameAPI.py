import requests

url = "https://www.notexponential.com/aip2pgaming/api/index.php"

payload = {'teamId1': '1198',
'teamId2': '1231',
'type': 'game',
'gameType': 'TTT',
'boardSize': '3',
'target': '3'}

headers = {
  'x-api-key': 'c390b1f5889a538eca88',
  'userID': '881',
  "User-Agent": "Mozilla / 5.0(X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
}


response = requests.post(url, headers=headers, data=payload)
print(response.text)

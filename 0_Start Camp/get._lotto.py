import requests

url = 'https://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo=837'

response = requests.get(url, verify = False)

print(response.text)

lotto_data = response.json()

real_numbers = []

         
for key, value in lotto_data.items():
    if 'drwtNo' in key :
        real_numbers.append(value)

real_numbers.sort()
bnus_number = lotto_data['bnusNo']

print(real_numbers)
print(bnus_number)
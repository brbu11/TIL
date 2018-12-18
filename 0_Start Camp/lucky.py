import requests
import random

url = 'https://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo=837'

response = requests.get(url, verify = False)

print(response.text)

lotto_data = response.json()

real_numbers = []

# for key in lotto_data:
#     if 'drwtNo' in key:
#         real_numbers.append(lotto_data[key])
         
for key, value in lotto_data.items():
    if 'drwtNo' in key :
        real_numbers.append(value)

real_numbers.sort()
bnus_number = lotto_data['bnusNo']

print(real_numbers)
print(bnus_number)


numbers = list(range(1,46))

my_numbers = random.sample(numbers,6)
my_numbers.sort()
print(my_numbers)

if my_numbers == real_numbers :
    print("1등입니다")
else if     
else :
    print("꽝")

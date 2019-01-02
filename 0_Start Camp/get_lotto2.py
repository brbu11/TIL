import requests
import random

def get_real_lotto(game_number):
    real_numbers = {'numbers':[], 'bonus':0}
    url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo='
    response = requests.get(url+str(game_number)).json()
    real_numbers['bonus'] = response['bnusNo']
    for i in range(1,7):
        real_numbers['numbers'].append(response['drwtNo'+str(i)])
    print('당첨번호 : ', real_numbers['numbers'], '+ ' + str(real_numbers['bonus']))
    return real_numbers
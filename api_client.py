import requests
import urllib3
import json

urllib3.disable_warnings()



def get_response(url, retry_num = 0):
    if retry_num > 10:
         print("Не получилось сдеалать запрос. Обработаю позже") #FIXME
         return None

    r = None
    try:
        r = requests.get(url, verify=False)
    except:
        r = get_response(url, retry_num + 1)
    
    return r



def get_place(x, y,retry_num=0):
    cad_value_url = 'https://pkk.rosreestr.ru/api/features/1?_=1688262719759&text='+ str(x) + '%20' + str(y) + '&limit=40&skip=0&inPoint=true&tolerance=32'
    r = get_response(cad_value_url)
    
    cad_nums = []
    for place in r.json()['features']:
        cad_nums.append(place['attrs']['cn'])
    
    
get_place(55.771527, 37.596928)
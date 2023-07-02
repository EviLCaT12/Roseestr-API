import requests
import urllib3
import json
import rosreestr_api.utils as utils
import models
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



def get_cad_nums(x,y):
    cad_value_url = 'https://pkk.rosreestr.ru/api/features/1?_=1688262719759&text='+ str(x) + '%20' + str(y) + '&limit=40&skip=0&inPoint=true&tolerance=32'
    r = get_response(cad_value_url)
    
    cad_nums = []
    for place in r.json()['features']:
        cad_nums.append(place['attrs']['cn'])

    return cad_nums

def get_places(x, y):
    cad_nums = get_cad_nums(x,y)
    
    places = []
    for cad_num in cad_nums:
        cad_num = utils.prepare_cad_value_string(cad_num)
        url = 'https://pkk.rosreestr.ru/api/features/1/' + str(cad_num) + '?date_format=%c&_=1688266157494'
        r = get_response(url)

        if r.json()['feature'] == None:
            continue

        place_dict = r.json()['feature']['attrs']
        place = models.Place(
            address=place_dict['address'],
            cad_cost=place_dict['cad_cost'],
            util_by_doc=place_dict['util_by_doc'],
            cc_date_entering=place_dict['cc_date_entering'],
            date_cost=place_dict['date_cost'],
            application_date=place_dict['application_date'],
            area_value=place_dict['area_value'],
        )

        places.append(place)

    return places

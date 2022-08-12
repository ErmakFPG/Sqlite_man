import yaml
import requests


HTTP = 'http://127.0.0.1:8000/mapping/'
SHOPS_YML = 'shops.yml'
BANKS_YML = 'banks.yml'
MCC_CODES_YML = 'mccCodes.yml'
PEOPLE_YML = 'people.yml'
MONEY_CELLS_YML = 'moneyCells.yml'


def parsing_shops(file_name):
    result = []
    with open(file_name, encoding="utf8") as file:
        my_list = yaml.safe_load(file)
        for name in my_list:
            for key in my_list[name]:
                for value in my_list[name][key]:
                    result.append({'name': name, 'key': value, 'value': key})
    return result


def parsing_banks_mcc(file_name):
    result = []
    with open(file_name, encoding="utf8") as file:
        my_list = yaml.safe_load(file)
        for name in my_list:
            for key in my_list[name]:
                result.append({'name': name, 'key': key, 'value': my_list[name][key]})
    return result


def parsing_people(file_name):
    result = []
    with open(file_name, encoding="utf8") as file:
        my_list = yaml.safe_load(file)
        name = 'displayNameMap'
        for key in my_list[name]:
            value = my_list[name][key]
            if value == 'OUTSIDE_USER':
                result.append({'name': name, 'key': key, 'value': '00000000-0000-0000-0000-000000000001'})
            else:
                result.append({'name': name, 'key': key, 'value': my_list['people'][value]['id']})
    return result


def parsing_money_cells(file_name):
    result = []
    with open(file_name, encoding="utf8") as file:
        my_list = yaml.safe_load(file)

        temp_dict = {}
        for owner in my_list['owners']:
            for cell in owner['cells']:
                temp_dict[cell['name']] = cell['id']

        names = ['accounNumberMap', 'cardNumberMap']
        for name in names:
            for key in my_list[name]:
                value = my_list[name][key]
                if value == 'OUTSIDE':
                    result.append({'name': name, 'key': key, 'value': '00000000-0000-0000-0000-000000000001'})
                else:
                    result.append({'name': name, 'key': key, 'value': temp_dict[value]})
    return result


def config_loader():
    for el in parsing_shops('data/' + SHOPS_YML):
        requests.post(HTTP, json=el)
    for el in parsing_banks_mcc('data/' + BANKS_YML):
        requests.post(HTTP, json=el)
    for el in parsing_banks_mcc('data/' + MCC_CODES_YML):
        requests.post(HTTP, json=el)
    for el in parsing_people('data/' + PEOPLE_YML):
        requests.post(HTTP, json=el)
    for el in parsing_money_cells('data/' + MONEY_CELLS_YML):
        requests.post(HTTP, json=el)


if __name__ == "__main__":
    config_loader()
    print('Done')

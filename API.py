import requests


def get_phone(name):    
    p = requests.get(f'http://localhost:5000/api?action=phone&name={name}')
    result = p.text
    return  result

def get_name(phone):
    r = requests.get(f'http://localhost:5000/api?action=name&phone={phone}')
    result = r.text
    return result
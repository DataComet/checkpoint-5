import requests

r = requests.get('http://localhost:5000/api?action=phone&name=Urban')


def get_name(p):    
    p = requests.get('http://localhost:5000/api?action=phone&name=Urban')
    print(p.text)
    return  p
    
    
def get_phone(n):
      n = requests.get('http://localhost:5000/api?action=phone&name=0435-4355438')
      print(n.text)
      return n
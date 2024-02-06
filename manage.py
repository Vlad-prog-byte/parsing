from urllib.request import urlopen
import re

def get_html_page(url):
    try:
        with urlopen(url) as webpage:
            content = webpage.read().decode()
            return content
    except:
        raise("Error url")

def get_numbers(url):
    page = get_html_page(url).replace(' ', '').replace('-', '').replace('(', '').replace(')','')

    pattern = r'(?:8\d{10}|7\d{10}|\d{7})'
    result = set(re.findall(pattern, page))

    for i in result: 
        print(i, sep='\n')


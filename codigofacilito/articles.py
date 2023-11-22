import requests


def articles():
    """Retorna los artículos en CódigoFacilito.

    >>> type(articles()) == type(list())
    True
    """
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36', "Upgrade-Insecure-Requests": "1","DNT": "1","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate"}
    response = requests.get('https://codigofacilito.com/api/v2/articles',headers)

    if response.status_code == 200:
        payload = response.json()
        return payload['data']['articles']
    else:
        return 'Request failed!'

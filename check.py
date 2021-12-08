import requests
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
def check_status(url):
    url = 'http://' + url
    response = requests.get(url, headers=headers)
    status_response = {'status' : response.status_code}
    return status_response
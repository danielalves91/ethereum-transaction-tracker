import requests
import re

url = 'https://etherscan.io/token/0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
}

request = requests.get(url, headers=headers)

pattern = re.compile('(?<="Description" content=")([^\(]*)\(([^\)]*)')
decimal_pattern = re.compile("(?<=\\'decimals\\': \\')\d+")
token_name, token_symbol = pattern.findall(request.text)[0][0], pattern.findall(request.text)[0][1]
token_decimal = decimal_pattern.findall(request.text)[0][0]


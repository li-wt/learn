import requests

url = "https://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQNodeData"

payload = {
    "page": 38, "num": 40,
    "sort": "symbol", "asc": 1, "node": "hsgs_hgt_sh"
}
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
}

response = requests.request("GET", url, headers=headers, params=payload)
print(response.text)

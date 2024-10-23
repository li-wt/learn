import json


class SinaParse:
    def __init__(self, data: json or str):
        self.data = data

    def save(self, *data):
        """这里我们使用sql"""
        with open('data/sina.txt', 'a', encoding='utf-8') as f:
            f.write(",".join([str(i) for i in data]) + "\n")

    def parse_json(self):
        for item in self.data:
            symbol = item.get("symbol")
            code = item.get('code')
            name = item.get('name')
            trade = item.get('trade')
            price_change = item.get('pricechange')
            change_percent = item.get('changepercent')
            self.save(symbol, code, name, trade, price_change, change_percent)

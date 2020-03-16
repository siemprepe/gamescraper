class GameResult:
    def __init__(self, title, price, url, shop):
        self.title = title
        self.price = price
        self.url = url
        self.shop = shop

    def print(self):
        print(self.title + " | " + self.price + " | " + self.url + " | " + self.shop)
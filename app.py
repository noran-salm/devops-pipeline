def calc_discount(price, discount):
    if price < 0:
        raise ValueError("price cannot be negative")
    if not 0 <= discount <= 100:
        raise ValueError("Invalid Discount")
    return price - (price * discount / 100)
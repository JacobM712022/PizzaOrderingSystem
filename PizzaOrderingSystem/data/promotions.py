from datetime import datetime

class Promotion:
    def __init__(self, promo_id, name, promo_type, value, start, end):
        self.id = promo_id
        self.name = name
        self.type = promo_type
        self.value = value
        self.start = start
        self.end = end
        self.active = True

promotions = {}

def active_promotions():
    now = datetime.now()
    return [
        p for p in promotions.values()
        if p.active and p.start <= now <= p.end
    ]

def apply_promotions(item, base_price):
    discount = 0
    for promo in active_promotions():
        if promo.type == "percent" and item.category == "pizza":
            discount += base_price * (promo.value / 100)
        elif promo.type == "fixed":
            discount += promo.value
    return max(base_price - discount, 0)
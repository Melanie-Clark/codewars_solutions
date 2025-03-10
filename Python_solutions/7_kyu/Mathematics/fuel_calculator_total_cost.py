"""
Purchases of 2 or more litres get a discount of 5 cents per litre, purchases of 4 or more litres get a discount of
10 cents per litre, and so on every two litres, up to a maximum discount of 25 cents per litre.

But total discount per litre cannot be more than 25 cents. Return the total cost rounded to 2 decimal places.
Also you can guess that there will not be negative or non-numeric inputs.
"""

def fuel_price(litres, price_per_litre):
    max_discount = min(((litres // 2) * 5), 25) / 100
    return (price_per_litre * litres) - (max_discount * litres)
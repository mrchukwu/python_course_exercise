tea_prices_inr = {
    "Ginger tea" : 100,
    "Milk tea" : 50,
    "Choco tea" : 150,
    "Iced tea" : 200,
}

tea_prices_usd ={tea:price / 80 for tea, price in tea_prices_inr.items() }
print( tea_prices_usd)
 
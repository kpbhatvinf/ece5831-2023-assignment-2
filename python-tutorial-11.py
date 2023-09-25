import pricing
net_price = pricing.get_net_price(
    price=100,
    tax_rate=0.01
)
print(net_price)

import pricing as selling_price
net_price = selling_price.get_net_price(
    price=100,
    tax_rate=0.01
)


from pricing import get_net_price
net_price = get_net_price(price=100, tax_rate=0.01)
print(net_price)

'''
OUTPUT:
/home/capeie/anaconda3/envs/ece552/bin/python /home/capeie/ece5831-2023-assignment-2/python-tutorial-11.py
(ece552) (base) capeie@capeie:~/ece5831-2023-assignment-2$ /home/capeie/anaconda3/envs/ece552/bin/python /home/capeie/ece5831-2023-assignment-2/python-tutorial-11.py
101.0
101.0
'''
#using list

amazon_cart= [
    'Mobile',
    'Bag',
    'Apple',
    'Books'
]


new_cart=amazon_cart[:]    #we need to use slicing for new cart,otherwise new value will assign in amazon cart
new_cart[0]='Tablet'
print(amazon_cart)
print(new_cart)

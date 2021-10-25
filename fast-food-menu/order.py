menu = {'burger': 5.0, 'fries': 3.5, 'drink': 1.0}
order = {'burger': 0, 'fries': 0, 'drink': 0}

def display_order(order):
    count = 1
    for item, amount in order.items():
        print('{}. {} ({})'.format(count, item.capitalize(), amount))
        count += 1
    print('q. Quit')

def calc_subtotal(order, menu):
    subtotal = 0
    for item, amount in order.items():
        subtotal += (menu[item] * amount)

    return subtotal

def calc_total(order, menu):
    return calc_subtotal(order, menu) + calc_subtotal(order, menu) * 0.0725

shouldContinue = True
while shouldContinue:
    display_order(order)
    userInput = input('Choose item: ')

    if userInput == 'q' or userInput == 'Q':
        shouldContinue = False
    
    elif userInput == '1':
        order['burger'] += 1
    elif userInput == '2':
        order['fries'] += 1
    elif userInput == '3':
        order['drink'] += 1

    print('Subtotal: {}'.format(calc_subtotal(order, menu)))

print('Total: {}'.format(round(calc_total(order, menu)), 2))
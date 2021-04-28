def print_message():
  print("\nI'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.\n")


def order_mocha():
  while True:
    res = input("\nWould you like to try our limited-edition peppermint mocha?\n[a] Sure!\n[b] Maybe next time!")
    if res == 'a':
      return 'peppermint mocha'
    elif res == 'b':
      return 'mocha'
    else:
      print_message()  
  return res


def order_latte():
  res = input("And what kind of milk for your latte?\n[a] 2% milk\n[b] Non-fat milk\n[c] Soy milk\n")
  if res == 'a':
    res = 'latte'
  elif res == 'b':
    res = 'non-fat latte'
  elif res == 'c':
    res = 'soy latte'
  else:
    print_message()
    return order_latte()

  return res

def get_drink_type():

  res = input("What type of drink would you like?[a] Brewed Coffee[b] Mocha[c] Latte\n")
  if res == 'a':
    res = 'brewed coffee'
  elif res == 'b':
    res = order_mocha()
  elif res == 'c':
    res = order_latte()
  else:
    print_message()
    return get_drink_type()

  return res


def get_size():
  res = input("What size drink can I get for you? \na. Small \nb. Medium \nc. Large \n")
  
  if res == 'a':
    res = 'small'
  elif res == 'b':
    res = 'medium'
  elif res =='c':
    res = 'large'
  else:
    print_message()
    return get_size()
  return res

def get_temperature():
  res = input("How would you like your drink to be served? \na.Iced \nb.Hot \n")
  if res == 'a':
    res = 'iced'
  elif res == 'b':
    res = 'hot'
  else:
    print_message()
    return get_temperature()
  return res


def coffee_bot():
  print('Welcome to the cafe!')
  order_drink = 'y'
  drinks = []


  while order_drink == 'y':
    size = get_size()  
    drink_type = get_drink_type()

    drink = '{} {}'.format(size, drink_type)
    print('Alright, that\'s a {}!'.format(drink))
    drinks.append(drink)
    while True:
      if order_drink == 'y' or order_drink == 'n':
        order_drink = input("Would you like to order another drink? (y/n)\n")
        break
      
    print("\nOkay,so i have: \n\n")
    for x in drinks :
      print(x + " ")
        
  name = input("\nCan I get your name please: ")
  print("\nThanks " + name +"! Your drink will be ready shortly.\n")
  print("\n\n Order complete...")
coffee_bot()
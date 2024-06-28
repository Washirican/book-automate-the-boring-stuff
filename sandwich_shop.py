# !/usr/bin/env python3

import logging
import pyinputplus as pyip

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

menu = {
    'bread': {'wheat': 2.99, 'white': 1.99, 'sourdough': 3.99},
    'protein': {'chicken': 2.99, 'beef': 1.99, 'pork': 3.99},
    'cheese':  {'cheddar': 2.99, 'swiss': 1.99, 'pepper jack': 3.99},
    'extras':  {'mayo': 0.99, 'mustard': 0.99, 'tomatoes': 0.99},
}

print('\n\nWelcome to the Sandwich Shop!\n')

print(r"""
                     _          _      _     
                    | |        (_)    | |    
 ___  __ _ _ __   __| |_      ___  ___| |__  
/ __|/ _` | '_ \ / _` \ \ /\ / / |/ __| '_ \ 
\__ \ (_| | | | | (_| |\ V  V /| | (__| | | |
|___/\__,_|_| |_|\__,_| \_/\_/ |_|\___|_| |_|
                                                                
""")

print(r"""
                    _.---._
                _.-~       ~-._
            _.-~               ~-._
        _.-~                       ~---._
    _.-~                                 ~\
 .-~                                    _.;
 :-._                               _.-~ ./
 `-._~-._                   _..__.-~ _.-~
  /  ~-._~-._              / .__..--~----._
 \_____(_;-._\.        _.-~_/       ~).. . \
    /(_____  \`--...--~_.-~______..-+_______)
  .(_________/`--...--~/    _/___________/\
 /-._     \_     (___./_..-~__.....__..-~./
 `-._~-._   ~\--------~  .-~_..__.-~ _.-~
     ~-._~-._ ~---------'  / .__..--~
         ~-._\.        _.-~_/
             \`--...--~_.-~
              `--...--~        
    """)
sandwich = []
price = 0
for category, products in menu.items():
    if category in ['cheese', 'extras']:
        prompt = f'Would you like {category}?\n'
        response = pyip.inputYesNo(prompt)
        if response == 'yes':
            prompt = f'Select type of {category}:\n'
            product_list = [product for product in products.keys()]
    
            response = pyip.inputMenu(product_list, prompt=prompt, numbered=True)
            price += products[response]
            sandwich.append(response)
    else:
        prompt = f'Select type of {category}:\n'
        product_list = [product for product in products.keys()]
    
        response = pyip.inputMenu(product_list, prompt=prompt, numbered=True)
        price += products[response]
        sandwich.append(response)

print(f"Your getting a {', '.join(sandwich)} sandwich. Your total is ${price}.")
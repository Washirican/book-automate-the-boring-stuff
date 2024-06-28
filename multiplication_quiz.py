# !/usr/bin/env python3
"""
Multiplication quiz using PyInputPlus module.
"""
import logging
import random
import time

import pyinputplus as pyip

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

number_of_questions = 10
correct_answers = 0

for question in range(1, number_of_questions + 1):
    num_1 = random.randint(0, 9)
    num_2 = random.randint(0, 9)

    prompt = f'Question #{question}: {num_1} x {num_2} = '

    try:
        response = pyip.inputStr(prompt,
                                 allowRegexes=['^%s$' % (num_1 * num_2)],
                                 blockRegexes=[('.*', 'Incorrect!')],
                                 timeout=5, limit=3)
    except pyip.TimeoutException:
        print('Out of time!')
    except pyip.RetryLimitException:
        print('Out of tries!')
    else:
        # This block runs if no exceptions were raised in the try block.
        print('Correct!')
        correct_answers += 1
    time.sleep(1) # Brief pause to let user see the result.
print(f'Score: {correct_answers} of {number_of_questions}')

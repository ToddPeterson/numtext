from . import mapping_en as mapping

def numtext(number):
    number = int(number)
    num_text = ''

    # handling for negative numbers
    if number < 0:
        num_text += mapping.NEGATIVE + ' '
        number *= -1

    # handling for single digit numbers
    if number < 1000:
        num_text += map_three_digit(number)
    
    return num_text

def map_one_digit(number):
    try:
        return mapping.SINGLE[number]
    except KeyError:
        raise ValueError('Expected a single digit number')

def map_two_digit(number):
    if number >= 100:
        raise ValueError('Expected a two digit number')
    if number < 10:
        return map_one_digit(number)

    if number in mapping.DOUBLE_SPECIAL:
        return mapping.DOUBLE_SPECIAL[number]

    ones = number % 10
    tens = number // 10

    num_text = mapping.DOUBLE[tens]

    if ones > 0:
        num_text += ' ' + map_one_digit(ones)
    
    return num_text

def map_three_digit(number):
    if number >= 1000:
        raise ValueError('Expected a three digit number')
    if number < 100:
        return map_two_digit(number)
    
    tens = number % 100
    hundreds = number // 100

    num_text = mapping.SINGLE[hundreds]
    num_text += ' ' + mapping.HUNDRED

    if tens > 0:
        num_text += ' ' + mapping.AND + ' '
        num_text += map_two_digit(tens)

    return num_text

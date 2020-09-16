from . import mapping_en as mapping

def numtext(number):
    number = int(number)
    num_text = ''

    # handling for negative numbers
    if number < 0:
        num_text += 'negative '
        number *= -1

    # handling for single digit numbers
    if number < 10:
        num_text += map_single(number)
    elif number < 100:
        num_text += map_double(number)
    
    return num_text

def map_single(number):
    try:
        return mapping.SINGLE[number]
    except KeyError:
        raise ValueError('Expected a single digit number')

def map_double(number):
    if number >= 100 or number < 10:
        raise ValueError('Expected a two digit number')

    if number in mapping.DOUBLE_SPECIAL:
        return mapping.DOUBLE_SPECIAL[number]

    ones = number % 10
    tens = number // 10

    num_text = mapping.DOUBLE[tens]

    if ones > 0:
        num_text += ' ' + map_single(ones)
    
    return num_text

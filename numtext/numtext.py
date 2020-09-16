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
    
    return num_text

def map_single(number):
    try:
        return mapping.SINGLE[number]
    except KeyError:
        raise ValueError('Expected a single value number')

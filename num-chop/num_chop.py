def clean_string(string):
    '''
    Function takes a string representing some number and cleans leading zeros and negative signs.
    '''
    if string[0] == '0':
        string = string.replace('0', '~', 1)
    if string[0] == '-' and string[1] == '0':
        string = string.replace('0', '~', 1)
    string = string.translate({ord('~'): None})

    return string


def chop(n, i_digits=0):
    '''
    Function preforms i-digit chopping to provided value n.
    '''
    string = clean_string(str(n))   # Convert number to string for chopping
    s = ''                          # String to be returned as float

    for x in range(len(string)):
        if string[x] == '.' or string[x] == '-':
            i_digits+=1
            s+=string[x]
        elif x < i_digits:
            s+=string[x]
        else:
            s+='0'

    return float(s)

def expanded_form(num):
    int_part, rest = str(num).split('.')
    int_part = ' + '.join(f'{int(n) * 10**len(int_part[i:])}' for i, n in enumerate(int_part, 1) if int(n) != 0)
    rest = ' + '.join(f'{n}/{10**i}' for i, n in enumerate(rest, 1) if int(n) != 0)
    if int_part and rest:
        return f'{int_part} + {rest}'
    return int_part or rest



if __name__ == '__main__':
    assert expanded_form(1.24) == '1 + 2/10 + 4/100'
    assert expanded_form(7.304) == '7 + 3/10 + 4/1000'
    assert expanded_form(0.04) == '4/100'

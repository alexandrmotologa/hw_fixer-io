fixer_rates = {
    "EUR" : 1.00,
    "MDL" : 13.00,
    "USD" : 18.00,
    "RUB" : 0.30
}


def transform_rates(original):
    transform_rates = {}
    for code1, rate1 in original.items():
        transform_rates[code1] = { "to" : {} }
        for code2, rate2 in original.items():
            transform_rates[code1]['to'][code2] = original[code2] / original[code1]
    return transform_rates


tr = transform_rates(fixer_rates)

print( tr['MDL']['to']['RUB'])
print( tr['RUB']['to']['MDL'])

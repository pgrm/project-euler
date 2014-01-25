"""
In England the currency is made up of pound, P, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, P1 (100p) and P2 (200p).
It is possible to make P2 in the following way:

1xP1 + 1x50p + 2x20p + 1x5p + 1x2p + 3x1p
How many different ways can P2 be made using any number of coins?
"""

desiredValue = 200


def get_value(*coins):
    coin_values = [200, 100, 50, 20, 10, 5, 2, 1]
    i = 0
    sum_value = 0

    for c in coins:
        sum_value += c * coin_values[i]
        i += 1

    return  sum_value


def get_all_possible_coin_combinations():
    for P2 in xrange(0, 2):
        if get_value(P2) > desiredValue:
            break

        for P1 in xrange(0, 3):
            if get_value(P2, P1) > desiredValue:
                break

            for p50 in xrange(0, 5):
                if get_value(P2, P1, p50) > desiredValue:
                    break

                for p20 in xrange(0, 11):
                    if get_value(P2, P1, p50, p20) > desiredValue:
                        break

                    for p10 in xrange(0, 21):
                        if get_value(P2, P1, p50, p20, p10) > desiredValue:
                            break

                        for p5 in xrange(0, 41):
                            if get_value(P2, P1, p50, p20, p10, p5) > desiredValue:
                                break

                            for p2 in xrange(0, 101):
                                if get_value(P2, P1, p50, p20, p10, p5, p2) > desiredValue:
                                    break

                                for p1 in xrange(0, 201):
                                    val = get_value(P2, P1, p50, p20, p10, p5, p2, p1)
                                    if val == desiredValue:
                                        yield [P2, P1, p50, p20, p10, p5, p2, p1]
                                    elif val > desiredValue:
                                        break


count = 0
for combination in get_all_possible_coin_combinations():
    count += 1

print str(count)
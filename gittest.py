waffels = input('do you like waffels: ')
if waffels == "yes":
    print('of course you like waffels')
else:
    print('well f you')


def raise(num, power):
    result = 1
    for index in range(power):
        result = result * num
    return result

print(raise(3, 2))
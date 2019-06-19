# CalcPersents.py
#===================
# Calculate Persents
# محاسبه درصدهای مرتبط به یک قیمت 
import sys

def CalcUpDownPersents(value, percent):
    return (price * (100 - percent)/100, price * (100 + percent)/100)

print()
print('Calculate Persents(5, 10, 20) For Stock Price ')
print('==============================================')
flag = True
while flag:
    try:
        price = float(input("Enter a price (or zero for exit): "))
        if price == 0.0:
            break
        print('+----------+----------+----------+')
        print('| {0:^8s} | {1:^8s} | {2:^8s} |'.format('Persent','Down', 'UP'))
        print('+----------+----------+----------+')
        for i in [5, 10, 20]:
            down, up = CalcUpDownPersents(price, i)
            print('| {0:^8d} | {1:^8.1f} | {2:^8.1f} |'.format(i, down, up))
            print('+----------+----------+----------+')
        print()
    except ValueError as err:
        print("ValueError: {0}".format(err))
        print("Please enter a valid price. ")
    except:
        print("Unexpected error:", sys.exc_info()[0])
        flag = False
        pass

print()
print("Goodbye.")
print()
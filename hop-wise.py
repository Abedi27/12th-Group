# hop --> 3
# wise --> 7
# hop-wise --> 21
hop = int(input('enter number hop:'))
wise = int(input('enter number wise:'))
for num in range(1, 100):
    if hop < wise:
        number = 'hop-wise' if not num % (hop * wise) else 'hop' if not num % hop else 'wise' if not num % wise else str(num)
    else:
        number = 'hop-wise' if not num % (hop * wise) else 'wise' if not num % wise else 'hop' if not num % hop else str(num)
        print(number)
# Hop Wise whit range
for b in range(1, 100):
    print ('Hop-wise' if  (b in range(0, 100, hop * wise)) else 'hop' if (b in range(0, 100, hop )) else 'wise' if  (b in range(0, 100, wise)) else str(b))
# print rivers alphabet
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for char in range(len(alphabet)):
    print(alphabet[-(char+1)])
# find primer number


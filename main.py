sum = ''

while True:
    type = input('Type? +-x/ ')
    if type == '+':
        try:
            if sum == '':

                num = int(input('Num? '))
                num2 = int(input('Num? '))
                sum = num+num2
                print(num+num2)
            else:
                sum2 = int(input('Num? '))
                sum = sum + sum2
                print(sum)

        except:
            print('Error')


    if type == '-':
        try:
            if sum == '':

                num = int(input('Num? '))
                num2 = int(input('Num? '))
                sum = num - num2
                print(num - num2)
            else:
                sum2 = int(input('Num? '))
                sum = sum - sum2
                print(sum)

        except:
            print('Error occurred')

    if type == 'x':
        try:
            if sum == '':

                num = int(input('Num? '))
                num2 = int(input('Num? '))
                sum = num * num2
                print(num * num2)
            else:
                sum2 = int(input('Num? '))
                sum = sum * sum2
                print(sum)

        except:
            print('Error occurred')
    if type == '/':
        try:
            if sum == '':

                num = int(input('Num? '))
                num2 = int(input('Num? '))
                sum = num / num2
                print(num / num2)
            else:
                sum2 = int(input('Num? '))
                sum = sum / sum2
                print(sum)

        except:
            print('Error occurred (Possibly divided by zero)')

    if type == 'stop':
        yn = input('Are you sure? Y/N ')
        if yn == 'Y' or yn == 'y':
            print('Shutting down')
            break
        if yn == 'N' or yn == 'n':
            print('Canceled')

    if type == 'restart':
        yn = input('Are you sure? Y/N ')
        if yn == 'Y' or yn == 'y':
            print('Resetting sum')
            sum = ''
        if yn == 'N' or yn == 'n':
            print('Canceled')

print('Hi! Please choose one of these in your mind.')
print('[Apple, Tree, Flower, Elephant, Mobile Phone, Squirrel, Watermelon, Car]')
ask = input('Are you ready? (yes/no?): ')
if ask == 'no':
    print("Nice to see you, Bye.")
else:
    print("OK, Let's play!")   
    while True:
        a = str(input('Is that a fruit?'))
        if a == 'yes':
            b = str(input('Is that fits in the pocket?'))
            if b == 'yes':
                print('Apple')
                break
            elif b == 'no':
                print('Watermelon')
                break
        elif a == 'no':
            c = str(input('Can it be seen in the nature?'))
            if c == 'yes':
                d = str(input('Is that an animal?'))
                if d == 'yes':
                    e = str(input('Is that big?'))
                    if e == 'yes':
                        print('Elephant')
                        break
                    elif e == 'no':
                        print('Squirrel')
                        break
                elif d == 'no':
                    f = str(input('Is that tall?'))
                    if f == 'yes':
                        print('Tree')
                        break
                    elif f == 'no':
                        print('Flower')
                        break
            elif c == 'no':
                g = str(input('Is that a tool?'))
                if g == 'yes':
                    h = str(input('Can you hold it by hand?'))
                    if h == 'yes':
                        print('Mobile Phone.')
                        break
                    elif h == 'no':
                        print('Car')
                        break
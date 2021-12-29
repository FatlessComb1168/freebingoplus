from random import randint;
from os import system;
array = [];
numbers = [];

b = True;
while b:
    print('Welcome to FreeBingo+!');
    print('0 - Generate bingo\n1 - Generate loto\n2 - Exit');

    a = input();

    if a == '0':
        system('cls');
        print('List of generated bingo maps:\n');

        for i in range(1, 11):
            while len(numbers) < 25:
                if len(numbers) == 12:
                    numbers.append(' * ');
                    continue;

                n = randint(1, 99);
                if n not in numbers:
                    if (len(numbers) + 1) % 5 == 0 and n < 10:
                        numbers.append(' ' + str(n) + '\n');
                    elif (len(numbers) + 1) % 5 == 0 and n >= 10:
                        numbers.append(str(n) + '\n');
                    elif n < 10:
                        numbers.append(' ' + str(n) + ' ');
                    else:
                        numbers.append(str(n) + ' ');
                
            print('Bingo #' + str(i) + ':');
            print('B  I  N  G  O');
            print(''.join(numbers));
            numbers = [];
        input();

    if a == '1':
        system('cls');
        print('List of generated loto maps:\n');

        for i in range(1, 11):
            while len(numbers) < 54:
                choice = randint(1, 20);
                if choice < 13:
                    n = randint(1, 99);
                    if n not in numbers:
                        if (len(numbers) + 1) % 9 == 0 and n < 10:
                            numbers.append(' ' + str(n) + '\n');
                        elif (len(numbers) + 1) % 9 == 0 and n >= 10:
                            numbers.append(str(n) + '\n');
                        elif n < 10:
                            numbers.append(' ' + str(n) + ' ');
                        else:
                            numbers.append(str(n) + ' ');
                    if len(numbers) == 27:
                        numbers.append('-' * 26 + '\n');

                else:
                    if (len(numbers) + 1) % 9 == 0:
                        numbers.append('  \n');
                    else:
                        numbers.append('   ');
                    if len(numbers) == 27:
                        numbers.append('-' * 26 + '\n');
            
            print('Loto #' + str(i) + ':');
            print('-' * 26);
            print(''.join(numbers)[0:-1]);
            print('-' * 26 + '\n');
            numbers = [];
        input();
    
    if a == '2':
        b = False;
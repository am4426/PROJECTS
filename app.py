started = False
while True:
    command = input('command: ')
    if command.upper() == 'HELP':
            print('''start-start the car
stop - stop the car
quit - to exit''')
    elif command.upper() == 'START':
        if started:
            print('CAR IS ALREADY STARTED')
        else:
            started = True
            print('CAR STARTED...READY TO GO!')
    elif command.upper() == 'STOP':
        if not started:
            print('CAR IS ALREADY STOPPED')
        else:
             started = False
             print('CAR IS STOPPED')
    elif command.upper() == 'QUIT':
            break
    else:
                        print("I DON'T UNDERSTAND THAT....")
speed = int(input('Enter your average speed: '))
average_speed = int(input('Average Speed: '))
points = (speed - average_speed)/5

if speed < average_speed:
    print('OK')
elif speed == average_speed:
    print('OK')
if points > 12:
    print('Demerit:' + str(points))
else:
    print('Time to go to Jail')

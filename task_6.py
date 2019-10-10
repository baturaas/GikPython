daily_distance = float(input('Enter starting distance: '))
total_distance = float(input('Enter final distance: '))
distance = float(daily_distance)
i = 1
while True:
    print(f'Result per day {i},{daily_distance:.3f},{distance:.3f}')
    if distance < total_distance:
        distance = distance + daily_distance
        daily_distance = daily_distance * 1.1
        i = i + 1

    else:
        print(f'Result will be achieved on {i} days')
        break

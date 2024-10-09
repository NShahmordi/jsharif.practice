input_working_hours = int(input('Enter your working hours:'))
input_hourly_rate = int(input('Enter your hourly rate of working hours:'))

if input_working_hours >= 40:
    print((40 * input_hourly_rate) + (((input_working_hours - 40) * 1.5* input_hourly_rate)))
else:
    print(input_working_hours * input_hourly_rate)
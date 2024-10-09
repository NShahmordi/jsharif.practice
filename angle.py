def time_angle(hour_number:int, min_number:int,result_angle=0):
    if hour_number > 24:
        raise ValueError('The number of hour is out of range.')
    if min_number > 60:
        raise ValueError('The number of minute is out of range.')

    if hour_number > 13:
        hour_number = 24 - hour_number
    min_angle, hour_angle = min_number * 6, hour_number * 30
    
    result_angle = abs(hour_angle - min_angle)
    if abs(360 - result_angle) > result_angle:
        return result_angle
    else:
        return abs(360 - result_angle)
time = time_angle(9,00)        
print(time)
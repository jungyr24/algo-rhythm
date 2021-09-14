import datetime
import math

def str_to_time(in_time, out_time):
    in_h, in_m = in_time.split(":")
    out_h, out_m = out_time.split(":")
    time_1 = datetime.timedelta(hours=int(in_h) , minutes=int(in_m))
    time_2 = datetime.timedelta(hours=int(out_h), minutes=int(out_m))
    h, m, s = str(time_2 - time_1).split(":")
    total_time = int(h)*60 + int(m)
    
    return total_time


def solution(fees, records):
    answer = []

    std_time, std_fee, per_time, per_fee = fees

    car_dict = {}
    for record in records:
        time, car_num, state = record.split(" ")
        if car_num not in car_dict.keys():
            car_dict[car_num] = [time]
        else:
            car_dict[car_num].append(time)
    car_dict = sorted(car_dict.items())

    for car, time_list in car_dict:
        if len(time_list) %2 == 1:
            time_list.append('23:59')
        total = 0
        while time_list:
            in_time = time_list.pop(0)
            out_time = time_list.pop(0)
            total += str_to_time(in_time, out_time)
        if total <= std_time:
            total_fee = std_fee
        else:
            total_fee = std_fee + math.ceil((total-std_time)/per_time) * per_fee
        answer.append(total_fee)

    

    return answer

print(solution([180, 5000, 10, 600], ["05:34 5961 IN", 
                                      "06:00 0000 IN", 
                                      "06:34 0000 OUT", 
                                      "07:59 5961 OUT", 
                                      "07:59 0148 IN", 
                                      "18:59 0000 IN", 
                                      "19:09 0148 OUT", 
                                      "22:59 5961 IN", 
                                      "23:00 5961 OUT"]))
print(solution([120, 0, 60, 591], ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]))
print(solution([1, 461, 1, 10], ["00:00 1234 IN"]))
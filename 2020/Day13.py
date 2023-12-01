from main import open_txt_by_line

contents = open_txt_by_line('inputD13.txt')

departure = int(contents[0])
buses = contents[1].split(',')


def bus_departures(departure_time, buses_list):
    timetable = []
    for bus in buses_list:
        bus_departure = 0
        if bus == 'x':
            continue
        else:
            while True:
                bus_departure += int(bus)
                if bus_departure >= departure_time:
                    break
            timetable.append((int(bus), bus_departure))
    fastest = min([timetable[i][1] for i in range(len(timetable))])

    def fastest_bus(fastest_time, table_of_times):
        for bus_n_time in table_of_times:
            if bus_n_time[1] == fastest_time:
                return bus_n_time
        pass

    return timetable, fastest_bus(fastest, timetable)


schedule = bus_departures(departure, buses)
print(schedule)
wait_time = schedule[1][1] - departure
print(wait_time)
print(wait_time * schedule[1][0])


def bus_by_minute(buses_list):
    buses_step = [(int(bus_id), step) for step, bus_id in enumerate(buses) if bus_id != 'x']
    t, iter = 0, 1
    for bus_id, step in buses_step:
        while (t + step) % bus_id != 0:
            t += iter
        iter *= bus_id
    return buses_step, t


print(bus_by_minute(buses))



# Not my code below

# print('#################################################')
# # read in aoc input and setup to vars from instructions
# time = int(open("inputD13_ex.txt").read().strip().split()[0])
# buses = open("inputD13_ex.txt").read().strip().split()[1].split(',')
# departures = {}
# print(buses)
# # part 1
# for bus in buses:
#     if bus != 'x':
#         bus_id = int(bus)
#         # calculate closest departure to your time for each bus
#         departing = (bus_id * (time // bus_id)) + bus_id
#         departures[departing] = bus_id
#
# # calculate the wait for the earliest (min) departing bus
# wait = min(departures) - time
# print(f'Part 1: {wait * departures[min(departures)]}')
#
# # part 2
# t, step = 0, 1
#
# # grab all bus id's and time offset
# p2 = [(int(i), j) for j, i in enumerate(buses) if i != 'x']
# print(p2)
#
# # iterate through buses
# for bus_id, mins in p2:
#     # check to see if bus is departing at current time
#     while (t + mins) % bus_id != 0:
#         t += step
#     # increase step multiple to find next min for next bus
#     step *= bus_id
#
# print(f'Part 2: {t}')
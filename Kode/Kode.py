import numpy as np
import csv
#Defining some variables
voltageoutput=3.3
average_hold_file_names = []
average_release_file_names = []
Resistances = [3300, 3300, 120, 120, 120, 120, 120]
#Making a list for the names of the files
for n in range(1,8):
    average_release_file_names.append("Malinger\D" + str(n) + "_opp.csv")
    average_hold_file_names.append("Malinger\D" + str(n) + "_ned.csv")

#Caluclates the average voltage from each of the csv files and returns a list of these averages
def average(files1):
    list_of_average=[]

    for n in range(7):
        with open(files1[n], 'r') as file:
            data=csv.reader(file)
            spenninger=[]
            for rad in data:
                spenninger.append(float(rad[1]))
            average=np.mean(spenninger)
            list_of_average.append(average)
    return list_of_average
average_hold= average(average_hold_file_names)
average_release=average(average_release_file_names)

#calculates the power usage of each of the situation, in which the dice shows the number 1-6
def Number_power(list):
    Number_power =[]
    Number_power.append(list[6])
    Number_power.append(list[0] + list[5])
    Number_power.append(list[0] + list[6] + list[5])
    Number_power.append(list[0] + list[1] + list[4] + list[5])
    Number_power.append(list[0] + list[1] + list[4] + list[5] + list[6])
    Number_power.append(list[0] + list[1] + list[2] + list[3] + list[4] + list[5])
    return Number_power



power_hold = []
power_release = []

#Calucates the power when the button is pressed, and when it's not pressed.
for n in range(7):
    power_hold.append(average_hold[n]/Resistances[n]*voltageoutput)
    power_release.append(average_release[n]/Resistances[n]*voltageoutput)

Power_for_each_number=Number_power(power_release)


# print('Voltage while Released [V]:')
# for n in range(7):
#     print(f'D{n+1}: {average_release[n]}')

# print('\nVoltage while Holding [V]:')
# for n in range(7):
#     print(f'D{n+1}: {average_hold[n]}')   

print('\nPower while released [W]:')
for n in range(7):
    print(f'D{n+1}: {power_release[n]}')

print('\nPower while holding [W]:')
for n in range(7):
    print(f'D{n+1}: {power_hold[n]}')


print('\nPower for each number [W]:')
for n in range(6):
    print(f'{n+1}: {Power_for_each_number[n]}')
print(f'Average: {sum(Power_for_each_number)/len(Power_for_each_number)}')

print(f'\nAverage power while holding [W]: \n{np.sum(power_hold)}')

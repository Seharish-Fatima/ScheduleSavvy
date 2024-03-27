import pandas as pd
import numpy as np
from collections import defaultdict

timetable = defaultdict(object)
classrooms = defaultdict(object)
slots = defaultdict(object)



monday_data = pd.read_csv('./timetables/monday.csv', skiprows=1)
tuesday_data = pd.read_csv('./timetables/tuesday.csv', skiprows=1)
wednesday_data = pd.read_csv('./timetables/wednesday.csv', skiprows=1)
thursday_data = pd.read_csv('./timetables/thursday.csv', skiprows=1)
friday_data = pd.read_csv('./timetables/friday.csv', skiprows=1)

# print(monday_data)

def makeObject(slot, slot_data):

    slot_object = {
        'status' : 'empty',
        'section' : '',
        'course' : '',
        'teacher' : ''
    }

    data = slot_data.values[1:]
    print(len(data))
    print(data)

    # assign 'empty' to free slots
    for i in range(0, len(data)):
        if pd.isna(data[i]):
            print('empty')
            data[i] = 'empty'
    print(data)

    for value in data:
        value_data = value.split(' ')
        print(value_data)
        if value_data[0] != 'empty' :
            slot_object['course'] = value_data[0]
            slot_object['section'] = value_data[1]
            name = [x for x in value_data[2:] if x != '']
            slot_object['teacher'] = ' '.join(name)
            slot_object['status'] = 'occupied'
    print(slot_object)


def convertToDictionary(day_data):
    
    # Getting slots
    slots = day_data.iloc[0].size - 1
    classrooms = day_data['Slots'].values[2:]
    print(classrooms)
    print(slots)

    for i in range(1, slots+1):

        makeObject(i, day_data[str(i)])

def slotsAndClassrooms(day_data):

    classes_data = day_data['Slots'].values[2:]
    classes_data = classes_data[classes_data != 'LABS']
    # print(classes_data)

    # Getting classes
    for i in range(len(classes_data)):
        classrooms[i] = classes_data[i]
    print(classrooms)

    slots_data = day_data.iloc[0].values[1:]
    # print(slots_data)
    for i in range(len(slots_data)):
        slots[i] = slots_data[i]
    print(slots)

def main():
    convertToDictionary(monday_data)

if __name__ == "__main__":
    main()
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

def appendObject(slot, class_index, obj):
    print(slot, class_index, obj)


def makeObject(slot, slot_data):

    data = slot_data.values[2:]
    print(len(data))
    print(data)

    # assign 'empty' to free slots
    for i in range(0, len(data)):
        if pd.isna(data[i]):
            print('empty')
            data[i] = 'empty'
    # print(data)

    # Remove labs row
    # get location of 'LABs' row
    key_list=list(classrooms.keys())
    val_list=list(classrooms.values())
    ind=val_list.index('CS LAB-1 (50)')
    # print(key_list[ind])

    # remove 'LAB's' row
    data = np.delete(data, ind)

    print(data, len(data))


    # append class detail object
    # for key, value in enumerate(data):
    #     slot_object = {
    #         'status' : 'empty',
    #         'section' : '',
    #         'course' : '',
    #         'teacher' : ''
    #     }

    #     value_data = value.split(' ')
    #     print(key, value_data)
    #     if value_data[0] != 'empty' :
    #         slot_object['course'] = value_data[0]
    #         slot_object['section'] = value_data[1]
    #         name = [x for x in value_data[2:] if x != '']
    #         slot_object['teacher'] = ' '.join(name)
    #         slot_object['status'] = 'occupied'
        
    #     appendObject(slot, key, slot_object)


def convertToDictionary(day_data):
    
    # Getting slots
    slots = day_data.iloc[0].size - 1
    print(slots)

    for i in range(1, slots+1):
        makeObject(i, day_data[str(i)])
 
def setSlots(day_data):
    slots_data = day_data.iloc[0].values[1:]
    # print(slots_data)
    for i in range(len(slots_data)):
        slots[i] = slots_data[i]
    # print(slots)

def setClassrooms(day_data):
    classes_data = day_data['Slots'].values[2:]
    classes_data = classes_data[classes_data != 'LABS']
    # print(classes_data)

    # Getting classes
    for i in range(len(classes_data)):
        classrooms[i] = classes_data[i]
    print(classrooms)


def main():
    setSlots(monday_data)
    setClassrooms(monday_data)
    # convertToDictionary(monday_data)

if __name__ == "__main__":
    main()
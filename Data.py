import pandas as pd
import numpy as np

timetable = {}
classrooms = {}
slots = {}

monday_data = pd.read_csv('./timetables/monday.csv', skiprows=1)
tuesday_data = pd.read_csv('./timetables/tuesday.csv', skiprows=1)
wednesday_data = pd.read_csv('./timetables/wednesday.csv', skiprows=1)
thursday_data = pd.read_csv('./timetables/thursday.csv', skiprows=1)
friday_data = pd.read_csv('./timetables/friday.csv', skiprows=1)

days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
dataframes = []

def appendObject(slot, class_index, obj):
    # print(slot, classrooms[class_index], obj)
    
    if str(slot) not in timetable:
        timetable[str(slot)] = {}

    if obj['status'] == 'empty':
        if classrooms[class_index] not in timetable[str(slot)]:
            timetable[str(slot)][classrooms[class_index]] = obj  
        else:
            pass  
    else:
        if "LAB" in obj['section']:
            # print('lab found : ', obj)
            obj['section'] = obj['teacher'].split('\n')[0]
            obj['teacher'] = obj['teacher'].split('\n')[1].strip()
            obj['course'] = obj['course'] + '-LAB'
            # lab_key = (obj['course'], obj['section'])
            # labs_to_be_adjusted.append(lab_key)
            timetable[str(slot)][classrooms[class_index]] = obj
            adjust_labs(slot, class_index, obj)

        timetable[str(slot)][classrooms[class_index]] = obj

def adjust_labs(slot, class_index, obj):
    # print('adjust labs called')
    for i in range(1,3):
        if str(slot+i) not in timetable:
            print('slot not exists, created')
            timetable[str(slot+i)] = {}
            timetable[str(slot+i)][classrooms[class_index]] = obj
            # print(timetable[str(slot+i)][classrooms[class_index]])
        elif classrooms[class_index] not in timetable[str(slot+i)]:
            print('class not exists, created')
            timetable[str(slot+i)][classrooms[class_index]] = {}
            timetable[str(slot+i)][classrooms[class_index]] = obj
            # print(timetable[str(slot+i)][classrooms[class_index]])
        


def makeObject(slot, slot_data):
    data = slot_data.values[2:]

    # assign 'empty' to free slots
    for i in range(0, len(data)):
        if pd.isna(data[i]):
            data[i] = 'empty'

    # Remove labs row
    classes_list = list(classrooms.values())
    if 'CS LAB-1 (50)' in classes_list:
        ind = classes_list.index('CS LAB-1 (50)')
        data = np.delete(data, ind)

    # append class detail object
    for key, value in enumerate(data):
        slot_object = {
            'status': 'empty',
            'section': '',
            'course': '',
            'teacher': ''
        }

        value_data = value.split(' ')
        if value_data[0] != 'empty':
            slot_object['course'] = value_data[0]
            slot_object['section'] = value_data[1].strip()
            name = [x for x in value_data[2:] if x != '']
            slot_object['teacher'] = ' '.join(name)
            slot_object['status'] = 'occupied'
        appendObject(slot, key, slot_object)

def read_data():

    for index,day in enumerate(days):
        dataframes[index] = pd.read_csv('./timetables/monday.csv', skiprows=1)


def convertToDictionary(day_data):
    slots = day_data.iloc[0].size - 1

    # slots + 1
    for i in range(1, slots + 1):
        makeObject(i, day_data[str(i)])

def setSlots(day_data):
    slots_data = day_data.iloc[0].values[1:]

    for i in range(len(slots_data)):
        slots[i] = slots_data[i]

def setClassrooms(day_data):
    classes_data = day_data['Slots'].values[2:]
    classes_data = classes_data[classes_data != 'LABS']

    for i in range(len(classes_data)):
        classrooms[i] = classes_data[i]

def main():
    setSlots(monday_data)
    setClassrooms(monday_data)
    convertToDictionary(monday_data)
    print(timetable)

if __name__ == "__main__":
    main()

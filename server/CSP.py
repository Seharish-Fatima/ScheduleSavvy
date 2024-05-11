import numpy as np
import Data

class CSP():

    def __init__(self, student_tt, timetable, days) -> None:
        
        self.student_tt = student_tt
        self.locatedtt = []
        self.timetable = timetable
        self.days = days

    def getStudentTT(self):

        for day in self.days:
            print(f"\n{day}\n")
            for slot, classes in self.timetable[day].items():
                self.locateClasses(day, slot, classes)
    
    def locateClasses(self, day, slot_no, slots_data):
        print(f"\nlocate classes function for {day}, Slot {slot_no}:\n")
        # print(slots_data)
        for class_name, class_info in slots_data.items():
            status = class_info['status']
            section = class_info['section']
            course = class_info['course']
            teacher = class_info['teacher']
            class_tuple = (class_name, course, section, teacher)
            print(f"Class: {class_tuple}")
            for student_class in self.student_tt:
                print(student_class, class_tuple[1:])
                print(student_class == class_tuple[1:])
                if student_class == class_tuple[1:]:
                    print("Student's class found!")
                    self.locatedtt.append((day, slot_no) + class_tuple)

        print(self.locatedtt)            


student_tt = [
    ('SCD', 'BSE-5B', 'Naz Memon'), 
    ('FSPM', 'BSE-7A', 'Iqra Fahad'), 
    ('TBW', 'BAI-7A', 'Sameera Sultan'), 
    ('IS', 'BCS-7D', 'Dr. Aqsa Aslam'), 
    ('PPIT', 'BCS-7D', 'Shaharbano'), 
    ]
# student_tt = [
#     # ('BSE-5B', 'SCD', 'Naz Memon'), 
#     # ('FSPM', 'BSE-7A', 'Iqra Fahad'), 
#     # ('TBW', 'BAI-7A', 'Sameera Sultan'), 
#     # ('IS', 'BCS-7D', 'Dr. Aqsa Aslam'), 
#     ('PPIT', 'BCS-7D', 'Shaharbano'), 
#     ]

days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
timetable = Data.getData()

csp = CSP(student_tt, timetable, days)
csp.getStudentTT()
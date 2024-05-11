import numpy as np
from collections import Counter
import Data


class CSP():

    def __init__(self, student_tt, timetable, days) -> None:
        
        self.student_tt = student_tt
        self.locatedtt = []
        self.timetable = timetable
        self.days = days
        self.clashesClasses = []
        self.clash_counts = {}
        self.clash_slots = {}
        self.resolved_courses = {}

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

    def countClashes(self):


        for day in self.days:
            self.clash_counts[day] = 0
            self.clash_slots[day] = []

            slots = [class_info[1] for class_info in self.locatedtt if class_info[0] == day]
            print(slots)
            slot_counts = Counter(slots)
            for slot, count in slot_counts.items():
                if count > 1:
                    self.clash_counts[day] += count - 1
                    self.clash_slots[day].append(slot)

        
        print(self.clash_counts, self.clash_slots)

        # return clash_counts, clash_slots
    
    def resolvedClasses(self):
        
        print('resolving clashes')
        # Iterate over the clash slots for each day
        for day, clash_slots in self.clash_slots.items():
            for slot in clash_slots:
                # Filter located classes for the current day and slot
                classes_in_slot = [class_info for class_info in self.locatedtt if class_info[0] == day and class_info[1] == slot]
                
                # Check if there are clashes in this slot
                if len(classes_in_slot) > 1:
                    for class_info in classes_in_slot:
                        class_tuple = class_info[0:2] + class_info[2:]
                        # Check if this class has already been clashed
                        if class_tuple not in self.resolved_courses:
                            self.resolved_courses[class_tuple] = []
                        # Append the clashed slot number to the list for this course
                        self.resolved_courses[class_tuple].append(slot)

        # Print or handle the clashed courses with their clashed slot numbers
        print('Clashed Courses with Clashed Slot Numbers:')
        for course, slots in self.resolved_courses.items():
            print(f'{course}: {slots}')



    def locateClashes(self):
        
        print('locating clashes')           
        print('counting no of clashes')    
        print('no of clashes are : ', self.countClashes())       


student_tt = [
    ('SCD', 'BSE-5B', 'Naz Memon'), 
    ('FSPM', 'BSE-7A', 'Iqra Fahad'), 
    ('TBW', 'BAI-7A', 'Sameera Sultan'), 
    ('IS', 'BCS-7D', 'Dr. Aqsa Aslam'), 
    ('PPIT', 'BCS-7D', 'Shaharbano'), 
    ('DS-LAB', 'BCS-3A', 'Safia Baloch'), 
    ('PF-LAB', 'BCY-1B', 'Mahnoor Javed'), 
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
csp.locateClashes()
csp.countClashes()
csp.resolvedClasses()
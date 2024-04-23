import streamlit as st
from typing import List, Tuple
from ortools.sat.python import cp_model

# Define the CSP model
model = cp_model.CpModel()


def generate_timetable(courses: List[str]):
    # Define variables and domains
    course_variables = {}
    for course in courses:
        course_variables[course] = []
        for day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']:
            for slot in range(1, 9):  # Assuming 8 time slots per day
                var_name = f"{course}_{day}_{slot}"
                course_variables[course].append(model.NewIntVar(0, 1, var_name))

    # Define constraints
    for day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']:
        for slot in range(1, 9):  # Assuming 8 time slots per day
            courses_in_slot = []
            for course in courses:
                courses_in_slot.append(course_variables[course][(slot - 1) + (8 * ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'].index(day))])
            model.Add(sum(courses_in_slot) <= 1)

    # Solve the CSP
    solver = cp_model.CpSolver()
    status = solver.Solve(model)
    
    # Print the timetable
    timetable = {}
    if status == cp_model.OPTIMAL:
        for course in courses:
            timetable[course] = []
            for day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']:
                for slot in range(1, 9):  # Assuming 8 time slots per day
                    var_index = (slot - 1) + (8 * ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'].index(day))
                    if solver.Value(course_variables[course][var_index]) == 1:
                        timetable[course].append((day, slot))
    else:
        st.error("No solution found!")

    return timetable

# Streamlit app
st.title("Course Timetable Generator")

# Get user input for courses
num_courses = st.number_input("Enter the number of courses:", min_value=1, max_value=10, value=5, step=1)
courses = []
for i in range(num_courses):
    course_name = st.text_input(f"Enter course {i+1} name:")
    courses.append(course_name.strip())

# Generate timetable button
if st.button("Generate Timetable"):
    timetable = generate_timetable(courses)
    st.success("Timetable generated successfully!")
    st.write(timetable)

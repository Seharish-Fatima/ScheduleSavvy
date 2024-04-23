import streamlit as st
import pandas as pd


# Read CSV file
@st.cache
def load_data(file_path):
    return pd.read_csv(file_path)


# Load data
df = load_data('Week.csv')

# Title and introduction
st.title('TimeTable Generator')
st.header('FALL 2023 Version 1')
st.markdown('This app allows you to generate a timetable.')

# Checkboxes for selecting courses
courses = []
for i in range(1, 6):
    course = st.selectbox(f'Course {i}', ['Please Select a Course.'] + df.iloc[:, i].dropna().tolist())
    courses.append(course)

# Checkbox to toggle all sections by default
if st.checkbox('Check All Sections by Default?'):
    selected_courses = [course for course in courses if course != 'Please Select a Course.']
    default_sections = df[df.isin(selected_courses).any(axis=1)].index.tolist()
else:
    default_sections = None

# Table for selecting time slots
st.subheader('Select Time Slots')
selected_time_slots = st.multiselect('Time Slots', df.columns[1:], default=default_sections)

# Button to generate timetable
if st.button('GENERATE'):
    # Filter selected rows and columns
    timetable = df[df.columns[0]].copy()
    for time_slot in selected_time_slots:
        timetable = timetable + '\n' + df[time_slot].fillna('')

    # Display timetable
    st.subheader('TimeTable')
    st.write(timetable)

# Instructions link
st.markdown('or see [instructions](Instructions.html)')

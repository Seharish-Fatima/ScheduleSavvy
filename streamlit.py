import streamlit as st
import pandas as pd


@st.cache
def load_data(file_path):
    return pd.read_csv(file_path)


df = load_data('Data.js')

st.title('TimeTable Generator')
st.header('FALL 2023 Version 1')
st.markdown('This app allows you to generate a timetable.')

courses = []
for i in range(1, 6):
    course = st.selectbox(f'Course {i}', ['Please Select a Course.'] + df.iloc[:, i].dropna().tolist())
    courses.append(course)

if st.checkbox('Check All Sections by Default?'):
    selected_courses = [course for course in courses if course != 'Please Select a Course.']
    default_sections = df[df.isin(selected_courses).any(axis=1)].index.tolist()
else:
    default_sections = None

if st.button('GENERATE'):
    timetable = df[df.columns[0]].copy()
    for time_slot in selected_time_slots:
        timetable = timetable + '\n' + df[time_slot].fillna('')

    st.subheader('TimeTable')
    st.write(timetable)


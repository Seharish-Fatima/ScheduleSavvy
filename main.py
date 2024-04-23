import pandas as pd

df = pd.read_csv('Week.csv')
print(df.head())
Day = 0
Periods = []
for row, val in df.iterrows():
    if pd.isnull(val.iloc[1]):
        Day += 1
    else:
        Venue = val.iloc[1]
        for col, period in enumerate(val[2:], start=2):
            if pd.notnull(period):
                Section = period.split("(")[-1].split(")")[0]
                Course = period.split("(")[0].strip()
                stime = (col - 2) * 60
                etime = stime + 60
                Periods.append([Course, Section, str(stime - 40), str(etime - 40), str(Day), Venue])


Periods.sort(key=lambda x: x[0])

with open("Data.js", "w") as file:
    file.write("Courses = [\n")
    for P in Periods:
        file.write('\t["' + '","'.join(P) + '"],\n')
    file.write("]\n")

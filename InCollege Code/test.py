from personalProfile import *
from menus import viewProfile
x = getExperienceInfo("test")
x = x.fetchall()
# print (x[0][0])
# print(len(x))
for d in x: # iterate through all the jobs from the database
    print("\t" + d[2] +
            "\n\t" + d[3] +
            "\n\tStart: " + d[4] +
            "\n\tEnd: " + d[5] +
            "\n\t" + d[6] +
            "\n\t" + d[7] + "\n")
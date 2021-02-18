import sys
import os

import os


directory = str(sys.argv[1])

index_1=[0.01,
            0.0230506,
            0.0531329,
            0.122474,
            0.282311,
            0.650743,
            1.5]
index_2=[0.0005,
            0.00122655,
            0.00300884,
            0.00738098,
            0.0181063,
            0.0444164,
            0.108958]
fp2 = open('timing', 'w')
fp2.write("{\n")
for filename in os.listdir(directory):
    fp = open(str(directory+"/"+filename),'r')
    if filename.endswith(".txt"):
        fnm=os.path.splitext(filename)[0]
        
        fp2.write("\t\""+fnm+",del_1_7_7\""+": {\n")
        fp2.write("\t\t\"index_1\""+": [\n")
        
        for i in index_1:
            fp2.write("\t\t\t"+str(i)+",")
        fp2.write("\t\t],")

        for i in index_2:
            fp2.write("\t\t\t"+str(i)+",")
        fp2.write("    \"index_2\""+": [\n")
        fp2.write("\"values\": [")
        fp2.write("\t\t\t\t[")
        line = fp.readline()
        while line:
            if "input_delay" and "0.01n" in line:
                continue
            elif "input_delay" in line:
                fp2.write("\t\t\t],")
                continue
            else :
                fp2.write("\t\t\t\t"+line+",\n")
            line = fp.readline()

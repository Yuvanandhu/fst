'''#write
student_details="reg_no:cb22,name:yjn,class:IIbsc"
fp=open("stud_details.txt","w")
fp.write(student_details)
fp.close()

#read
fp=open("stud_details.txt","r")
print(fp.read())

#append
fp=open("stud_details.txt","a")
student_details="reg_no:cb21,name:vk,class:IIbsc"
fp.write("\n"+student_details)

#rename
import os
Old_name=r"D:\22USCE2042\stud_details.txt"
New_name=r"D:\22USCE2042\student_details.txt"
os.rename(Old_name,New_name)
print("done")'''

#remove
import os
os.remove(r"D:\22USCE2042\student_details.txt")
print("come")

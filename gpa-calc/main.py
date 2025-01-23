

numCourses = int(input("How many courses are you taking? "))

course_inputs = 0



A_counts = int(input("how many As did you make? : ")) * 4.0
Bplus_counts = int(input("how many B+s did you make? : ")) * 3.5
B_counts = int(input("how many Bs did you make? : ")) * 3.0
Cplus_counts = int(input("how many C+s did you make? : ")) * 2.5
C_counts = int(input("how many Cs did you make? : ")) * 2.0
Dplus_counts = int(input("how many D+s did you make? : ")) * 1.5
D_counts = int(input("how many Ds did you make? : ")) * 1.0
E_counts = int(input("how many E did you make? : ")) * 0.5
F_counts = int(input("how many Fs did you make? : ")) * 0


GPA = sum([A_counts, Bplus_counts, B_counts, Cplus_counts, C_counts, Dplus_counts, D_counts, E_counts, F_counts]) / numCourses

print(f"Your GPA is: {GPA:.2f}")
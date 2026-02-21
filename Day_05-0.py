"""The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students.
Print the average of the marks array for the student name provided, showing 2 places after the decimal."""

if __name__ == '__main__':
    n = int(input("No of students:"))
    student_marks = {}
    for i in range(n):
        name, *line = input("Enter name and marks of the student").split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input("student's name whose avg marks is to be calc.:")
    j=0
    tot=0
    try:
        for k in student_marks[query_name]:
            j=j+1
            tot+=k
        avg=tot/j
        print(f"{avg:.2f}")
    except:
        print(f"Please enter marks for {query_name}")
    

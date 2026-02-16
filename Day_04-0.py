"""Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line."""

#sorted sorts a list or set and returns a list of sorted elements

records=[]
lst=[]
names=[]
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        lst.append(score)
        records.append([name,score])
    sor_lst=sorted(set(lst))
    s_low=sor_lst[1]
    for i in records:
        if i[1]==s_low:
            names.append(i[0])
    sor_names=sorted(names)
    for i in sor_names:
        print(i)
        

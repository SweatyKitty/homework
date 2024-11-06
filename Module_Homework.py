grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]#содержит списки оценок для каждого ученика в алфавитном порядке.
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}#содержит неупорядоченную последовательность имён
statistic_result={}
print(type(grades))
students=list(students)
students=sorted(students)
print(students)
i=0

while i!=int(len(students)):#Использовал циклы потому что так можно написать программу
    b=len(grades[i])-1# которая считает средний бал независимо от количства учеников
    a=0#               и оценок в первоначальном списке
    while b>-1:
        a=a+grades[i][b]
        b=b-1
    b=round(a/len(grades[i]),2)
    a=str(students[i])
    statistic_result.update({a:b})
    i=i+1
print(statistic_result)
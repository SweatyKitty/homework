grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]#содержит списки оценок для каждого ученика в алфавитном порядке.
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}#содержит неупорядоченную последовательность имён
statistic_result={}
print(type(grades))
students=tuple(students)
print(students)
i=0

while i!=int(len(students)):
    b=len(grades[i])-1
    a=0
    while b>-1:
        a=a+grades[i][b]
        b=b-1
    b=a/len(grades[i])
    a=str(students[i])
    statistic_result.update({a:b})
    i=i+1
print(statistic_result)
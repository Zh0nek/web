if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input() 
    summa = 0
    count = 0
    ans = 0
    for i in student_marks.keys():
        if i == query_name:
            for i in student_marks[query_name]:
                summa = summa + i
                count = count + 1
    ans = float(summa/count)
    print("%.2f" % ans)
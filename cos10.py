def solution(data):
    total =sum(data)
    average = total/ len(data) #한줄변경하여 제대로 돌아가도록 
    cnt = 0
    for d in data:
        if d > average:
            cnt+= 1
    return cnt 

data1 = [1,2,3,4,5,6,7,8,9,10]
ret1 = solution(data1)


print(ret1)
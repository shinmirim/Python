#문제 1

'''def solution(shirt_size):
    answer=[]
    #for _ in range(6):
        #answer.append(0)  
    answer=[0 for _ in range(6)] #answer=[0]*6 / 모두 0으로 초기화 시킨다. 
    
    for i in shirt_size:
        if i == "XS":
            answer[0]+=1
        elif i == "S":
            answer[1]+=1
        elif i == "M":
            answer[2]+=1
        elif i == "L":
            answer[3]+=1
        elif i == "XL":
            answer[4]+=1
        elif i == "XXL":
            answer[5]+=1
    
    return answer


shirt_size=["XS","S","M","L","XL","XXL"]
ret = solution(shirt_size)

print(ret)'''




'''for i in shirt_size:
    for j in range(6):
        if i == answer[j]:
            answer[j]+=1
return answer'''
#j는 다 0인데 ?



#문제 2
'''def solution(price, grade):
    answer = 0
    if grade == "S":
        answer = price - price*0.05
    elif grade == "G":
        answer = price - price*0.1
    elif grade == "V":
        answer = price - price*0.15 
    return answer

    price1 = 2500
    grade1 =  "V"
    ret1 = solution(price1, grade1)'''





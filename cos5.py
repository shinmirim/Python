'''def solution(arr):
    left,right =0, len(arr)-1
    print(left,right)
    while True: #for in in range(len(arr)/2) #left<ringht
        arr[left], arr[right] = arr[right],arr[left]
        left +=1
        right-=1
    return arr 


arr= [1,2,3,4]
ret =solution(arr)

print("Solution: return value of the function is",ret,"입니다")'''

#그렇다면 트루 일때는 언제 빠져나오나 ?


def solution(number):
    count = 0
    for i in range(1, number+1):
        current = i
        temp = count
        while current !=0:
            if current % 10 ==3 or current % 10==6 or current %10 == 9 :
                count += 1
                print("pair", end="")
            current = current//10 # while빠져나감
        if temp == count:
            print(i, end=" ")
        print(" ",end = '')
    print("")
    return count 

number =  40
ret = solution(number)


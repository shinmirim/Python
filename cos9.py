from numpy import char, character


def solution(characters):
    result =""
    result += characters[0]
    for i in range(1,len(characters)): #그래야 인덱스 0과 1을 비교하면서 시작하게 된다.
        if characters[i- 1] !=  characters[i]:
            result += characters[i]
    return result

characters = "senteeeencccccceeee"
ret = solution(characters)

print(ret)



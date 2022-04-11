#이상형이 뭐예요? 제작하기 

# 첫번째 방법

'''total_dictionary = {}
while True:
    question = input("질문을 입력해주세요 : ")
    if question == "q":
        break
    else:
        total_dictionary[question] = "" #value값은 아직 없이 나옴

for i in total_dictionary:
    print(i)
    answer = input("답변을 입력해주세요 : ")
    total_dictionary[i] = answer


print(total_dictionary)'''

#두번째 방법
total_list = [] # 리스트로

while True:
    question = input("질문을 입력해주세요 : ")
    if question == "q":
        break
    else:
        total_list.append({"질문" : question, "답변" : ""})#온전한 딕셔너릴ㄹ 만들고 리스트에 추가

for i in total_list:
    print(i["질문"])
    answer = input("답변을 입력해주세요 : ")
    i["답변"] = answer
print(total_list)        
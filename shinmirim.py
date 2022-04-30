
import random

def qna(name):
    print("=====안녕하세요 ",name,"님, 당신은 집순이일까요 ?=====")
    print("=====모든 질문의 대답을 네, 아니오로 답변해주세요=====")
    new_qna = create_question()
    qna_num = int(input("받을 질문의 개수를 입력해주세요 (최대 7개 가능): "))
    count =0
    choice_qna = list()
    for i in range(qna_num) :
        key = random.choice(list(new_qna.keys()))
        while key in choice_qna:
            key = random.choice(list(new_qna.keys()))
        choice_qna.append(key)
        print(key)
        new_qna[key] = input("답변 : ")
        if new_qna.get(key) == "네":
            count+=1
    
    percent = count/qna_num *100
    return percent

def your_type(percent):
    if(percent>=75):
        print("당신은 집순이입니다.")
    elif(percent>=50):
        print("당신은 집을 조금 더 좋아하네요.")
    elif(percent>=25):
        print("당신은 밖을 조금 더 좋아하네요.")
    else:
        print("당신은 바깥순이입니다.")

def create_question():
    qna = {"집밖에 나가는 것 자체가 스케줄?":""}
    qna["불금에는 북적대는 곳보단 집이지?"] = ""
    qna["휴대폰만 있어도 안 심심한가요?"] = ""
    qna["카톡, 문자 알림을 잘 확인하지 않나요?"] = ""
    qna["아무 생각이 없다. 왜냐하면 아무 생각이 없기 때문이다 라고 자주 느끼나요?"] = ""
    qna["당신은 배달앱 VIP인가요?"] = ""
    qna["친구와의 약속이 갑작스레 파토났을 때 아쉽다는 생각보다 오예!라는 생각이 더 자주 드나요?"] = ""
    return qna


        

name = input("당신의 이름은? ")
percent = qna(name)
your_type(percent)

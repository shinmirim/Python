from argparse import ONE_OR_MORE


e_dict={"one":"하나","two":"둘","three":"셋","four":"넷","five":"다섯"}

word = input("영어숫자입력:")

if word in e_dict:
  print(e_dict[word])
else:
    ansewer = input("사전에 없는 단어입니다. 추가할까요?[y/n]")

    if ansewer == "y":
        k_word = input("해당하는 한글단어를 입력해주세요")
        e_dict[word] = k_word
        print("추가되었습니다.")
        print(e_dict)
    elif ansewer == "n":
        print("다시 시도해보세요")

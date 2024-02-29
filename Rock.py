# # 1. 플레이어와 컴퓨터가 참여하는 가위바위보 게임을 만드세요.
# # 2. 게임은 다음 순서로 진행됩니다.
# #     - 플레이어가 가위, 바위, 보 중 하나를 입력합니다.
# #     - 컴퓨터도 무작위로 가위, 바위, 보 중 하나를 선택합니다.
# #     - 플레이어와 컴퓨터의 선택을 비교하여 승패를 판정합니다.
# #     - 결과를 출력하여 플레이어가 이겼는지, 컴퓨터가 이겼는지, 비겼는지를 알려줍니다.
# #     - 게임을 반복하거나 종료할 수 있는 기능을 추가하세요.
# # ---------------------------------------------
# # - 사용자의 입력값을 ‘가위 바위 보’로 제한할 수 있는가
# # - 컴퓨터가 랜덤으로 ‘가위 바위 보’를 선택하게 할 수 있는가
# # - 다중 if 문으로 승패를 비교할 수 있는가
# # - while문을 이용해서 경기를 반복시키고 통계를 만들 수 있는가

# import random
# def rock_game():
#     a = ['가위', '바위', '보']
#     b = random.choice(a)
#     print(b)

#     while True:
#         # input("안내문 진 거 가위바위보!: ") ## input을 프린트하고, 터미널에 입력한 건 값이 되지 않고 날라가 버린다. 쉽게 말해 값을 담을 그릇을 같이 설정해줘야한다!
#         c = input("안내문 진 거 가위바위보!: ")
#         if c == b : #input이 랜덤이랑 같을 경우
#             print('비겼음 ㅋ')
#             break


def rock_game():
    import random
    a = ['가위', '바위', '보']
    a = random.choice(a)
    # print(a)
    while True:
        user = input("안내문 진 거 가위바위보!: ")
        if user == a:  # input이 랜덤이랑 같을 경우
            print('비겼음 ㅋ')
            break
        elif (user == '가위' and a == '바위') or (user == '바위' and a == '보') or (user == '보' and a == '가위'):
            print('뭐함? 졌음 ㅋ')
            break
        elif (user == '가위' and a == '보') or (user == '바위' and a == '가위') or (user == '보' and a == '바위'):
            print('올ㅋ 이겼네')
            break
        else:
            print('뭐하3? 바르게 입력해줘')


def reply_rock():
    while True:
        answer = input("다시할래? (ㅇㅇ/ㄴㄴ): ")  # 다시할래를 물어봄.
        if answer == 'ㅇㅇ':  # 응 이라고 대답하면
            rock_game()  # 게임을 다시 시작한다.
        elif answer == 'ㄴㄴ':
            print('게임을 종료합니다')
            
        elif answer != 'ㅇㅇ' and 'ㄴㄴ':  # 그렇지 않으면
            print('올바른 답을 입력하세요')
            break
            # 게임을 종료합니다를 출력한다.

        # 그리고 멈춘다. 와우! 브레이크의 중요성 ㅠㅎㅎㅎ
# 나는 사용자가 ㅇㅇ이나 ㄴㄴ 말고 다른 답을 입력할 경우 올바른 답을 입력하세요를 출력한 후 다시할래? 함수를
# 다시 호출하고 싶다. 그럼 어떻게 해야할까? 나의 시도 1. else에서


def rock_game_main():
    while True:  # 반복문
        rock_game()  # 게임함수 호출
        if not reply_rock():  # if문은 트루인 경우에만 작동한다.
            break  # 멈춘다.  어떤 상황에 브레이크가 나는 걸까나? 


rock_game_main()  # 함수호출!

# # or = 둘 중 하나여도 참
# # and = 둘다 참
# # if (input == '가위'and a == '바위') or (input == '가위'and a == '보') or (input == '바위'and a == '가위') or (input == '바위'and a == '보') or (input == '보'and a == '가위') or (input == '보'and a == '바위')
#     # 사용자: 가위 컴퓨터: 바위
#     # 사용자: 가위 컴퓨터: 보 -> 이김
#     # 사용자: 바위 컴퓨터: 가위 -> 이김
#     # 사용자: 바위 컴퓨터: 보
#     # 사용자: 보 컴퓨터: 가위
#     # 사용자: 보 컴퓨터: 바위 -> 이김

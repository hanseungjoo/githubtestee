# 1. **`Member`** 클래스와 **`Post`** 클래스를 정의하세요.
# 2. **`Member`** 클래스에는 다음과 같은 속성을 가지고 있어야 합니다.
#     - 회원 이름 (**`name`**)
#     - 회원 아이디 (**`username`**)
#     - 회원 비밀번호 (**`password`**)
# 3. **`Member`** 클래스에는 다음과 같은 메소드를 가지고 있어야 합니다.
#     - 회원 정보를 print해주는 `display` (회원이름과 아이디만 보여주고 비밀번호는 보여줘서는 안됩니다!)
# 4. **`Post`** 클래스에는 다음과 같은 속성을 가지고 있어야 합니다.
#     - 게시물 제목 (**`title`**)
#     - 게시물 내용 (**`content`**)
#     - 작성자 (**`author`**) : 회원의 `username` 이 저장되어야 함!
# 5. 회원 인스턴스를 세개 이상 만들고 `members` 라는 빈리스트에 append를 써서 저장해주세요
#     1. members 리스트를 돌면서 회원들의 이름을 모두 프린트 해주세요
# 6. 각각의 회원이 게시글을 세개 이상 작성하는 코드를 만들어주세요.(회원이 세명이명 총 9개 이상의 post 인스턴스가 만들어져야 합니다). 만들어진 게시글 인스턴스들은 posts 빈리스트에 append를 써서 저장해주세요
#     1. for 문을 돌면서 특정유저가 작성한 게시글의 제목을 모두 프린트 해주세요
#     2. for문을 돌면서 ‘특정 단어’가 content에 포함된 게시글의 제목을 모두 프린트 해주세요

class Member:
    def __init__(self, name, username, password):  # 회원 이름, 이게 속성임
        self.name = name
        self.username = username
        self.password = password

    def display(self):  # 초기세팅된 붕어빵판을(멤버) 가지고 내가 원하는 메소드를(함수) 만든다.
        print(f'내이름{self.name}')

    def __repr__(self):
        return f'{self.name}, {self.username}, {self.password}'


# 멤버라는 붕어빵판을 불러온다. name값에 승주를 넣는다. =>어떤걸 갖다 쓸건지 한 번 정의 필요
user = Member('한나', '금쪽이', 1235)
user2 = Member('근영', '금쪽이2', 1245)
user3 = Member('승주', '금쪽이3', 1345)


# members 리스트를 돌면서 회원들의 이름을 모두 프린트 해주세요
Members = []
Members.append(user)
Members.append(user2)
Members.append(user3)

for member in Members:
    member.display()


class post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def text(self):
        print(f'제목:{self.title}')

    def word(self):
        print(f'{self.content}')

    def __repr__(self):
        return f'{self.title}, {self.content}, {self.author}'

#객체 = 인스턴스
user1_text1 = post('좋아하는 영화', '일단 나는 만화영화를 좋아한다. 미니언즈 같은..', '한나')
user1_text2 = post('좋아하는 드라마', '드라마는 잔잔한게 좋아. 멜로가체질같은..', '한나')
user1_text3 = post('좋아하는 음악', '음악은 신나는 음악이지! 펑키!', '한나')
user2_text1 = post('싫어하는 음식', '내가 볼 때 회는 맛이없어..', '근영')
user2_text2 = post('싫어하는 운동', '으 필라테스.. 으..', '근영')
user2_text3 = post('싫어하는 사람', '시간약속 안지키는 사람 제일 싫어', '근영')
user3_text1 = post('그저그런 말들', '다른 사람이 욕해도 난 아무렇지 않아', '승주')
user3_text2 = post('그저그런 동물', '사실 난 동물이 별로 귀엽지 않아', '승주')
user3_text3 = post('그저그런 옷들', '옷을 사입는 건 귀찮아.', '승주')


user_text = []
user_text.append(user1_text1)
user_text.append(user1_text2)
user_text.append(user1_text3)
user_text.append(user2_text1)
user_text.append(user2_text2)
user_text.append(user2_text3)
user_text.append(user3_text1)
user_text.append(user3_text2)
user_text.append(user3_text3)


for i in user_text:  # 유저 텍스트 안에서 반복을 한다.
    if i.author == user3.name:
        print(i.title)


# 2. for문을 돌면서 ‘특정 단어’가 content에 포함된 게시글의 제목을 모두 프린트 해주세요
for i in user_text:  # 유저 텍스트 안에서 반복을 한다.
    if '음악' in i.content: #if에도 in사용이 가능하다!!!
        print(i.title)

#변수는 소문자, 클래스명은 대문자로 하기로 파이썬 개발자들끼리 합의 봄! (카멜 케이스)
from flask import Flask
import random
import requests


app = Flask(__name__)

@app.route('/')
def home():
    return 'hello'


# 1. 주문서를 만들고, 
# 2. 해당 주문이 들어왔을 때 무엇을 할 지 정의

# 사용자가 우리에게 어떤 주문을 할지 @
@app.route('/name')
def name():
    return '이도현'


@app.route('/hello/<name>')

def hello(name):
    return f'hello {name}'


@app.route('/squaree/<num>')

def numnum(num):

    s=int(num)
    s*= s

    num=str(s)
    return f'square {num}'


@app.route('/square/<int:number>')
def square(number):

    #number를 제곱하여 반환
    #url에서 들어오는 숫자는 글자로 들어와요
    #1. 글자 number를 숫자로 변환   
    return str(number ** 2)


@app.route('/menu')
def menu():
    foods = ['바스버거', '대우식당', '진가와', '고갯마루']
    print(type(foods[0]))
    return random.choice(foods)


@app.route('/lottoo')
def lottoo():
   winner = [3, 5, 12, 13, 33, 39]
   a=random.sample(range(1, 47), 6)
   temp = [] 

   # 만약 6개가 모두 일치하면 
   # 1등
   for i in winner:
       if i not in a:
           temp.append(i)
   rank=len(temp)

   # 만약 5개가 일치하면 
   # 3등
   # 만약 4개가 일치하면
   # 4등
   # 만약 3개가 일치하면
   # 5등
   return str(sorted(a)) + str(rank)


@app.route('/lottoe')
def lottoe():
   winner = [3, 5, 12, 13, 33, 39]
   result=random.sample(range(1, 47), 6)
   for i in result:
       if i in winner:
           cnt += i
   
   rank='꽝'
   if cnt == 6:
       rank = "1등"
   elif cnt ==5:
       rank = "3등"
   elif cnt ==4:
       rank = "4등"
   elif cnt == 3:
       rank = "5등"
   # 만약 6개가 모두 일치하면 
   # 1등
   # 만약 5개가 일치하면 
   # 3등
   # 만약 4개가 일치하면
   # 4등
   # 만약 3개가 일치하면
   # 5등
  
   return str(sorted(result)) + str(rank)


@app.route('/lottoee')
def lottoee():
   winner = [3, 5, 12, 13, 33, 39]
   result=random.sample(range(1, 47), 6)
   winner = [3, 5, 12, 13, 14, 15]
   cnt=len(set(winner), 6)

   for i in result:
       if i in winner:
           cnt += i

   rank='꽝'

   if cnt == 6:
       rank = "1등"
   elif cnt ==5:
       rank = "3등"
   elif cnt ==4:
       rank = "4등"
   elif cnt == 3:
       rank = "5등"

   # 만약 6개가 모두 일치하면 
   # 1등
   # 만약 5개가 일치하면 
   # 3등
   # 만약 4개가 일치하면
   # 4등
   # 만약 3개가 일치하면
   # 5등
   return str(sorted(result)) + str(rank)

@app.route('/lotto')
def lotto():
    url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=873'

    #갖고왔으면 응답으로 받아라
    response = requests.get(url)
    response.text
    res_dict = response.json()

    # 1등 번호 6개가 담긴 result 라는 list를 출력.
    temp = []
    temp.append(res_dict['drwtNo1'])
    temp.append(res_dict['drwtNo2'])
    temp.append(res_dict['drwtNo3'])
    temp.append(res_dict['drwtNo4'])
    temp.append(res_dict['drwtNo5'])
    temp.append(res_dict['drwtNo6'])

    winner=temp
    result=random.sample(range(1, 47), 6)
   
    # for i in range(6):
    #      temp.append(res_dict['drwtNo{i+1}'])     i=0부터 시작한다. 
    # for i in range(1,7):
    #      temp.append(res_dict['drwtNo{i}'])     i=0부터 시작한다. 


    cnt=len(set(winner)&set(result))  

    rank='꽝'
    if cnt == 6:
        rank = "1등"
    elif cnt ==5:
        rank = "3등"
    elif cnt ==4:
        rank = "4등"
    elif cnt == 3:
        rank = "5등"

   # 만약 6개가 모두 일치하면 
   # 1등
   # 만약 5개가 일치하면 
   # 3등
   # 만약 4개가 일치하면
   # 4등s
   # 만약 3개가 일치하면
   # 5등
    return str(result)+rank




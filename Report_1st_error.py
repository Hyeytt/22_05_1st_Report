#과제를 맨처음에 vscode로 작성하고 최종적으로 저장하는 과정에서 항상 오류가 생겨 직접적인 과제제출과 관련은 없지만따로 올렸습니다
#문제 4번의 code는 아래 Report_1st_practice4에 따로 업로드했습니다 
#4번에 첫 문장으로 작성한 import turtle 부분이 저장을 하면 항상 1번의 부분에 끼어들어가는 오류가 발생합니다. 관련해서 질문드립니다

# 1 "환영합니다." , "파이썬의 세계에 오신 것을 환영합니다.", "파이썬은 강력합니다." 를 화면에 출력하는 프로그램을 작성하시오
import turtle
print("환영합니다.", "파이썬의 세계에 오신 것을 환영합니다.", "파이썬은 강력합니다.")
print("환영합니다.")
print("파이썬의 세계에 오신 것을 환영합니다.")
print("파이썬은 강력합니다.")

# 2 다음 프로그램의 실행 결과를 쓰시오
print("반갑습니다. 파이썬!")
print(2*3/10)
print("hello", "world", "!!!")

# 3 파이썬 쉘을 사용하여 한 주가 몇시간에 해당하는지를 계산해보자
print(7*24)

# 4 터틀 그래픽에서 거북이를 이동시켜서 다음과 같은 그림을 그려보자. foward(), right(), left() 함수만을 사용한다
t = turtle .Turtle()
t.shape("turtle")
t.forward(100)
t.left(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.left(90)
t.forward(100)
t.exitonclick()

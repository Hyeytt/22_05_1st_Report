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

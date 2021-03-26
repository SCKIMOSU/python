# enumerat는 리스트 원소의 순서 (index)와 값을 동시에 호출함
# 주로 for 문과 함께 사용

fruit = ['strawberry', 'grape', 'apple', 'mango', 'orange']
a = list(enumerate(fruit))

# enumerate(fruit) # fruit 리스트를 enumerate() 취하면
# 아래와 같이 객체가 된다
# Out[6]: <enumerate at 0x2889d0cc700>

# list(enumerate(fruit)) 와 같이 enumerate 객체를 list()화 시키면
# [(0, 'strawberry'), (1, 'grape'), (2, 'apple'), (3, 'mango'), (4, 'orange')]
# 형태의 리스트 원소의 순서 (index)와 값을 보여준다


a = [0,1,2,3,4]
for idx, val in enumerate(fruit):  # list a의 원소 0,1,2,3,4를 i라 하고
    print (idx, val)  # 매번 i를 출력시켜라

# 0 strawberry
# 1 grape
# 2 apple
# 3 mango
# 4 orange

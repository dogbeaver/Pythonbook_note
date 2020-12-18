name = input('학생 이름을 입력하세요:')
kor =int(input('국어 성적을 입력하세요:'))
eng = int(input('영어 성적을 입력하세요:'))
math = int(input('수학 성적을 입력하세요:'))
total = kor + eng + math
avg = total/3

print('이름:%s, 국어:%d, 영어:%d, 수학:%d, 평균:%.1f점' % (name, kor, eng, math, avg))



#Q2.6 주석문
'''
프로그램명 : 두 수 더하기
작성자 : 홍길동
작성일 : 2021.9.20
'''


a = 10  # 변수 a에 10 저장
b = 20  # 변수 b에 20 저장

c = a + b  # 두 수를 더해 변수 c에 저장

# 결과를 출력한다.
print(c)


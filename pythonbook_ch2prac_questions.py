# Question2

a = 7
b = 10

c = a+b*2
c %= 5
c **= 3
c -= c*10

print(c)



# Question3_1

'''
the result should be

반지름을 입력하세요: 10
반지름 : 10cm
원의 둘레 : 62.80cm
원의 면적 : 314.00 cm^2
'''

print('반지름을 입력하세요:')
print('반지름: cm')
print('원의 둘레: %.2fcm')
print('원의 면적: %.2fcm^2')


# Question3_2
radius = int(input('반지름을 입력하세요:'))
print('반지름: %dcm' % radius)

C = 2*3.14*radius

print('원의 둘레: %.2fcm' % C)

S = 3.14*radius*radius

print('원의 면적: %.2fcm^2' % S)



#Question4
book_price = int(input('책 값을 입력하세요:'))
sale_percentage = int(input('할인율을 입력하세요:'))
delivery_fee = int(input('배송료를 입력하세요:'))

totalprice = book_price - (book_price * sale_percentage / 100) + delivery_fee
total_price = print('%d원' % totalprice)


#Question5
name = str(input('이름을 입력하세요:'))
year = int(input('현재년을 입력하세요:'))
birth_year = int(input('탄생년을 입력하세요:'))
age = year - birth_year + 1
print('%s님의 나이는 %d세 입니다!' %(name, age))


#Question6
year = 2020
print('연을 입력하세요: %d' % year)

month = 1
print('월을 입력하세요: %d' % month)

day = 18
print('일을 입력하세요: %d' % day)


a = '%d-%02d-%02d' % (year, month, day)
print(a)









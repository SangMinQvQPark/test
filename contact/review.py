print('''주식은 대박이다''')
# 2-1
Daum = 89000
Naver = 751000
total = Daum * 100 + Naver * 20
print('someone has the money :',total)
# 2-2
loss_total = (Daum * 0.05) * 100 + (Naver * 0.1) * 20
# 2-3

F = 50
C = (F-32)/1.8
print('현재 화씨 온도는 50.0도 섭씨 온도는', C)

# 2-4
print('loss total_price :', loss_total)
while 1:
    print('pizza\n'*10)
    break
# 2-5
monday_stock = 1000000 * 0.7
tuesday_stock = monday_stock * 0.7
wednesday_stock = tuesday_stock * 0.7
print(wednesday_stock)

# 2-6
name = '박상민'
birth_day = '98.12.02'
SSN = '981202-0000000'
print('이름 : %s'%name)
print('생년월일 : %s' %birth_day)
print('주민등록번호 : %s' %SSN)

# 2-7
s = 'Daum KaKao'
s = s[5:] + ' ' + s[0:4]
print('이름 바꾸기 : ',s)

# 2-8
a = 'hello world'
a = 'hi ' + a[6:]
print(a)

# 2-9
x = 'abcdef'
x = x[1:] + x[0]
print(x)

# 3-1

naver_list = [ '날짜', '요일', '종가']
naver_list[0] = [ '09/07', '09/08', '09/09', '09/10', '09/11' ]
naver_list[1] = [ '뤟', '화', '수' , '목', '금']
naver_list[2] = [ 474500, 461500, 501000, 500500, 488500 ]
naver_list_date = naver_list[0]
naver_list_day = naver_list[1]
naver_closing_price = naver_list[2]
print('네이버 일주일 종가 : ', naver_closing_price)

# 3-2 3-3 3-4 3-5 3-6
max_ncp = max(naver_closing_price)
min_ncp = min(naver_closing_price)
between_max_min = max_ncp - min_ncp
print(max_ncp)
print(min_ncp)
print(between_max_min)
print('네이버 수요일 종가:',naver_closing_price[2])

naver_closing_price2 = {'09/07':474500, '09/08':461500, '09/09':501000, '09/10': 500500, '09/11':488500}
print(naver_closing_price2)

print(naver_closing_price2['09/09'])

# 4-1
for i in range(5):
    print('*',end='')

print(' ')

# 4-2
for i in range(5):
    for d in range(5):
        print('*',end='')
    print('')

# 4-3
for i in range(5):
    for d in range(i+1):
        print('*',end='')
    print('')

# 4-4
for i in range(5):
    for d in range(5-i):
        print('*',end='')
    print('')

# 4-5
for i in range(5):
    for d in range(4-i):
        print(' ',end='')
    for f in range(i+1):
        print('*',end='')
    print('')

# 4-6
for i in range(5):
    for f in range(i):
        print(' ', end='')

    for d in range(5-i):
        print('*',end='')
    print('')

# 4-7
for i in range(5):
    for f in range(4-i):
        print(' ',end='')
    for d in range((2*i)+1):
        print('*',end='')
    print('')

# 4-8
for i in range(5):
    for d in range(i):
        print(' ',end='')
    for f in range(9-i*2):
        print('*',end='')
    print('')

# 4-9

apart = [[101,102,103,104], [201,202,203,204], [301,302,303,304], [401,402, 403, 404]]
apart_newspaper_except = [101,203,301,404]
floor_1 = apart[0]
floor_2 = apart[1]
floor_3 = apart[2]
floor_4 = apart[3]

for floor in apart:
    for home_number in floor:
        if home_number in apart_newspaper_except:
                continue
        else:
            print("delivered : ", home_number)

# 5-1
def myaverage(a,b):
    return (a+b)/2

print(myaverage(2,3))

# 5-2
def get_max_min(data_list):
    max_val = max(data_list)
    min_val = min(data_list)
    return  (max_val,min_val)

max_val, min_val = get_max_min([2,3,4])
max_val
min_val

# 5-3
import os
def get_txt_list(path):
    org_list = os.listdir(path)
    ret_list = []
    for x in org_list:
        if x.endswith('txt'):
            ret_list.append(x)
    return ret_list

print(get_txt_list('d:/'))

# 5-4

def get_bmi_index(weight, height):
    height = height * 0.01
    bmi = weight / (height*height)
    if bmi < 18.5:
        print('마른 체형')
    elif 18.5 <= bmi < 25.0:
        print('표준')
    elif 25.0 <= bmi < 30.0:
        print('비만')
    else:
        print('고도비만')

print(get_bmi_index(93,180))

# 5-5
def cal_bmi2(height, weight):
    height = height * 0.01
    bmi = weight / (height * height)
    print("BMI: ", bmi)
    if bmi < 18.5:
        print("마른체형")
    elif 18.5 <= bmi < 25.0:
        print("표준")
    elif 25.0 <= bmi < 30.0:
        print("비만")
    else:
        print("고도비만")

#
# while 1:
#     height = input("Height (cm): ")
#     weight = input("Weight (kg): ")
#     cal_bmi2(float(height), float(weight))
#     break

# 5-6
def get_triangle_area(width, height):
    return width * height / 2

print(get_triangle_area(2,3))


# 5-7
def add_start_to_end(start,end):
    return sum(range(start,end+1))
print(add_start_to_end(1,10))

# 5-8
def get_religion_list(list):
    result = []
    for get_thr in list:
        result.append(get_thr[:3])
    return result

print(get_religion_list(['seoul', 'ouelsan', 'dauegeon']))

# 6-1
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def setx(self, x):
        self.x = x

    def sety(self, y):
        self.y = y

    def get(self):
        return (self.x, self.y)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

a = Point(3,3)
print(a.get())

a.setx(4)
a.sety(2)
print(a.get())

a.move(-4,-2)
print(a.get())

class Stock:
    market = "kospi"
a = Stock()
b = Stock()
a.market = "kosdaq"
print(a.market)
print(b.market)

# >>> a.market
# ??? kospi
# >>> b.market
# ??? kospi
# >>> Stock.market
# ??? kospi
# >>> a.market = "kosdaq"
# >>> b.market = "nasdaq"
# >>> a.market
# ??? kosdaq
# >>> b.market
# ??? nasdaq
# >>> Stock.market
# ??? kospi
# >>>

# 7-0
# f = open('D:\\s.txt','rt')
# lines = f.readlines()
# print(lines)

# # 7-0
# f = open('D:\\s.txt','wt')
# for d in range(2):
#     f.write(input('')+'\n')

# 7-1
f = open('d:\\s.txt','wt')
for x in range(1,11):
    f.write('%d\n' % x)
f.close()

import os
def print_filst(path):
    f = open('d:\\x.txt','wt')
    flist = os.listdir(path)
    for x in flist:
        f.write('%s\n' % x)
    f.close()

print_filst('d:\\')
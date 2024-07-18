# 柯博文作業
# 1.  透過python 印出以下的數字 while
#        2,3,4,5,6,7,8
# 2.  透過python 印出以下的數字 for in
#        2,4,6
# 3.  把第一題 修改一下 把 if 數字3 改成國字的參 印出
#        2,參,4,5,6,7,8

# 4. 把第二題 修改一下   做出 雙數乘法表 印出如下  (雙迴圈)
#   2*2=4
#   2*4=8
#   2*6=12
#   4*2=8
#   4*4=16
#   4*6=24  
#   6*2=12
#   6*4=24
#   6*6=36
   
# 5. 接著上一個題目
#    透過 if 處理
#    如果答案為  4, 24  就顯示 "我不喜歡數字四"  (雙迴圈 if)
#    印出如下的答案

#   我不喜歡數字四
#   2*4=8
#   2*6=12
#   4*2=8
#   4*4=16
#   我不喜歡數字四  
#   6*2=12
#   我不喜歡數字四
#   6*6=36


# 6.  把 第五題 包成一個 def 函數 叫做 fun1  並使用他



'''
#(1)
a = 2
while (a < 9):
	print(a)
	a += 1


#(2)
for b in range(2,8,2) : print (b)


#(3)
a = 2
while a < 9 :
	if a == 3: 
	    print(f"參" ) 
    else:
	    print(f'{a}')
    a += 1

(4)
for b in range(2,8,2) :
    for c in range(2,8,2) :
        print (f'{b} * {c} = {b*c}')
    

(5)  
for a in range(2,8,2):
    for b in range(2,8,2):
        if(a*b == 4 or a*b == 24):
            print("我不喜歡四")
        else:
            print(f'{a} * {b} = {a*b} ')
'''
(6)
def fun1 (a,b) :
    for a in range(2,8,2):
        for b in range( 2,8,2):
            if( a*b == 4 or a*b == 24):
                 print( "我不喜歡四")
            else:
                print(f'{a} * {b} = {a*b} ')

#fun1(1,10)

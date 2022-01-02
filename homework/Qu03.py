'''
[문제 3]
아래와 같은 패턴의 별(*)을 출력하는 프로그램을 작성해보세요.

*
**
***
****
*****
'''
'''방법1'''
for i in range(5):    # 행 5개
    for j in range(5): # * 1~5개
        if i>=j:    # i행이면 * i개 출력
            print('*', end='')
    print() # 한 행 출력 후 줄바꿈

'''방법2'''
for i in range(1,6):    # 행 5개
    for j in range(1,i+1): # i의 개수만큼 * 출력
        print('*', end='')
    print() # 한 행 출력 후 줄바꿈
    
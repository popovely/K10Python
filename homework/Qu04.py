'''
[문제 4]
아래와 같은 패턴의 별(*)을 출력하는 프로그램을 작성해보세요.

*****   # 1행 * 5개
****    # 2행 * 4개
***     # 3행 * 3개
**      # 4행 * 2개
*       # 5행 * 1개
'''
'''방법1'''
for i in range(1,6):     # 행 5개
    for j in range(1,6): # * 1~5개
        if i<=j:
            print('*', end='')
    print()
 
'''방법2'''
for i in range(1,6):     # 행 5개
    for j in range(i,6):
        print('*', end='')
    print()
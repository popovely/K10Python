'''
[문제 7]
아래와 같은 패턴의 별(*)을 출력하는 프로그램을 작성해 보세요.

    *       # 1행 : 4 / 별 1개 (2i-1)
   ***      # 2행 : 3 / 별 3개
  *****     # 3행 : 2 / 별 5개
 *******    # 4행 : 1 / 별 7개
*********   # 5행 : 0 / 별 9개
'''
'''기본형태
for i in range(1,6):     # 1~5행
    for j in range(1,6-i): # 1~(5-i)까지 공백
        print(' ', end='')
    for j in range(1,i+1):  # 1~i까지 별
        print('*', end=' ')
    print()
'''
'''range표현방식1'''
for i in range(1,6):     # 1~5행
    for j in range(1,6-i): # 1~(5-i)까지 공백
        print(' ', end='')
    for j in range(1,2*i):  # 별 2i-1개
        print('*', end='')
    print()
    
'''range표현방식2'''
for i in range(5):     # 0~5행
    for j in range(4-i): # 0~(4-i)까지 공백
        print(' ', end='')
    for j in range(2*i+1):  # 0~별 2i-1개
        print('*', end='')
    print()
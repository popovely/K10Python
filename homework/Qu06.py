'''
[문제 6]
아래와 같은 패턴의 별(*)을 출력하는 프로그램을 작성해 보세요.

* * * * *   # 1행 : 0 / 별 5개
 * * * *    # 2행 : 1 / 별 4개
  * * *     # 3행 : 2 / 별 3개
   * *      # 4행 : 3 / 별 2개
    *       # 5행 : 4 / 별 1개
'''
'''기본형태'''
for i in range(1,6):     # 행 5개
    for j in range(i,6):
        print('*', end='')
    print()

'''해당문제'''
for i in range(1,6):     # 1행
    for j in range(1,i): # 공백0개
        print(' ', end='')
    for j in range(i,6):  # 별 5개
        print('*', end=' ')
    print()
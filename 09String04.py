'''
replace('바꿀문자열', '새문자열')
    : 특정 문자열을 찾아 변경한다.
'''
print("="*5, "replace()", "="*20)
print('Hello, world!'.replace('world', 'Python'))

s = 'Hello, world!'
s = s.replace('world!', 'Python')
print(s)

'''
문자바꾸기
    translate()는 문자열 안의 문자를 다른 문자로 변경한다.
    
maketrans('바꿀문자', '새문자')로 변환 table을 만든 후
translate()함수를 통해 table의 내용을 변경한다.
'''
print("="*5, "maketrans()/translate()", "="*20)
str1 = "apple"
table = str1.maketrans('aeiou', '12345')    # a는 1로, e는 2로 변경
print(str1.translate(table))

str2 = "한글은 아름다운 언어"
table = str2.maketrans('한아언', 'XYZ') # '한'은 X, '아'는 Y로 변경
print(str2.translate(table))

'''
'구분자'.join(합칠문자열)
    : 합칠 문자열을 구분자를 통해 합쳐서 반환한다.
'''
print("="*5, "join()", "="*20)
print('-'.join(['010', '7906', '3600']))

print("="*5, "join()", "="*20)
print('-'.join(['010', '7906', '3600']))

'''
공백삭제 혹은 특정 문자 삭제

lstrip(문자) : 왼쪽의 해당 문자 삭제
rstrip(문자) : 오른쪽의 해당 문자 삭제
strip(문자) : 양쪽의 해당 문자 삭제

()안에 별도의 인자가 없으면 공백이 삭제된다.
'''
print("="*5, "strip()", "="*20)
str = "#^%오늘은 @@파이썬 @@ 공부하는날#^%"
print(str.lstrip('#'))
print(str.rstrip('%'))
print(str.rstrip('%').lstrip('#').replace('@', ''))

'''
열 위치 찾기
find(문자열) : 왼쪽에서부터 찾아서 인덱스 반환
rfind(문자열) : 오른쪽에서부터 찾아서 인덱스 반환

[참고] JAVA의 index of()와 같음
'''
print("="*5, "find()", "="*20)
print('apple pineapple'.find('pl'))
print('apple pineapple'.rfind('pl'))
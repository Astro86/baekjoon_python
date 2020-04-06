# 단어의 개수

##
`upper()` : 모든 문자를 대문자로 변경하고 싶을 때 사용하는 함수
`set()` : 입력받은 원소, 리스트, dictionary들을 중복되는 원소가 없는 집합으로 만들어주는 함수
`count(x)` : 문자열 내에 x의 개수를 카운트 하는 함수

## 전체 코드
```python
words = input().upper()
words_list = list(set(words))
word_count = list()


for i in words_list:
    count = words.count(i)
    word_count.append(count)

if(word_count.count(max(word_count)) >= 2):
    print('?')
else:
    print(words_list[(word_count.index(max(word_count)))])
```
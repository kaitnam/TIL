#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://programmers.co.kr/learn/courses/30/lessons/86051

# 0부터 9까지의 숫자 중 일부가 들어있는 배열 numbers가 매개변수로 주어집니다. 
# numbers에서 찾을 수 없는 0부터 9까지의 숫자를 모두 찾아 더한 수를 return 하도록 
# solution 함수를 완성해주세요.

# 제한사항
# 1 ≤ numbers의 길이 ≤ 9
# 0 ≤ numbers의 모든 수 ≤ 9
# numbers의 모든 수는 서로 다릅니다.

# 입출력 예
# numbers	result
# [1,2,3,4,6,7,8,0] 	14
# [5,8,4,0,6,7,9]	6


# In[1]:


# numbers 안에 있는 숫자 더하기

def solution(numbers):
    answer = 0
    for i in numbers:
        answer += i
    return answer


# In[2]:


solution([1,2,3,4,5])


# In[3]:


# numbers 안에 없는 숫자 더하기

def solution(numbers):
    answer = 0
    for i in range(0,10):
        if i not in numbers:
            answer += i
        else:
            pass
    return answer


# In[4]:


solution([1,3,5,7,9])


# ## <정리>
# - ### '숫자가 리스트에 없으면~' 이라고 하려면 "not in" 사용
# - ### range를 쓸때 range(start, stop) 인데 stop값이 stop-1 이므로 0부터 9까지이면 range(0, 10) 이렇게 써야한다.

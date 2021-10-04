# Problem: Programmers Hash #01
# Final Solution 
def solution(participant, completion):
    answer = ''
    hash = {}
    for name in participant:
        hash[name] = 0
    for name in participant:
        hash[name] += 1
    for name in completion:
        hash[name] -= 1
        if hash.get(name) == 0:
            del hash[name]
    answer = list(hash.keys())
    return answer

'''
# First Solution
# Not use Hash, O(N^2) => time complexcity FAILED

def solution(participant, completion):
    answer = ''
    for name in participant:
        if name in completion:
            completion.remove(name)
            continue
        answer = name
        break
    return answer
 '''

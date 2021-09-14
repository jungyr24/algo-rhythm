# 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
# 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
# 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
# 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
# 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
# 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
#      만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
# 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.

# 아이디의 길이는 3자 이상 15자 이하여야 합니다.
# 아이디는 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.) 문자만 사용할 수 있습니다.
# 단, 마침표(.)는 처음과 끝에 사용할 수 없으며 또한 연속으로 사용할 수 없습니다.


def upper_to_lower(id):
    return id.lower()
def remove_forbidden_str(id):
    tmp = []
    for s in id:
        if s.isalpha() or s.isdigit() or s in ['-', '_', '.']:
            tmp.append(s)
    
    return ''.join(tmp)
def check_count_period(id):
    id = list(id)

    tmp = []
    is_period = False
    for s in id:
        if s != '.':
            tmp.append(s)
            if is_period == True:
                is_period = False
        elif s == '.' and is_period == False:
            is_period = True
            tmp.append(s)

    return ''.join(tmp)
def remove_period(id):
    id = list(id)
    is_not_check = True
    while len(id) != 0 and is_not_check:
        print(id)
        if id[0] == '.':
            id.pop(0)
        elif id[-1] == '.':
            id.pop(len(id)-1)
        
        elif id[0] != '.' and id[-1] != '.':
            is_not_check = False

    return ''.join(id)

def check_length(id):
    tmp = id
    if len(id) > 15:
        new_tmp = tmp[:15]
        return remove_period(new_tmp)
    else:
        return id
def is_empty(id):
    id = list(id)
    if len(id) == 0:
        id.append('a')
    return ''.join(id)
def under_len_two(id):
    id = list(id)
    if len(id) <= 2:
        while len(id) < 3:
            id.append(id[-1])
    return ''.join(id)
def solution(new_id):
    answer = upper_to_lower(new_id)
    answer = remove_forbidden_str(answer)
    answer = check_count_period(answer)
    answer = remove_period(answer)
    answer = check_length(answer)
    answer = is_empty(answer)
    answer = under_len_two(answer)
    
    return answer


print(solution("...!@BaT#*..y.abcdefghijklm")) # bat.y.abcdefghi
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p")) #abcdefghijklmn
print(solution("......a......a......a....."))

# ----------------------------------------------------------------------------
def solution2(new_id):
    answer = ''
    # 1
    new_id = new_id.lower()
    # 2
    for c in new_id:
        if c.isalpha() or c.isdigit() or c in ['-', '_', '.']:
            answer += c
    # 3
    while '..' in answer:
        answer = answer.replace('..', '.')
    # 4
    if answer[0] == '.':
        answer = answer[1:] if len(answer) > 1 else '.'
    if answer[-1] == '.':
        answer = answer[:-1]
    # 5
    if answer == '':
        answer = 'a'
    # 6
    if len(answer) > 15:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    # 7
    while len(answer) < 3:
        answer += answer[-1]
    return answer

# ----------------------------------------------------------------------------
import re

def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st
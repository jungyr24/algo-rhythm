def solution(id_list, report, k):
    sender_dict = {}
    receiver_dict = {}
    id_dict = {}

    for id in id_list:
        id_dict[id] = 0
        sender_dict[id] = []
        receiver_dict[id] = []

    for s in report:
        sender, receiver = s.split(" ")
        if sender not in receiver_dict[receiver]:
            receiver_dict[receiver].append(sender)
            sender_dict[sender].append(receiver)

    for sender in sender_dict:
        for receiver in sender_dict[sender]:
            if len(receiver_dict[receiver]) >= k:
                id_dict[sender] += 1
        
    return list(id_dict.values())

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))
print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))
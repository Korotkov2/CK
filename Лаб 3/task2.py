# TODO Напишите функцию find_common_participants
def find_common_participants(first, second, ar=','):
    first_team = first.split(ar)
    second_team = second.split(ar)
    common = list(set(first_team).intersection(second_team))
    common.sort()
    return common

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
result = find_common_participants(participants_first_group, participants_second_group, '|')
# TODO Провеьте работу функции с разделителем отличным от запятой
print("Общие участники", result)
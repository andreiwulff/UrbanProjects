# print('I study at {}{}'.format('Urban ', 'university'))
# print(f'{'Urban'} is the best university')


# Использование %:
# Количество участников первой команды (team1_num):
team1_num = 5
result = 'Encoding Masters Team has participants: %d !' % team1_num
print(result)

# Количество участников в обеих командах (team1_num, team2_num):
team1_num = 5
team2_num = 6
result = 'Totally for today teams have participants: %d и %d !' % (team1_num, team2_num)
print(result)

# Использование format():
# Количество задач решённых командой 2 (score_2):
score_2 = 42
result = 'Data Magicians Team has solved tasks: {} !'.format(score_2)
print(result)

# Время за которое команда 2 решила задачи (team1_time):
team1_time = 18015.2
result = 'Data Magicians has solved tasks for {:.1f} с !'.format(team1_time)
print(result)

# Использование f-строк:
# Количество решённых задач по командам: score_1, score_2:
score_1 = 40
score_2 = 42
result = f'Teams have solved {score_1} and {score_2} tasks.'
print(result)

# Исход соревнования (challenge_result):
challenge_result = 'Encoding Masters Win!'
result = f'Result of challenge: {challenge_result}'
print(result)

# Количество задач (tasks_total) и среднее время решения (time_avg):
tasks_total = 82
time_avg = 350.4
result = f'Today solved {tasks_total} tasks, on average {time_avg:.1f} seconds for 1 task!'
print(result)

# Расчет переменной challenge_result:
score_1 = 40
score_2 = 42
team1_time = 18015.2
team2_time = 17000.0

if score_1 > score_2 or (score_1 == score_2 and team1_time > team2_time):
    challenge_result = 'Encoding Masters Win!'
elif score_1 < score_2 or (score_1 == score_2 and team1_time < team2_time):
    challenge_result = 'Data Magicians Win!'
else:
    challenge_result = 'Draw Game!'
result = f'Result of Challenge: {challenge_result}'
print(result)
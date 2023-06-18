import random


member = open('static/member.txt', 'r')
task = open('static/task.txt', 'r')

members = member.readlines()
tasks = task.readlines()

members = list(map(lambda member : member.strip(),members))
tasks = list(map(lambda task : task.strip(),tasks))

number_of_members = len(members)
number_of_tasks = len(tasks)

random_choice_member = random.sample(members,number_of_members)
random_choice_task = random.sample(tasks, number_of_tasks)

result = open('result/Result.txt', 'w')

for i in range(number_of_members):
    result.writelines('Task : '+ random_choice_task[i] + ' is set to ' + random_choice_member[i] +'\n')

# The results will be saved on result directory in text format
lists = ['hello','how']

cont_list = ''

for item in lists:
    cont_list = item + '_' + cont_list
    
print(cont_list)

cont_list = lists[0] + '_' + lists[1]
print(cont_list)
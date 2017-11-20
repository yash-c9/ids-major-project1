rf = open('kdd_required2.csv', 'a+')
of = open('KDDTrain+.txt', 'r')
rf.write('Protocol_type,Service,Land,Wrong_Fragmant,Num_Failed_Login,Logged_in,Root_Shell,Is_guest_login\n')


dict1 = {}
dict2 = {}
count1=0
count2=0
for line in of:
	element = line.split(',')
	if element[41] != 'normal':
		element[41] = 'not-normal'

	if element[1] in dict1:
		element[1] = str(dict1[element[1]])
	else:
		dict1[element[1]] = count1
		count1 += 1
		element[1] = str(dict1[element[1]])

	if element[2] in dict2:
		element[2] = str(dict2[element[2]])
	else:
		dict2[element[2]] = count2
		count2 += 1
		element[2] = str(dict2[element[2]])

	res_string = element[1]+','+element[2]+','\
				+element[6]+','+element[7]+','+element[10]+','\
				+element[11]+','+element[13]+','+element[21]+','+element[41]+'\n'
	rf.write(res_string)
rf = open('kdd_required_test2', 'a+')
of = open('KDDTest-21.txt', 'r')
rf.write('Protocol_type,Service,Land,Wrong_Fragmant,Num_Failed_Login,Logged_in,Root_Shell,Is_guest_login')

for line in of:
	element = line.split(',')
	res_string = element[1]+','+element[2]+','\
				+element[6]+','+element[7]+','+element[10]+','\
				+element[11]+','+element[13]+','+element[21]+','+element[41]+'\n'
	rf.write(res_string)
for i in range(1,13):
	end_day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	week = {"일" : 0, "월" : 1, "화" : 2, "수" : 3, "목" : 4,
		"금" : 5, "토" : 6}
	print(" {} 월".format(i))
	print("")
	print("일   월   화   수   목   금   토")
	count += end_day[i-1]
	count_num = (week[first_day] + count%7)%7
	print("     "*count_num, end = "")
	for j in range(1,8 - count_num):
		print("{}".format(j), end="    ")
	print("")
	for j in range(8 - count_num, 15 - count_num):
		print("{}".format(j), end="   ")
		if j < 10:
			print("", end= " ")
	print("")
	for j in range(15 - count_num, 22 - count_num):
		print("{}".format(j), end = "   ")
		if j < 10 :
			print("", end = " ")
	print("")
	if 29 - count_num <= end_day[i]:
		for j in range( 22- count_num, 29 - count_num):
			print("{}".format(j), end = "   ")
		print("")
		if end_day[i] - (29 -count_num) >= 7:
			for j in range( 29- count_num, 36- count_num):
				print("{}".format(j), end = "   ")
			print("")
			for j in range( 36 - count_num,  end_day[i] + 1):
				print("{}".format(j), end = "   ")
			print("")
		else:
			for j in range( 29- count_num, end_day[i] + 1):
				print("{}".format(j), end = "   ")
			print("")
	else:
		for j in range( 22- count_num, end_day[i] +1):
			print("{}".format(j), end = "   ")
	print("")
	print("")

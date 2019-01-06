end_day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for i in range(1,13):
    print("{} 월\n".format(i))
    print(" 일  월  화  수  목  금  토")
    for j in range(1,6):
        if j == 1:
            for k in range(1,8):
                print(" {}".format(k), end = "  ")
        elif j == 2:
            print("")
            for k in range(8,15):
                if k < 10:
                    print("", end = " ")
                print("{}".format(k), end = "  ")
        elif j == 3:
            print("")
            for k in range(15,22):
                print("{}".format(k), end= "  ")
        elif j == 4:
            print("")
            for k in range(22,29):
                print("{}".format(k), end= "  ") 
        elif j == 5:
            print("")
            for k in range(29,end_day[i]+1):
                print("{}".format(k), end= "  ")
                
        print("")
    print("")

def program(num):
    print("Your input number is: " + str(num))
    p_list = list()
    c = 0
    for n in range(1000**num):
        if c == num:
            break
        elif (sum(int(digit) for digit in str(n))) == 10:
            #print(n)
            p_list.append(n)
            c+=1
    print("The " + str(num) + "th perfect number is " + str(p_list[num-1]))
    print("...")

program(1)
program(2)
program(3)
program(3000000)
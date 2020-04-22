def program(num):
    print("Your input number is: " + str(num))
    for n in range(num):
        if num % 10 == 1:
            text_var = "st"
        elif num % 10 == 2:
            text_var = "nd"
        elif num % 10 == 3:
            text_var = "rd"
        else:
            text_var = "th"
    print(str(num) + "'s N-th is called: " + str(num) + str(text_var))


for i in range(0, 12): #1~12
    program(i+1)



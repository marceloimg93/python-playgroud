is_male = True
is_tall = False

if is_male and not is_tall:
    print("is male and it is not tall")
elif is_male or is_tall:
    print("is male or is tall")
else:
    print("Well...")

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else: 
        return num3

greatest_number = max_num(1,2,3)
print("Greatest number is: " + str(greatest_number))